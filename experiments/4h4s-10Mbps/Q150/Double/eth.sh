#!/bin/bash

ethtool -K h1-eth0 gro off
ethtool -K h1-eth0 gso off
ethtool -K h1-eth0 tso off


ethtool -K h2-eth0 gro off
ethtool -K h2-eth0 gso off
ethtool -K h2-eth0 tso off


ethtool -K h3-eth0 gro off
ethtool -K h3-eth0 gso off
ethtool -K h3-eth0 tso off

ethtool -K h4-eth0 gro off
ethtool -K h4-eth0 gso off
ethtool -K h4-eth0 tso off


ethtool -K s1-eth1 gro off
ethtool -K s1-eth1 gso off
ethtool -K s1-eth1 tso off
ethtool -K s1-eth2 gro off
ethtool -K s1-eth2 gso off
ethtool -K s1-eth2 tso off
ethtool -K s1-eth3 gro off
ethtool -K s1-eth3 gso off
ethtool -K s1-eth3 tso off

ethtool -K s2-eth1 gro off
ethtool -K s2-eth1 gso off
ethtool -K s2-eth1 tso off
ethtool -K s2-eth2 gro off
ethtool -K s2-eth2 gso off
ethtool -K s2-eth2 tso off
ethtool -K s2-eth3 gro off
ethtool -K s2-eth3 gso off
ethtool -K s2-eth3 tso off



ethtool -K s3-eth1 gro off
ethtool -K s3-eth1 gso off
ethtool -K s3-eth1 tso off
ethtool -K s3-eth2 gro off
ethtool -K s3-eth2 gso off
ethtool -K s3-eth2 tso off
ethtool -K s3-eth3 gro off
ethtool -K s3-eth3 gso off
ethtool -K s3-eth3 tso off


ethtool -K s4-eth1 gro off
ethtool -K s4-eth1 gso off
ethtool -K s4-eth1 tso off
ethtool -K s4-eth2 gro off
ethtool -K s4-eth2 gso off
ethtool -K s4-eth2 tso off
ethtool -K s4-eth3 gro off
ethtool -K s4-eth3 gso off
ethtool -K s4-eth3 tso off

