# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 13:29:34 2019

@author: Moamen Soroor pro
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 12:20:50 2019

@author: Moamen Soroor pro
"""

import socket as soc
s = soc.socket(soc.AF_INET,soc.SOCK_STREAM)
host = "127.0.0.1"
port = 5500

s.connect((host,port))
s.send(b"Hello World")
s.close()
print("client ended")
    
    
