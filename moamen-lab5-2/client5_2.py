# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 13:29:34 2019

@author: Moamen Soroor pro
"""

#----------------------------------------
# --------------- UI Part ---------------   
import tkinter as tk

window = tk.Tk()
window.title("Client UI")
window.geometry("500x200")

def btn_clicked():
    # check if connection established 
    if conn== None:
        return
    
    txt = entry.get()
    conn.send(txt.encode("utf-8"))
    
    
entry = tk.Entry(window, width= 50, font= "non 12 bold")
entry.grid(row=1, column=1)

btn = tk.Button(window,text="Send" ,font= "non 12 bold", width=30,height=2,command=btn_clicked)
btn.grid(row=2 , column=1)

lbl = tk.Label(window,text=" " , font= "non 12 bold", width=50,height=2)
lbl.grid(row=3 , column=1)
    
    

#------------------------------------------------
# --------------- Networking Part ---------------  
import socket as soc
import threading as thr
import sys , traceback as trace

class RecvThread(thr.Thread):
    def __init__(self, socket1):
        super().__init__()
        self.socket1 = socket1
        
    def run(self):
        while True:
            msg = self.socket1.recv(2048).decode("utf-8")
            lbl["text"] = msg
   

try:   
    conn = soc.socket(soc.AF_INET,soc.SOCK_STREAM)
    host = "127.0.0.1"
    port = 5500
        
    conn.connect((host,port))
    
    print("Client Started at ",conn.getsockname())
    print("Connection with Server:",conn.getpeername())

    recv = RecvThread(conn)
    recv.start()
    
    # --------------- Run the UI ---------------
    window.mainloop()
    
    
except soc.error as e:
    print(e)
    sys.exit(0)
except KeyboardInterrupt:
    print("----------end-----------")
    sys.exit(0)
except:
    print(trace.print_exc())
finally:
    conn.close()


























