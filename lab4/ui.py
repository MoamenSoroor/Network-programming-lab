# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 12:19:39 2019

@author: moame
"""

import tkinter as tk


window = tk.Tk()
window.title("Tic Tac Tok")
#window.geometry("400x400")
window.configure(background="gray")

turn = 1

def get_turn_XY():
    return "X" if turn == 1 else "Y"

def button_clicked(btn1 , n):
    print("Button {} Clicked".format(n))
    global turn
    if btn1["text"]== " ":
        if turn == 1:
            
            btn1["text"]="X"
            check_win()
            turn = 0
        else:
    
            btn1["text"]="O"
            check_win()
            turn= 1
        
    else:
        print("error")
    
def button1_click():
    print("button1 clicked")
    global turn
    if btn1["text"]== " ":
        if turn == 1:
            
            btn1["text"]="X"
            check_win()
            turn = 0
        else:
    
            btn1["text"]="O"
            check_win()
            turn= 1
        
    else:
        print("error")
        

def button2_click():
    print("button2 clicked")
    global turn
    if btn2["text"]== " ":
        if turn == 1:
            
            btn2["text"]="X"
            check_win()
            turn = 0
        else:
            btn2["text"]="O"
            check_win()
            turn = 1
        
    else:
        print("error")

def button3_click():
    print("button3 clicked")
    global turn
    if btn3["text"]== " ":
        if turn == 1:
            btn3["text"]="X"
            check_win()
            turn = 0
        else:
            btn3["text"]="O"
            check_win()
            turn = 1
    else:
        print("error")

def button4_click():
    print("button4 clicked")
    global turn
    if btn4["text"]== " ":
        if turn == 1:
            
            btn4["text"]="X"
            check_win()
            turn = 0
        else:
            
            btn4["text"]="O"
            check_win()
            turn = 1
    else:
        print("error")
    
def button5_click():
    print("button5 clicked")
    global turn
    if btn5["text"]== " ":
        if turn == 1:
            
            btn5["text"]="X"
            check_win()
            turn = 0
        else:
             
            btn5["text"]="O"
            check_win()
            turn = 1
    else:
        print("error")

def button6_click():
    print("button6 clicked")
    global turn
    if btn6["text"]== " ":
        if turn == 1:
             
            btn6["text"]="X"
            check_win()
            turn = 0
        else:
             
            btn6["text"]="O"
            check_win()
            turn = 1
    else:
        print("error")
    
def button7_click():
    print("button7 clicked")
    global turn
    if btn7["text"]== " ":
        if turn == 1:
             
            btn7["text"]="X"
            check_win()
            turn = 0
        else:
             
            btn7["text"]="O"
            check_win()
            turn = 1
    else:
        print("error")

def button8_click():
    print("button8 clicked")
    global turn
    if btn8["text"]== " ":
        if turn == 1:
             
            btn8["text"]="X"
            check_win()
            turn = 0
        else:
             
            btn8["text"]="O"
            check_win()
            turn = 1
    else:
        print("error")
    
def button9_click():
    print("button9 clicked")
    global turn
    if btn9["text"]== " ":
        if turn == 1:
             
            btn9["text"]="X"
            check_win()
            turn = 0
        else:
             
            btn9["text"]="O"
            check_win()
            turn = 1
    else:
        print("error")
        
def check_win():
    player = get_turn_XY()
    if btn1["text"] == btn2["text"] ==btn3["text"]== player or\
    btn4["text"] == btn5["text"] ==btn6["text"]==player or\
    btn7["text"] == btn8["text"] ==btn9["text"]==player or\
    btn1["text"] == btn4["text"] ==btn7["text"]==player or\
    btn2["text"] == btn5["text"] ==btn8["text"]==player or\
    btn3["text"] == btn6["text"] ==btn9["text"]==player or\
    btn1["text"] == btn5["text"] ==btn9["text"]==player or\
    btn3["text"] == btn5["text"] ==btn7["text"]==player:
        print("PLAYER {} Win !!".format(player))
        label3["text"] = "PLAYER {} Win !!".format(player)
        
    

label1 = tk.Label(window,text="Player1:X ",width=10,bg="yellow",font="non 18 bold" , fg="black")
label1.grid(row=0, column=0)
label2 = tk.Label(window,text="player2:O ",width=10,bg="yellow",font="non 18 bold" , fg="black")
label2.grid(row=1, column=0)
label3 = tk.Label(window,text=" ",width=10,bg="Green",font="non 18 bold" , fg="White")
label3.grid(row=2, column=0)

btn1 = tk.Button(window,text=" ",width=10,bg="yellow",font="non 18 bold" , fg="black",command=button1_click)
btn1.grid(row=0, column=1)
btn2 = tk.Button(window,text=" ",width=10,bg="yellow" ,font="non 18 bold", fg="black",command=button2_click)
btn2.grid(row=0, column=2)
btn3 = tk.Button(window,text=" ",width=10,bg="yellow" ,font="non 18 bold", fg="black",command=button3_click)
btn3.grid(row=0, column=3)
btn4 = tk.Button(window,text=" ",width=10,bg="yellow" ,font="non 18 bold", fg="black",command=button4_click)
btn4.grid(row=1, column=1)
btn5 = tk.Button(window,text=" ",width=10,bg="yellow" ,font="non 18 bold", fg="black",command=button5_click)
btn5.grid(row=1, column=2)
btn6 = tk.Button(window,text=" ",width=10,bg="yellow" ,font="non 18 bold", fg="black",command=button6_click)
btn6.grid(row=1, column=3)
btn7 = tk.Button(window,text=" ",width=10,bg="yellow" ,font="non 18 bold", fg="black",command=button7_click)
btn7.grid(row=2, column=1)
btn8 = tk.Button(window,text=" ",width=10,bg="yellow" ,font="non 18 bold", fg="black",command=button8_click)
btn8.grid(row=2, column=2)
btn9 = tk.Button(window,text=" ",width=10,bg="yellow" ,font="non 18 bold", fg="black",command=button9_click)
btn9.grid(row=2, column=3)




window.mainloop()
