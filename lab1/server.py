# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 12:20:50 2019

@author: Moamen Soroor pro
"""

import socket as soc
s = soc.socket(soc.AF_INET,soc.SOCK_STREAM)
host = "127.0.0.1"
port = 5500

s.bind((host,port))
s.listen(6)

while True:
    c,add = s.accept()
    print("connection from",add[1])
    m = c.recv(1024)
    print(m)
    c.close()
    
    
    
