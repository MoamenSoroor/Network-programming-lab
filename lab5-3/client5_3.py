# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 13:29:34 2019

@author: Moamen Soroor pro
"""

#------------------------------------------------
# --------------- Networking Part ---------------
import socket as soc
import threading as thr
import sys , traceback as trace

# make connection socket global
conn_soc = None

# make function for socket code to call it in thread
def socket_thread():
    try:
        
        global conn_soc
        conn_soc = soc.socket(soc.AF_INET,soc.SOCK_STREAM)
        host = "127.0.0.1"
        port = 5500
            
        conn_soc.connect((host,port))
        
        print("Client Started at ",conn_soc.getsockname())
        print("Connection with Server:",conn_soc.getpeername())
        
        # Receive code
        while True:
            # ------------------ blocking function --------------------
            msg = conn_soc.recv(2048).decode("utf-8")
            # global ui label
            label["text"] = msg
    
    except soc.error:
        print(trace.print_exc())
        sys.exit(0)
    except KeyboardInterrupt:
        print("----------end-----------")
        sys.exit(0)
    except:
        print(trace.print_exc())
        sys.exit(0)


# close sockets       
def close_conn():
    conn_soc.close()
    
#----------------------------------------
# --------------- UI Part ---------------
import tkinter as tk

# make all needed ui elements in socket global
label = None

# make user interface function that return window
def user_Intrface():
    
    window = tk.Tk()
    window.title("Client UI")
    window.geometry("500x200")
    
    def btn_clicked():
        # global conn_soc
        # check if connection established 
        if conn_soc == None:
            return
        
        txt = entry.get()
        conn_soc.send(txt.encode("utf-8"))
        
        
    entry = tk.Entry(window, width= 50, font= "non 12 bold")
    entry.grid(row=1, column=1)
    
    btn = tk.Button(window,text="Send" ,font= "non 12 bold", width=30,height=2,command=btn_clicked)
    btn.grid(row=2 , column=1)
    
    global label
    label = tk.Label(window,text=" " , font= "non 12 bold", width=50,height=2)
    label.grid(row=3 , column=1)
    
    return window




# main     
def main():
    # --------------- Run the UI ---------------
    window = user_Intrface()
    
    soc_thr = thr.Thread(target=socket_thread)
    soc_thr.start()
    
    window.mainloop()
    
if __name__ == "__main__":
    main()

























