#!/bin/bash

# 4switch 4host flow table configuration

#for switch-s1

ovs-ofctl add-flow s1 dl_type=0x806,nw_proto=1,action=flood
ovs-ofctl add-flow s1 dl_src=00:00:00:00:00:01,dl_dst=00:00:00:00:00:02,actions=output:2
ovs-ofctl add-flow s1 dl_src=00:00:00:00:00:01,dl_dst=00:00:00:00:00:03,actions=output:2
ovs-ofctl add-flow s1 dl_src=00:00:00:00:00:01,dl_dst=00:00:00:00:00:04,actions=output:2,controller

ovs-ofctl add-flow s1 dl_src=00:00:00:00:00:02,dl_dst=00:00:00:00:00:01,actions=output:1
ovs-ofctl add-flow s1 dl_src=00:00:00:00:00:03,dl_dst=00:00:00:00:00:01,actions=output:1
ovs-ofctl add-flow s1 dl_src=00:00:00:00:00:04,dl_dst=00:00:00:00:00:01,actions=output:1

#for switch-s2

ovs-ofctl add-flow s2 dl_type=0x806,nw_proto=1,action=flood
ovs-ofctl add-flow s2 dl_src=00:00:00:00:00:02,dl_dst=00:00:00:00:00:01,actions=output:2
ovs-ofctl add-flow s2 dl_src=00:00:00:00:00:02,dl_dst=00:00:00:00:00:03,actions=output:3
ovs-ofctl add-flow s2 dl_src=00:00:00:00:00:02,dl_dst=00:00:00:00:00:04,actions=output:3

ovs-ofctl add-flow s2 dl_src=00:00:00:00:00:01,dl_dst=00:00:00:00:00:02,actions=output:1
ovs-ofctl add-flow s2 dl_src=00:00:00:00:00:01,dl_dst=00:00:00:00:00:04,actions=output:3
ovs-ofctl add-flow s2 dl_src=00:00:00:00:00:01,dl_dst=00:00:00:00:00:03,actions=output:3

ovs-ofctl add-flow s2 dl_src=00:00:00:00:00:03,dl_dst=00:00:00:00:00:02,actions=output:1
ovs-ofctl add-flow s2 dl_src=00:00:00:00:00:03,dl_dst=00:00:00:00:00:01,actions=output:2

ovs-ofctl add-flow s2 dl_src=00:00:00:00:00:04,dl_dst=00:00:00:00:00:01,actions=output:2
ovs-ofctl add-flow s2 dl_src=00:00:00:00:00:04,dl_dst=00:00:00:00:00:02,actions=output:1

#for switch-s3

ovs-ofctl add-flow s3 dl_type=0x806,nw_proto=1,action=flood
ovs-ofctl add-flow s3 dl_src=00:00:00:00:00:03,dl_dst=00:00:00:00:00:01,actions=output:2
ovs-ofctl add-flow s3 dl_src=00:00:00:00:00:03,dl_dst=00:00:00:00:00:02,actions=output:2
ovs-ofctl add-flow s3 dl_src=00:00:00:00:00:03,dl_dst=00:00:00:00:00:04,actions=output:3

ovs-ofctl add-flow s3 dl_src=00:00:00:00:00:01,dl_dst=00:00:00:00:00:03,actions=output:1
ovs-ofctl add-flow s3 dl_src=00:00:00:00:00:01,dl_dst=00:00:00:00:00:04,actions=output:3

ovs-ofctl add-flow s3 dl_src=00:00:00:00:00:02,dl_dst=00:00:00:00:00:03,actions=output:1
ovs-ofctl add-flow s3 dl_src=00:00:00:00:00:02,dl_dst=00:00:00:00:00:04,actions=output:3

ovs-ofctl add-flow s3 dl_src=00:00:00:00:00:04,dl_dst=00:00:00:00:00:01,actions=output:2
ovs-ofctl add-flow s3 dl_src=00:00:00:00:00:04,dl_dst=00:00:00:00:00:02,actions=output:2
ovs-ofctl add-flow s3 dl_src=00:00:00:00:00:04,dl_dst=00:00:00:00:00:03,actions=output:1

#for switch-s4

ovs-ofctl add-flow s4 dl_type=0x806,nw_proto=1,action=flood
ovs-ofctl add-flow s4 dl_src=00:00:00:00:00:04,dl_dst=00:00:00:00:00:01,actions=output:2
ovs-ofctl add-flow s4 dl_src=00:00:00:00:00:04,dl_dst=00:00:00:00:00:02,actions=output:2
ovs-ofctl add-flow s4 dl_src=00:00:00:00:00:04,dl_dst=00:00:00:00:00:03,actions=output:2

ovs-ofctl add-flow s4 dl_src=00:00:00:00:00:01,dl_dst=00:00:00:00:00:04,actions=output:1,controller
ovs-ofctl add-flow s4 dl_src=00:00:00:00:00:02,dl_dst=00:00:00:00:00:04,actions=output:1
ovs-ofctl add-flow s4 dl_src=00:00:00:00:00:03,dl_dst=00:00:00:00:00:04,actions=output:1
