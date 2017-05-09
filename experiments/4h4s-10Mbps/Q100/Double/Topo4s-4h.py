	
#!/usr/bin/python
'''
2 host and 2 switch topo to work with Pox controller and timings/  timesatamps
Delay/link imparement is in between switches.

'''

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSKernelSwitch, UserSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.link import Link, TCLink


def topology():
	"Create a network."
	net = Mininet( controller=RemoteController, link=TCLink, switch=OVSKernelSwitch )
	print "*** Creating nodes"
	h1 = net.addHost( 'h1', mac = '00:00:00:00:00:01')
	h2 = net.addHost( 'h2', mac = '00:00:00:00:00:02')
	h3 = net.addHost( 'h3', mac = '00:00:00:00:00:03')
	h4 = net.addHost( 'h4', mac = '00:00:00:00:00:04')
	
	s1 = net.addSwitch('s1')
	s2 = net.addSwitch('s2')
	s3 = net.addSwitch('s3')
	s4 = net.addSwitch('s4')
	
	c0 = net.addController('c0', controller = RemoteController, defaultIP ='127.0.0.1',port=6633)

	# between hosts & switches
	net.addLink(h1, s1, intfName1='h1-eth0', intfName2='s1-eth1')
	net.addLink(h2, s2, intfName1='h2-eth0', intfName2='s2-eth1')
	net.addLink(h3, s3, intfName1='h3-eth0', intfName2='s3-eth1')
	net.addLink(h4, s4, intfName1='h4-eth0', intfName2='s4-eth1')

	net.addLink(s1, s2, intfName1='s1-eth2', intfName2='s2-eth2')#, delay='20ms')
	net.addLink(s2, s3, intfName1='s2-eth3', intfName2='s3-eth2',bw=10, delay='10ms',max_queue_size=100)
	net.addLink(s3, s4, intfName1='s3-eth3', intfName2='s4-eth2')#, delay='20ms')

	print "*** Starting network"
	net.build()
	c0.start
	s1.start([c0])
	s1.cmd('switch s1 start')
	s2.start([c0])
	s2.cmd('switch s2 start')
	s3.start([c0])
	s3.cmd('switch s3 start')
	s4.start([c0])
	s4.cmd('switch s4 start')

	# to set tcp segmentation tso, gro, gso offloading disabled

	h1.cmd('bash eth.sh')
	h2.cmd('bash eth.sh')
	h3.cmd('bash eth.sh')
	h4.cmd('bash eth.sh')
	s1.cmd('bash eth.sh')
	s2.cmd('bash eth.sh')
	s3.cmd('bash eth.sh')
	s4.cmd('bash eth.sh')
	s1.cmd('bash flowtable4s-4h.sh')
	s2.cmd('bash reno.sh')

	# h1.cmd('h1 ping h2 -c 2')

	# h2.cmd('tcpdump -i h2-eth2 -w server-tcpdump')
	# h1.cmd('tcpdump -i h1-eth2 -w client-tcpdump')
	# h2.cmd('iperf -s > server_output.txt &')
	# h1.cmd('iperf -c ', h1.IP() + ' -i 1 -t 50   >  client_output.txt &')

	print "*** Running CLI"
	CLI( net )
	print "*** Stopping network"
	net.stop()

if __name__ == '__main__':
	setLogLevel( 'info' )
	topology()



















	
