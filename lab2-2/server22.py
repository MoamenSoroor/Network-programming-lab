



# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 12:20:50 2019

@author: Moamen Soroor pro
"""

import socket as soc
import threading as thr
import sys

class SendThread(thr.Thread):
    def __init__(self, socket1):
        thr.Thread.__init__(self)
        self.socket1 = socket1
        
    def run(self):
        while True:
            msg = input("Server: ")
            self.socket1.send(msg.encode("utf-8"))
                
                
class RecvThread(thr.Thread):
    def __init__(self, socket1):
        thr.Thread.__init__(self)
        self.socket1 = socket1
        
    def run(self):
        while True:
            msg = self.socket1.recv(2048).decode("utf-8")
            print("client:", msg)
            


try:
    
    s = soc.socket(soc.AF_INET,soc.SOCK_STREAM)
    s.setsockopt(soc.SOL_SOCKET, soc.SO_REUSEADDR , 1)
    host = "127.0.0.1"
    port = 5500
    
    s.bind((host,port))
    s.listen(6)
    c,add = s.accept()
    print("connection from",add[1] , add[0])
    sendthr = SendThread(c)
    sendthr.start()
    while True:
            msg = c.recv(2048).decode("utf-8")
            print("client:", msg)
    
    
except soc.error as e:
    print(e)
    sys.exit(0)
except KeyboardInterrupt:
    print("end-------------------")
    sys.exit(0)
finally:
    
    s.close()
    c.close()
    


















    
    
