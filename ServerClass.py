#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 14:59:43 2022

@author: mitpatel
"""

import socket
import signal
import sys
import platform


class Server:
    
    def __init__(self):
        self.localIP     = "0.0.0.0"
        self.localPort   = 49151
        self.bufferSize  = 1024
        
    def signal_handler(self,sig, frame):
        sys.exit(0)
        
    def demon(self):
        signal.signal(signal.SIGINT, self.signal_handler)
        if platform.system() == 'Windows':
            signal.signal(signal.SIGBREAK, self.signal_handler)
        # Create a datagram socket
        
        UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        # Bind to address and ip
        UDPServerSocket.bind((self.localIP, self.localPort))
        print("UDP server up and listening")
        # Listen for incoming datagrams
        while(True):
            try:
                bytesAddressPair = UDPServerSocket.recvfrom(self.bufferSize)
                address = bytesAddressPair[1]
                #Below line will throw an exception if message isn't Interger
                message = float(bytesAddressPair[0])
                print(message)
                UDPServerSocket.sendto(str.encode(str(2*message)), address)
            #this exception is for when server don't have address e.g. no communication between client/sever
            except NameError:
                pass
            #this exception is for message value 
            except ValueError:
                print("error: input must be a number")
                UDPServerSocket.sendto(str.encode("error: input must be a number"), address)
                UDPServerSocket.close()
                UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
                # Bind to address and ip
                UDPServerSocket.bind((self.localIP, self.localPort))
                print("UDP server Restarted and listening")


