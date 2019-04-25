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
import threading as thr
class SendThread(thr.Thread):
    def __init__(self, socket1):
        thr.Thread.__init__(self)
        self.socket1 = socket1
        
    def run(self):
        while True:
            msg = input("Client: ")
            self.socket1.send(msg.encode("utf-8"))
                
                
class RecvThread(thr.Thread):
    def __init__(self, socket1):
        thr.Thread.__init__(self)
        self.socket1 = socket1
        
    def run(self):
        msg = self.socket1.recv(2048).decode("utf-8")
        print("Server:", msg)

try:
    
    s = soc.socket(soc.AF_INET,soc.SOCK_STREAM)
    host = "127.0.0.1"
    port = 5500
    
    s.connect((host,port))
    
    sendthr = SendThread(s)
    sendthr.start()
        
    while True:
        msg = s.recv(2048).decode("utf-8")
        print("Server:", msg)
    
except soc.error as e:
    print(e)
except KeyboardInterrupt:
    print("end-------------------")
finally:
    s.close()
