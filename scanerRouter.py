 #!/usr/bin/python2.7.14
 #the first import scapy moduls
from scapy.all import *
from scapy.layers.l2 import Ether, ARP
#create a loop for testing every ip in localhost
for subnetId in range(1,255):
	for hostId in range(1,255):
		ip="192.168."+str(subnetId) + "." +str(hostId)
		arpRequest=Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip,hwdst="ff:ff:ff:ff:ff:ff")
		arpResponse = srp1(arpRequest,timeout=1,verbose=0)
		if arpResponse:
			print "IP >> " + arpResponse.psrc + " MAC >> " + arpResponse.hwsrc
#___________________________________________________________________________________________