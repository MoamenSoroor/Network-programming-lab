# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 12:20:50 2019

@author: Moamen Soroor pro
"""

import socket as soc
try:
    
    s = soc.socket(soc.AF_INET,soc.SOCK_STREAM)
    s.setsockopt(soc.SOL_SOCKET, soc.SO_REUSEADDR , 1)
    
    host = "127.0.0.1"
    port = 5500
    
    s.bind((host,port))
    
    s.listen(6)
    print("Server now can listen at {}".format(s.getsockname()))
    
    # establish a connection
    # it return connection socket and tuple with (host address, port)
    conn,add = s.accept()
    print("Server Listen to ",add)
    #print("Server Listen to ",c.getpeername())
    
    while True:
        msg = conn.recv(2048)
        print("client:", msg.decode("utf-8"))
        conn.send(input("Server: ").encode("utf-8"))
        
except soc.error as e:
    print(e)
except KeyboardInterrupt:
    print("end-------------------")
finally:
    s.close()
    
    
