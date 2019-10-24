#!/bin/bash
ping -q -w 1 -c 1 `ip r | grep default | cut -d ' ' -f 3` > /dev/null 
if [ $? -eq 0 ]; then
   #sudo systemctl stop hostapd.service
   #sudo systemctl stop dnsmasq.service
   sudo iptables --flush
   sudo sysctl net.ipv4.ip_forward=0
else
   systemctl start hostapd
   sleep 1
   sysctl net.ipv4.ip_forward=1
   iptables --flush
   iptables -t nat --flush
   iptables -t nat -A PREROUTING -i br0 -p udp -m udp --dport 53 -j DNAT --to-destination 10.1.1.1:53
   iptables -t nat -A PREROUTING -i br0 -p tcp -m tcp --dport 80 -j DNAT --to-destination 10.1.1.1:3000
   iptables -t nat -A PREROUTING -i br0 -p tcp -m tcp --dport 443 -j DNAT --to-destination 10.1.1.1:3000
   iptables -t nat -A POSTROUTING -j MASQUERADE
   python /home/pi/network_auth/app.py
   #service dnsmasq start
fi