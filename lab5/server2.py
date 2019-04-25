# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 12:20:50 2019

@author: Moamen Soroor pro
"""

import socket as soc
import sys , traceback as trace
import threading as thr

class RecvThread(thr.Thread):
    def __init__(self, socket1,lbl):
        super().__init__()
        self.socket1 = socket1
        
    def run(self):
        while True:
            msg = self.socket1.recv(2048).decode("utf-8")
            lbl["text"] = msg   
    
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
    import tkinter as tk
    import tkinter.messagebox as msgbox
    window = tk.Tk()
    window.title("server ui")
    window.geometry("400x400")
    
    
    #window.configure(background="gray")
    def btn_clicked():
        txt = entry.get()
        conn.send(txt.encode("utf-8"))
        
        
    entry = tk.Entry(window, width= 100)
    entry.grid(row=1, column=1)
    
    btn = tk.Button(window,text="print" , width=50,height=2,command=btn_clicked)
    btn.grid(row=2 , column=1)
    
    lbl = tk.Label(window,text=" " , width=50,height=2)
    lbl.grid(row=3 , column=1)
    
    
    
    recv = RecvThread(conn , lbl)
    recv.start()
    window.mainloop()
        
except soc.error as e:
    print(e)
except KeyboardInterrupt:
    print("end-------------------")
finally:
    s.close()
    
    
