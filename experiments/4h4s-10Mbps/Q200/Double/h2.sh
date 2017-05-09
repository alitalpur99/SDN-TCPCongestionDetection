#!/bin/bash

# run Iperf at regular interval ( i.e. run for 3 sec, after every 3 sec of sleep )

# tcpdump -i h2-eth0 -w h2 

iperf(){
	echo $(date) >> iperf3h2.txt
	iperf3 -c 10.0.0.3 -t19 -i1 >> iperf3h2.txt

}

while true 
do 
	iperf
	sleep 3
done