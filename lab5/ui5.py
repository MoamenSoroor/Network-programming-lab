# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 10:57:06 2019

@author: moame
"""
import tkinter as tk
import tkinter.messagebox as msgbox
window = tk.Tk()
window.title("simle ui")
window.geometry("400x400")


#window.configure(background="gray")
def btn_clicked():
    txt = entry.get()
    print("Entry:{}".format(txt))
    lbl["text"] = txt
    msgbox.showinfo("Entry data",txt)
    
    
entry = tk.Entry(window, width= 100)
entry.grid(row=1, column=1)

btn = tk.Button(window,text="print" , width=50,height=2,command=btn_clicked)
btn.grid(row=2 , column=1)

lbl = tk.Label(window,text=" " , width=50,height=2)
lbl.grid(row=3 , column=1)




window.mainloop()