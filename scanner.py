#!/bin/python3

import sys
import socket
from datetime import datetime

if len(sys.argv ) == 2:
    target = socket.gethostbyname(sys.argv[1]) #Hostname to IPv4
else:
    print("Invalid amount of arguments.")
    print("Syntax: python3 scanner.py <ip>")

#Display scan
print("-" * 50)
print("Scanning target: " + target)
print("Time started: " + str(datetime.now()))
print("-" * 50)

#Common (useful) ports
commonPorts = [21,22,23,25,53,67,68,69,80,110,139,143,161,443,445]

try:
    for port in commonPorts: # only common ones
    # for port in range(1,65535): (FULL SCAN)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port)) #return an error
        if result == 0:
            print("Port {} is open".format(port))
        s.close()
except KeyboardInterrupt:
    print("\nExiting program.")
    sys.exit()
except socket.gaierror:
    print("Hostname couuld not be resolved.")
    sys.exit()
except socket.error:
    print("Couldn't connet to server.")
    sys.exit()









