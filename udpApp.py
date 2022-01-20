#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 14:54:51 2022

@author: mitpatel
"""

import sys
from ClientClass import Client
from ServerClass import Server
if (sys.argv[1].lower()=='client'):
    Client(sys.argv[2]).sendData(sys.argv[3])
else:
    Server().demon()


    