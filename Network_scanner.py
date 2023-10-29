#!/usr/bin/env python

import scapy.all as scapy
import argparse

def get_arguments():
	parser = argparse.ArgumentParser()
	parser.add_argument("-t", "--target", dest="target", help="Target IP / IP range.")
	options = parser.parse_args()
	return options

def scan(ip):
	arp_reqest = scapy.ARP(pdst=ip)
	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	arp_reqest_broadcast = broadcast/arp_reqest
	answered_list = scapy.srp(arp_reqest_broadcast, timeout=1, verbose=False)[0]
	
	clients_list = []
	for element in answered_list:
	    client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
	    clients_list.append(client_dict)
	return client_list

def print_result(result_list):
	print("IP\t\t\tMAC Address\n -------------------------------------")
	for client in results_list:
	     print(client["ip"] + "\t\t" + client["mac"])

options = get_arguments()
scan_result = scan(options.target)
print_result(scan_result)
