#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 14:59:57 2022

@author: mitpatel
"""

import socket
import sys


class Client:
    
    def __init__(self, hostIP):
        self.serverAddress = hostIP
        #Register any port from 1024 to 49151
        self.portNumber = 49151
        #receive a packet into buffer memory
        self.bufferSize = 1024
        
    def sendData(self,data):
        bytesToSend = str.encode(data)
        # Create a UDP socket at client side
        
        UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        try:
            UDPClientSocket.settimeout(5.0)
            
            UDPClientSocket.sendto(bytesToSend, (self.serverAddress,self.portNumber))
            
            msgFromServer = UDPClientSocket.recvfrom(self.bufferSize)[0]
            print("Message from Server " +(msgFromServer).decode('utf-8'))
            
        except:
            print("error: Server is not started")
        
        
        
 