#!/bin/bash

"APPLIED IN FOUR SWITCH TOPOLOGY"


from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.util import dpid_to_str
from pox.lib.util import str_to_bool
from pox.lib.addresses import EthAddr, IPAddr

import time

log = core.getLogger()
_flood_delay = 0


class LearningSwitch (object):
  log.info('ali.py is running')

  def __init__ (self, connection, transparent):
    # Switch we'll be adding L2 learning switch capabilities to
    self.connection = connection
    self.transparent = transparent
    connection.addListeners(self)

  # def __init__ (self, connection):
  #   self.connection = connection
  #   connection.addListeners(self)

  def _handle_PacketIn (self, event):
  
    packet = event.parsed
    dpidstr = dpid_to_str(event.dpid)

    # fm = of.ofp_flow_mod()
    # fm.match.in_port = 1
    # # fm.priority = 33002
    # fm.match.dl_type = 0x0800
    # fm.match.nw_src = IPAddr("10.0.0.1")
    # fm.match.nw_dst = IPAddr("10.0.0.4")
    # event.connection.send( fm )


    # s1
    if dpidstr=="00-00-00-00-00-01":
        fm = of.ofp_flow_mod()
        fm.match.in_port = 1
        # fm.priority = 33001
        fm.match.dl_type = 0x0800
        fm.match.nw_src = IPAddr("10.0.0.1")
        fm.match.nw_dst = IPAddr("10.0.0.4")
        fm.actions.append(of.ofp_action_output( port = of.OFPP_CONTROLLER ) )
        fm.actions.append(of.ofp_action_output( port = 2 ) )
        event.connection.send( fm )

        fm = of.ofp_flow_mod()
        fm.match.in_port = 2
        fm.priority = 33001
        fm.match.dl_type = 0x0800
        fm.match.nw_src = IPAddr("10.0.0.4")
        fm.match.nw_dst = IPAddr("10.0.0.1")
        fm.actions.append(of.ofp_action_output( port = 1 ) )
        event.connection.send( fm )

  

    #s2
    if dpidstr=="00-00-00-00-00-02":
        fm = of.ofp_flow_mod()
        fm.match.in_port = 2
        fm.priority = 33001
        fm.match.dl_type = 0x0800
        fm.match.nw_src = IPAddr("10.0.0.1")
        fm.match.nw_dst = IPAddr("10.0.0.4")
        fm.actions.append(of.ofp_action_output( port = of.OFPP_CONTROLLER ) )
        fm.actions.append(of.ofp_action_output( port = 3 ) )
        event.connection.send( fm )

        fm = of.ofp_flow_mod()
        fm.match.in_port = 3
        fm.priority = 33001
        fm.match.dl_type = 0x0800
        fm.match.nw_src = IPAddr("10.0.0.4")
        fm.match.nw_dst = IPAddr("10.0.0.1")
        fm.actions.append(of.ofp_action_output( port = 2) )
        event.connection.send( fm )

     #s3
    if dpidstr=="00-00-00-00-00-03":
        fm = of.ofp_flow_mod()
        fm.match.in_port = 2
        fm.priority = 33001
        fm.match.dl_type = 0x0800
        fm.match.nw_src = IPAddr("10.0.0.1")
        fm.match.nw_dst = IPAddr("10.0.0.4")
        fm.actions.append(of.ofp_action_output( port = of.OFPP_CONTROLLER ) )
        fm.actions.append(of.ofp_action_output( port = 3 ) )
        event.connection.send( fm )

        fm = of.ofp_flow_mod()
        fm.match.in_port = 3
        fm.priority = 33001
        fm.match.dl_type = 0x0800
        fm.match.nw_src = IPAddr("10.0.0.4")
        fm.match.nw_dst = IPAddr("10.0.0.1")
        fm.actions.append(of.ofp_action_output( port = 2) )
        event.connection.send( fm )


    #s4
    if dpidstr=="00-00-00-00-00-04":
        fm = of.ofp_flow_mod()
        fm.match.in_port = 2
        fm.priority = 33001
        fm.match.dl_type = 0x0800
        fm.match.nw_src = IPAddr("10.0.0.1")
        fm.match.nw_dst = IPAddr("10.0.0.4")
        fm.actions.append(of.ofp_action_output( port = of.OFPP_CONTROLLER ) )
        fm.actions.append(of.ofp_action_output( port = 1 ) )
        event.connection.send( fm )

        fm = of.ofp_flow_mod()
        fm.match.in_port = 1
        fm.priority = 33001
        fm.match.dl_type = 0x0800
        fm.match.nw_src = IPAddr("10.0.0.4")
        fm.match.nw_dst = IPAddr("10.0.0.1")
        fm.actions.append(of.ofp_action_output( port = 2) )
        event.connection.send( fm )

    # fm = of.ofp_flow_mod()
    # fm.match.in_port = 3
    # fm.priority = 33001
    # fm.match.dl_type = 0x0800
    # fm.match.nw_src = IPAddr("10.0.0.2")
    # fm.match.nw_dst = IPAddr("10.0.0.3")
    # fm.actions.append(of.ofp_action_output( port = 1 ) )
    # event.connection.send( fm )

    # fm = of.ofp_flow_mod()
    # fm.match.in_port = 1
    # fm.priority = 33001
    # fm.match.dl_type = 0x0800
    # fm.match.nw_src = IPAddr("10.0.0.3")
    # fm.match.nw_dst = IPAddr("10.0.0.2")
    # fm.actions.append(of.ofp_action_output( port = 3 ) )
    # event.connection.send( fm )

    # # ARP Flooding
    # fm = of.ofp_flow_mod()
    # fm.priority = 33001
    # fm.match.dl_type = 0x0806
    # fm.actions.append(of.ofp_action_output( port = of.OFPP_FLOOD ) )
    # event.connection.send( fm )


    # fm = of.ofp_flow_mod()
    # fm.match.in_port = 1
    # fm.priority = 33001
    # fm.match.dl_type = 0x0806
    # fm.actions.append(of.ofp_action_output( port = 2 ) )
    # event.connection.send( fm )

    # fm = of.ofp_flow_mod()
    # fm.match.in_port = 2
    # fm.priority = 33001
    # fm.match.dl_type = 0x0806
    # fm.actions.append(of.ofp_action_output( port = 1 ) )
    # event.connection.send( fm )

class l2_learning (object):


  def __init__ (self, transparent):
    core.openflow.addListeners(self)
    self.transparent = transparent

  def _handle_ConnectionUp (self, event):
    log.debug("Connection %s" % (event.connection,))
    LearningSwitch(event.connection, self.transparent)


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
