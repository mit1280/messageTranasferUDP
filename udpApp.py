#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 14:54:51 2022

@author: mitpatel
"""
import re
import sys
import socket
from ClientClass import Client
from ServerClass import Server
try:
    if (sys.argv[1].lower()=='client'):
        if not re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",sys.argv[2]):
            raise socket.error()
        socket.inet_aton(sys.argv[2])
        Client(sys.argv[2]).sendData(sys.argv[3])
    elif (sys.argv[1].lower()=='server'):
        Server().demon()
    else:
        raise IndexError()
except IndexError:
    print("Please add correct arugments")
except socket.error:
    print("Please enter valid IP address")
  