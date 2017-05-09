
from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.util import dpidToStr
from pox.lib.addresses import EthAddr, IPAddr
import re


log = core.getLogger()

class Tutorial (object):
	def __init__ (self, connection):
		self.connection = connection
    	connection.addListeners(self)

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
def launch ():
	"""
	Starts the component
	"""
	def start_switch (event):
		log.debug("Controlling %s" % (event.connection,))
		Tutorial(event.connection)
	core.openflow.addListenerByName("ConnectionUp", start_switch)


# def _handle_ConnectionUp (event):

#   def to_controller(self, event):
#     msg = of.ofp_flow_mod()
#     msg.actions.append(of.ofp_action_output(port = of.OFPP_CONTROLLER))
#     event.connection.send(msg)
#     print '********', event.connection.send(msg)
#     log.info("Hubifying %s", dpidToStr(event.dpid))

#   def hub(self, event):
#     msg = of.ofp_flow_mod()
#     msg.actions.append(of.ofp_action_output(port = of.OFPP_FLOOD))
#     event.connection.send(msg)
#     print '********', event.connection.send(msg)
#     log.info("Hubifying %s", dpidToStr(event.dpid))

  

# def _handle_ConnectionUP(event):
#   self.send_packet(packet_in.buffer_id, packet_in.data,
#                      of.OFPP_FLOOD, packet_in.in_port)


	# def _handle_ConnectionUp (event):
	#   # log.debug("Connection %s" % (event.connection,))

	#   msg = of.ofp_flow_mod()
	#   msg.idle_timeout = 0
	#   msg.hard_timeout = 0
	#   # msg.match.of_dl_src = EthAddr('00:00:00:00:00:01')
	#   # msg.match.of_dl_dst = EthAddr('00:00:00:00:00:02')
	#   # msg.actions.append(of.ofp_action_output(port = 2))
	#   # core.openflow.sendToDPID(event.dpid, msg)
	#   # # msg.match.of_eth_src = EthAddr('00:00:00:00:00:01')
	#   # # msg.match.of_eth_dst = EthAddr('00:00:00:00:00:02')
	#   # # core.openflow.sendToDPID(event.dpid, msg)
	#   # msg.match = of.ofp_match(dl_src = EthAddr('00:00:00:00:00:01'),dl_dst = EthAddr('00:00:00:00:00:02'),dl_type=0x0800,nw_tos= 0, nw_proto =1,nw_src = IPAddr('10.0.0.1'),nw_dst = IPAddr('10.0.0.2'))
	#   # msg.actions.append(of.ofp_action_output(port = of.OFPP_FLOOD))
	#   msg.actions.append(of.ofp_action_output(port = of.OFPP_CONTROLLER))
	#   event.connection.send(msg)

# def _handle_ConnectionUp1 (event):


#   msg1 = of.ofp_flow_mod()
#   msg1.idle_timeout = 0
#   msg1.hard_timeout = 0
#   msg1.match.of_dl_src = EthAddr('00:00:00:00:00:02')
#   msg1.match.of_dl_dst = EthAddr('00:00:00:00:00:01')
#   # msg1.match = of.ofp_match(dl_src = EthAddr('00:00:00:00:00:02'),dl_dst = EthAddr('00:00:00:00:00:01'))
#   msg1.actions.append(of.ofp_action_output(port = 1))
#   # core.openflow.sendToDPID(event.dpid, msg)
#   event.connection.send(msg1)



# def launch ():
# 	core.openflow.addListenerByName("ConnectionUp", _handle_ConnectionUp)
  # core.openflow.addListenerByName("ConnectionUp", _handle_ConnectionUp1)
	# def start_switch (event):
	# 	log.debug("Controlling %s" % (event.connection,))
	# 	Tutorial(event.connection)
		# core.openflow.addListenerByName("ConnectionUp", start_switch)
  # log.info("Hub running.")
