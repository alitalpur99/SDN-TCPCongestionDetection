#!/bin/bash

tcpdump -i h4-eth0 -s 120 -w h4 &

iperf3 -s
