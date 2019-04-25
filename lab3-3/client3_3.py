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
import sys


class SendThread(thr.Thread):
    def __init__(self, socket1):
        super().__init__()
        self.socket1 = socket1
        
    def run(self):
        while True:
            msg = input("send-to[{}]: ".format(self.socket1.getpeername())).encode("utf-8")
            self.socket1.send(msg)
                
                
class RecvThread(thr.Thread):
    def __init__(self, socket1):
        super().__init__()
        self.socket1 = socket1
        
    def run(self):
        while True:
            msg = self.socket1.recv(2048).decode("utf-8")
            print("recv-from[{}]: ".format(self.socket1.getpeername()), msg)
            



try:
    
    s = soc.socket(soc.AF_INET,soc.SOCK_STREAM)
    host = "127.0.0.1"
    port = 5500
    
    s.connect((host,port))
    print("Client Started at ",s.getsockname())
    print("Connection with Server:",s.getpeername())
    sendthr = SendThread(s)
    sendthr.start()

    while True:
        msg = s.recv(2048).decode("utf-8")
        print("Server:", msg)
    
except soc.error as e:
    print(e)
    sys.exit(0)
except KeyboardInterrupt:
    print("----------end-----------")
    sys.exit(0)
except:
    print(sys.exc_info())
    
finally:
    s.close()
