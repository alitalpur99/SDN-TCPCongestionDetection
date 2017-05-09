'''
 run command: $ ./pox.py log.level --DEBUG my_switch
description: every incoming packet to be sent to controller
'''
import pox.openflow.libopenflow_01 as of
from pox.lib.util import dpid_to_str
from pox.lib.util import str_to_bool
import time

log = core.getLogger()


class My_Switch (object):
	def __init__ (self, connection):
    # Switch we'll be adding L2 learning switch capabilities to
	self.connection = connection

	connection.addListeners(self)

	def _handle_PacketIn (self, event):

		ofp_match.from_packet
