#!/bin/bash

#Copyright (C) 2014  Harry Sharrock harry@hackapi.org
#               	 @harrysharrock twitter.com
#	This program is free software: you can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation, either version 3 of the License, or
#	(at your option) any later version.
#
#	This program is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details.
#
#	You should have received a copy of the GNU General Public License
#	along with this program.  If not, see <http://www.gnu.org/licenses/>.

echo .Killing Airbase-ng..
pkill airbase-ng
sleep 2;
echo .Killing DHCP..
pkill dhcpd3
sleep 5;

echo .Putting Wlan In Monitor Mode..
airmon-ng stop wlan1 # Change to your wlan interface.
sleep 5
airmon-ng start wlan1 # Change to your wlan interface.
sleep 5;
echo .Starting Fake AP..
airbase-ng -e Test -c 11 -v wlan1 &amp; # Change essid, channel and interface.
sleep 5;

ifconfig ath0 up
ifconfig ath0 172.16.42.42 netmask 255.255.255.0 # Change IP addresses as configured in your dhcpd.conf
route add -net 172.16.42.0 netmask 255.255.255.0 gw 172.16.42.1

sleep 5;

iptables .flush					#From line 25 - 29 setting up iptabels.
iptables .table nat .flush
iptables .delete-chain
iptables .table nat .delete-chain
iptables -P FORWARD ACCEPT

echo &gt; ./var/lib/dhcp3/dhcpd.leases.
ln -s /var/run/dhcp3-server/dhcpd.pid /var/run/dhcpd.pid
dhcpd3 -d -f -cf /etc/dhcp3/dhcpd.conf at0 &amp;

sleep 5;
echo .1. &gt; /proc/sys/net/ipv4/ip_forward
echo dhcp and wireless AP setup was successful :)