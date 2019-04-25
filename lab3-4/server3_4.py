# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 12:20:50 2019

@author: Moamen Soroor
"""

import socket as soc
import threading as thr
import sys,traceback as trace

    
class SendThread(thr.Thread):
    def __init__(self, socket1):
        super().__init__()
        self.socket1 = socket1
        self.clients = []
    
    def run(self):
        while True:
            self.show_clients()
            client_id = int(input("Select Client: "))
            if 0 < client_id <= len(self.clients):
                client_soc,add = self.clients[client_id - 1]
                prompt = "send-to[{0}]: ".format(add)
                msg = input(prompt).encode("utf-8")
                client_soc.send(msg) 
        
    def add_client(self, client):
        self.clients.append(client)
        
    def find_client(self, client_id):
        if 0 < client_id - 1 < len(self.clients):
            return self.clients[client_id - 1]
        else:
            return (-1,-1)
        
    def show_clients(self):
        print("=" * 40)
        print("{:>7s}{:>15s}{:>10s}".format( "ID", "HostAddr","Port"))
        counter = 0
        for client_soc , client in self.clients:
            counter += 1
            print("{0:>7d}{c[0]:>15s}{c[1]:>10d}".format(counter,c=client))
        print("=" * 40)
        
       

        
                
                
class RecvThread(thr.Thread):
    def __init__(self, socket1):
        super().__init__()
        self.socket1 = socket1
        
    def run(self):
        while True:
            msg = self.socket1.recv(2048).decode("utf-8")
            prompt = "recv-from[{0}]:".format(self.socket1.getpeername())
            print(prompt, msg)
            


try:
    
    s = soc.socket(soc.AF_INET,soc.SOCK_STREAM)
    s.setsockopt(soc.SOL_SOCKET, soc.SO_REUSEADDR , 1)
    host = "127.0.0.1"
    port = 5500
    
    s.bind((host,port))
    
    s.listen(10)
    print("Server now can listen at {}".format(s.getsockname()))
    sendthr = SendThread(s)
    sendthr.start()
    
    while True:
        conn,add = s.accept()
        print("Server is listening to new Client:",add)
        recvthr = RecvThread(conn)
        recvthr.start()
        sendthr.add_client((conn,add))
        sendthr.show_clients()
    
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
    


















    
    
