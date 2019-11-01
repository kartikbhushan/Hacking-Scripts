#!/usr/bin/env python

import subprocess #subprocess allows to run code in termianl
import optparse 
import re

def get_arguments():
    #parser object 
    parser= optparse.OptionParser()

    #options to the object 
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC Address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New  MAC Address")

    #handle the arguments user enters
    (options, arguments)=parser.parse_args()
    if not options.interface:
        #code to handle the error
        parser.error("[-] Please specify an interface use --help for more info ")
    elif not options.new_mac:
        #code to handle the error 
        parser.error("[-] Please specify a MAC Address use --help for more info ")
    return options

def change_mac(interface,new_mac):
    print("[+]Changing MAC Address for " + interface + " to " +new_mac)
    
    #subprocess.call("ifconfig" + interface + "down ",shell=True)
    #subprocess.call("ifconfig" + interface + "hw ether" + new_mac",shell=True)
    #subprocess.call("ifconfig" + interface + "up ",shell=True)
    #this way we can hijack the code beacause interface is a variable where we can input anything
    #example=interface = wlan0;ls;
    #this will execute ls along with ifconfig wlan0 down 

    #much secure method is using list in the call function
    #here we input " ifconfig wlan0 down " as ["ifconfig", interface, "down"]
    #this is a list and u cant bypass commands in this 
    subprocess.call(["ifconfig", interface ,"down"])
    subprocess.call(["ifconfig", interface ,"hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface ,"up"])


def get_current_mac(interface):
    ifconfig_result=subprocess.check_output(["ifconfig", options.interface])

    mac_address_search_result=re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconfig_result)

    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read MAC Address.")

#variables
#one way of taking input without parsing 
#interface =input("Interface >")
#new_mac=input("New MAC >")


#input into the variables using parsing 
#interface= options.interface
#new_mac= options.new_mac


#calling the function change_mac() and get_arguments()
options=get_arguments()
current_mac=get_current_mac(options.interface)
print("Current MAC =" + str(current_mac))
change_mac(options.interface,options.new_mac) 
current_mac=get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("[+] MAC Address was Successfully changed to " + current_mac)
else:
    print("[-] MAC Address couldnt be changed ")

