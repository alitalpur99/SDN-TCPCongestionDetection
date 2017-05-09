"""
command to run
$ ./pox.py log.level --DEBUG forwarding.my_dump_switch
An L2 learning switch, adding print (#MY)statement to understand its behavior. 
"""

from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.util import dpid_to_str
from pox.lib.util import str_to_bool
import time

log = core.getLogger()


class DumpSwitch (object):

	def __init__(self, connection):
		self.connection = connection
		connection.addListeners(self)
		self.mactoport = {}

	def _handle_packetIn(self, event):
		packet = event.parsed
		print packet
		print 'src mac:',packet.src
		print 'dst mac:',packet.dst
		self.mactoport[packet.src] = event.port
		
		if packet.dst not in self.mactoport:
			msg = of.ofp_packet_out()
			msg.actions.append(of.ofp_action_output(port = of.OFPP_FLOOD))
			msg.data = event.ofp
			msg.in_port = event.port
			self.connection.send(msg)

		else:
			port = self.mactoport[packet.dst]
			log.debug("installing flow for %s.%i > %s.%i"%(packet.src, event.port, packet.dst, port))
			msg = of.ofp_flow_mod()
			msg.match = of.ofp_match.from_packet(packet, event.port)
			msg.idle_timeout = 10 
			msg.hard_timeout = 30
			msg.actions.append(of.ofp_action_output(port = port))
			msg.data = event.ofp
			self.connection.send(msg)

class l2_learning (object):
	def __init__ (self):
		core.openflow.addListeners(self)

	def _handle_ConnectionUp(self,event):
		log.debug("connection %s"%(event.connection,))
		DumpSwitch(event.connection)

def launch ():
	core.registerNew(l2_learning)















		# def to_controller():
		# 	if packet.src == '00:00:00:01' or pacekt.dst == '00:00:00:01':
		# 		msg = of.ofp_packet_out()
		# 		msg.actions.append(of.ofp_action_output(port = of.OFPP_CONTROLLER))
		# 		msg.data = event.ofp
		# 		print 'message data', msg.data
		# 		self.connection.send(msg)
		# 	else:
				



