#!/usr/bin/env python

import  scapy.all as scapy 
import optparse

def get_arguments():
    #parser object 
    parser= optparse.OptionParser()
    #options to the object 
    parser.add_option("-t", "--target", dest="target", help="To Specify the Ip range you want to scan in")
    #handle the arguments user enters
    (options, arguments)=parser.parse_args()
    if not options.target:
        #code to handle the error
        parser.error("[-] Please specify an ip use --help for more info ")
    return options



def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    #print(arp_request.summary())
    broadcast= scapy.Ether(dst="ff:ff:ff:ff:ff:ff") #This creates a ethernet frame/object
    #print(broadcast.summary())
    arp_request_broadcast= broadcast/arp_request
    #arp_request_broadcast.show()#to show options in the class
    answered_list =scapy.srp(arp_request_broadcast, timeout=1,verbose=False)[0]
    #print(answered_list.summary())
    #print(unanswered_list.summary())



    clients_list=[]
    for element in answered_list:
        clients_dict={"ip":element[1].psrc,"mac":element[1].hwsrc}
        clients_list.append(clients_dict)
        #print(element[1].psrc+"\t\t"+element[1].hwsrc)
     #print(clients_list) #this shows the list on the screen     
    return clients_list



def print_result(results_list):
    print("IP\t\t\tMAC ADDRESS\n------------------------------------")
    for client in results_list:
        print(client["ip"]+"\t\t"+client["mac"])



options=get_arguments()
scan_result=scan(options.target)
print_result(scan_result)