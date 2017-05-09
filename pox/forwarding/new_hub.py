from pox.core import core
import pox.openflow.libopenflow_01 as of
import re

log = core.getLogger()

class Tutorial (object):
  def __init__ (self, connection):
    self.connection = connection
    connection.addListeners(self)
    # Use this table to keep track of which ethernet address is on
    # which switch port (keys are MACs, values are ports).
    self.mac_to_port = {} 
    self.matrix={} # This will keep track of the traffic matrix. 
                   # matrix[i][j]=number of times a packet from i went to j
  def send_packet (self, buffer_id, raw_data, out_port, in_port):
    #Sends a packet out of the specified switch port.
    msg = of.ofp_packet_out()
    msg.in_port = in_port
    msg.data = raw_data
    # Add an action to send to the specified port
    action = of.ofp_action_output(port = out_port)
    msg.actions.append(action)
    # Send message to switch
    self.connection.send(msg)


  def act_like_hub (self, packet, packet_in):
    #flood packet on all ports
    self.send_packet(packet_in.buffer_id, packet_in.data,
                     of.OFPP_FLOOD, packet_in.in_port)


  def act_like_switch (self, packet, packet_in):
    # Learn the port for the source MAC
    self.mac_to_port[packet.src]=packet_in.in_port
    # Add the entry to the traffic matrix.
    if self.mac_to_port.get(packet.dst)!=None:
      # Send packet out the associated port
      self.send_packet(packet_in.buffer_id, packet_in.data,self.mac_to_port[packet.dst], packet_in.in_port)
    else:
      # Flood the packet out everything but the input port (same as hub)
      self.send_packet(packet_in.buffer_id, packet_in.data,
                       of.OFPP_FLOOD, packet_in.in_port)

  def _handle_PacketIn (self, event):
    """
    Handles packet in messages from the switch.
    """
    packet = event.parsed # This is the parsed packet data.
    if not packet.parsed:
      log.warning("Ignoring incomplete packet")
      return
    packet_in = event.ofp # The actual ofp_packet_in message.

    self.act_like_hub(packet, packet_in)
    self.act_like_switch(packet, packet_in)

def launch ():
  """
  Starts the component
  """
  def start_switch (event):
    log.debug("Controlling %s" % (event.connection,))
    Tutorial(event.connection)
  core.openflow.addListenerByName("ConnectionUp", start_switch)
