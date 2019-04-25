# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 13:29:34 2019

@author: Moamen Soroor pro
"""

import socket as soc
import sys , traceback as trace

try:   
    s = soc.socket(soc.AF_INET,soc.SOCK_STREAM)
    host = "127.0.0.1"
    port = 5500
        
    s.connect((host,port))
    
    print("Client Started at ",s.getsockname())
    print("Connection with Server:",s.getpeername())
    
    while True:
        s.send(input("Client: ").encode("utf-8"))
        data = s.recv(2048)
        print("Server:", data.decode("utf-8") )
except soc.error as e:
    print(e)
    sys.exit(0)
except KeyboardInterrupt:
    print("----------end-----------")
    sys.exit(0)
except:
    print(trace.print_exc())
finally:
    s.close()


























