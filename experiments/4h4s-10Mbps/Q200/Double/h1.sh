#!/bin/bash

tcpdump -i h1-eth0 -s 120 -w h1 &

> /var/log/syslog

ovs-ofctl snoop s1 --timestamp 2> switch1 &
# ovs-ofctl snoop s2 --timestamps 2> switch2 &

ovs-ofctl snoop s4 --timestamp 2> switch4 &

iperf3 -c 10.0.0.4 -t200 -i1 > iperf3h1.txt