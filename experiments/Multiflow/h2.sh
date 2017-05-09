#!/bin/bash

tcpdump -i h2-eth0 -w h2 &

# > /var/log/syslog

# ovs-ofctl snoop s1 --timestamp 2> switch1 &
# ovs-ofctl snoop s2 --timestamps 2> switch2 &

# ovs-ofctl snoop s4 --timestamp 2> switch4 &

iperf3 -c 10.0.0.5 -t200 -i1 > iperf3h2.txt