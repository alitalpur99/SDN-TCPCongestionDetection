"""
command to run
$ ./pox.py log.level --DEBUG forwarding.myl2_learning


An L2 learning switch, adding print (#MY)statement to understand its behavior. 

"""

from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.addresses import EthAddr, IPAddr
from pox.lib.util import dpid_to_str
from pox.lib.util import str_to_bool
import time

log = core.getLogger()

# We don't want to flood immediately when a switch connects.
# Can be overriden on commandline.
_flood_delay = 0

class LearningSwitch (object):
  """
  The learning switch "brain" associated with a single OpenFlow switch.

  When we see a packet, we'd like to output it on a port which will
  eventually lead to the destination.  To accomplish this, we build a
  table that maps addresses to ports.

  We populate the table by observing traffic.  When we see a packet
  from some source coming from some port, we know that source is out
  that port.

  When we want to forward traffic, we look up the desintation in our
  table.  If we don't know the port, we simply send the message out
  all ports except the one it came in on.  (In the presence of loops,
  this is bad!).

  In short, our algorithm looks like this:

  For each packet from the switch:
  1) Use source address and switch port to update address/port table
  2) Is transparent = False and either Ethertype is LLDP or the packet's
     destination address is a Bridge Filtered address?
     Yes:
        2a) Drop packet -- don't forward link-local traffic (LLDP, 802.1x)
            DONE
  3) Is destination multicast?
     Yes:
        3a) Flood the packet
            DONE
  4) Port for destination address in our address/port table?
     No:
        4a) Flood the packet
            DONE
  5) Is output port the same as input port?
     Yes:
        5a) Drop packet and similar ones for a while
  6) Install flow table entry in the switch so that this
     flow goes out the appopriate port
     6a) Send the packet out appropriate port
  """
 
  def __init__ (self, connection, transparent):
    # Switch we'll be adding L2 learning switch capabilities to
    self.connection = connection
    self.transparent = transparent
    # v=0
    # Our table
    self.macToPort = {}

    # We want to hear PacketIn messages, so we listen
    # to the connection
    connection.addListeners(self)
    print connection.addListeners

    # We just use this to know when to log a helpful message
    self.hold_down_expired = _flood_delay == 0

    #log.debug("Initializing LearningSwitch, transparent=%s",
    #          str(self.transparent))

  def _handle_PacketIn (self, event):
    """
    Handle packet in messages from the switch to implement above algorithm.
    """
    packet = event.parsed
    print packet.payload
    
    # MY
    # print event #<pox.openflow.PacketIn object at 0x7fa594607cd0>

    # print '**********************************pacekt.src =', packet.src

    #MY (output print packet [00:00:00:00:00:01>00:00:00:00:00:02 IP])
    # print '*********************************print whole packet', packet # parsing packet source and dst mac add

    def flood (message = None):
      """ Floods the packet """
      msg = of.ofp_packet_out()
      if time.time() - self.connection.connect_time >= _flood_delay:
        # Only flood if we've been connected for a little while...

        if self.hold_down_expired is False:
          # Oh yes it is!
          self.hold_down_expired = True
          log.info("%s: Flood hold-down expired -- flooding",
              dpid_to_str(event.dpid))

        if message is not None: log.debug(message)
        #log.debug("%i: flood %s -> %s", event.dpid,packet.src,packet.dst)
        # OFPP_FLOOD is optional; on some switches you may need to change
        # this to OFPP_ALL.
        msg.actions.append(of.ofp_action_output(port = of.OFPP_FLOOD))


      else:
        pass
        #log.info("Holding down flood for %s", dpid_to_str(event.dpid))
      msg.data = event.ofp
      
      #MY
      ##print '***********messg data printing',msg.data # no ouput
      
      msg.in_port = event.port
      self.connection.send(msg)

    def drop (duration = None):
      """
      Drops this packet and optionally installs a flow to continue
      dropping similar ones for a while
      """
      if duration is not None:
        if not isinstance(duration, tuple):
          duration = (duration,duration)
        msg = of.ofp_flow_mod()
        msg.match = of.ofp_match.from_packet(packet)
        msg.idle_timeout = duration[0]
        msg.hard_timeout = duration[1]
        msg.buffer_id = event.ofp.buffer_id
        self.connection.send(msg)
      elif event.ofp.buffer_id is not None:
        msg = of.ofp_packet_out()
        msg.buffer_id = event.ofp.buffer_id
        msg.in_port = event.port
        self.connection.send(msg)

    self.macToPort[packet.src] = event.port # 1

    if not self.transparent: # 2
      if packet.type == packet.LLDP_TYPE or packet.dst.isBridgeFiltered():
        drop() # 2a
        return

    if packet.dst.is_multicast:
      flood() # 3a
    else:
      if packet.dst not in self.macToPort: # 4
        flood("Port for %s unknown -- flooding" % (packet.dst,)) # 4a
      else:
        port = self.macToPort[packet.dst]
        if port == event.port: # 5
          # 5a
          log.warning("Same port for packet from %s -> %s on %s.%s.  Drop."
              % (packet.src, packet.dst, dpid_to_str(event.dpid), port))
          drop(10)
          return
        # 6
        log.debug("installing flow for %s.%i -> %s.%i" %
                  (packet.src, event.port, packet.dst, port))
        # msg = of.ofp_flow_mod()
        # msg.match = of.ofp_match.from_packet(packet, event.port)
        msg = of.ofp_packet_out()
        # msg.in_port = in

        # MY, show the wild cards, and other src,dest mac port ip add vlan etc
        # print 'PRINTING MSG.MATCH------------>',msg.match
        '''
        ofp_match
        wildcards: nw_tos|tp_dst|tp_src (1000000000000011000000 = 2000c0)
        in_port: 1
        dl_src: a6:80:d6:a7:08:cb
        dl_dst: de:f4:25:ce:52:5a
        dl_vlan: 65535
        dl_vlan_pcp: 0
        dl_type: 0x806
        nw_proto: 1
        nw_src: 10.0.0.1
        nw_dst: 10.0.0.2

        '''

        # msg.idle_timeout = 0 # 0 means permenant
        # msg.hard_timeout = 0
        # msg.actions.append(of.ofp_action_output(port = port))
        msg.actions.packet_out(of.ofp_action_output(port = port))
        # if port == 1 :
        #   print 'send to controller'
        #   msg.actions.append(of.ofp_action_output(port = of.OFPP_CONTROLLER))
        #   self.connection.send(msg)
        # else:
        #   pass
        '''above makes loop'''

        #, 
        # print 'port print000000000000000000000', port # print out going port
        # of.ofp_action_output(port = port)
        # print '++++', msg.actions() # no output
        # msg.data = event.ofp # 6a
        self.connection.send(msg)
        #My
        # print 'msg.data pring ==================>',msg.data
        '''
        msg.data pring ==================> ofp_packet_in
        header
        version: 1
        type:    10 (OFPT_PACKET_IN)
        length:  60
         xid:     0
        buffer_id: 263
        total_len: 42
        in_port: 2
        reason: 0
        data:
        '''
        

        #My
        # print 'PRINTING MSG',msg
        '''
        ofp_flow_mod
        header: 
        version: 1
        type:    14 (OFPT_FLOW_MOD)
        length:  80
        xid:     27
        match: 
        wildcards: nw_tos|tp_dst|tp_src (1000000000000011000000 = 2000c0)
        in_port: 1
        dl_src: a6:80:d6:a7:08:cb
        dl_dst: de:f4:25:ce:52:5a
        dl_vlan: 65535
        dl_vlan_pcp: 0
        dl_type: 0x806
        nw_proto: 2
        nw_src: 10.0.0.1
        nw_dst: 10.0.0.2
        cookie: 0
        command: 0
        idle_timeout: 1
        hard_timeout: 1
        priority: 32768
        buffer_id: None
        out_port: 65535
        flags: 0
        actions: 
        type: 0
        len: 8
        port: 2
        max_len: 0  '''            '''
        Packet-In Message:OFPT_PACKET_IN 
        reason; /* Reason packet is being sent (one of OFPR_*) *
        OFPR_ACTION /* Action explicitly output to controller. */
        '''



class l2_learning (object):
  """
  Waits for OpenFlow switches to connect and makes them learning switches.
  """
  def __init__ (self, transparent):
    core.openflow.addListeners(self)
    self.transparent = transparent

  def _handle_ConnectionUp (self, event):
    log.debug("Connection %s" % (event.connection,))
    LearningSwitch(event.connection, self.transparent)
    
    # msg = of.ofp_flow_mod()
    # msg.idle_timeout = 0
    # msg.hard_timeout = 0
    # msg.match.of_eth_src = EthAddr('00:00:00:00:00:01')
    # msg.match.of_eth_dst = EthAddr('00:00:00:00:00:02')
    # core.openflow.sendToDPID(event.dpid, msg)
    # msg.match = of.ofp_match(dl_src = EthAddr('00:00:00:00:00:01'),dl_dst = EthAddr('00:00:00:00:00:02'),dl_type=0x0800,nw_tos=7, nw_proto =1,nw_src = IPAddr('10.0.0.1'),nw_dst = IPAddr('10.0.0.2'))
    # msg.actions.append(of.ofp_action_output(port = of.OFPP_CONTROLLER))
    # event.connection.send(msg)

    # msg = of.ofp_flow_mod()
    # msg.idle_timeout = 0
    # msg.hard_timeout = 0
    # msg.match.of_eth_src = EthAddr('00:00:00:00:00:02')
    # msg.match.of_eth_dst = EthAddr('00:00:00:00:00:01')
    # msg.actions.append(of.ofp_action_output(port = 1))
    # core.openflow.sendToDPID(event.dpid, msg)
    # msg.match = of.ofp_match(in_port=1, dl_src = EthAddr('00:00:00:00:00:01'),dl_dst = EthAddr('00:00:00:00:00:02'),dl_type=0x0800,nw_tos= 0, nw_proto =1,nw_src = IPAddr('10.0.0.1'),nw_dst = IPAddr('10.0.0.2'))
    # event.connection.send(msg)
    


def launch (transparent=False, hold_down=_flood_delay):
  """
  Starts an L2 learning switch.
  """
  try:
    global _flood_delay
    _flood_delay = int(str(hold_down), 10)
    assert _flood_delay >= 0
  except:
    raise RuntimeError("Expected hold-down to be a number")

  core.registerNew(l2_learning, str_to_bool(transparent))
