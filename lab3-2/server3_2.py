# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 12:20:50 2019

@author: Moamen Soroor pro
"""

import socket as soc
import threading as thr
import sys,traceback as trace


lock = thr.Lock()
def get_input(text):
    lock.acquire()
    msg = input(text)
    lock.release()
    return msg


class SendThread(thr.Thread):

    def __init__(self, socket1):
        super().__init__()
        self.socket1 = socket1
        
    def run(self):
        while True:
            # use safe input function
            msg = get_input("send-to[{}]: ".format(self.socket1.getpeername())).encode("utf-8")
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
    s.setsockopt(soc.SOL_SOCKET, soc.SO_REUSEADDR , 1)
    host = "127.0.0.1"
    port = 5500
    
    s.bind((host,port))
    
    s.listen(10)
    print("Server now can listen at {}".format(s.getsockname()))
    while True:
        conn,add = s.accept()
        print("Server Listen to ",add)
        sendthr = SendThread(conn)
        sendthr.start()
        recvthr = RecvThread(conn)
        recvthr.start()
    
    print("Server Closed Correctly".center(50,"="))
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
    


















    
    
