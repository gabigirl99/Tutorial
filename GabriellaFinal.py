#=====================#
#                 Yahtzee                   #
#       By:Shawn McCausland     #
#                   130025                  #
#=====================#
import sys
import os
import Tkinter
import random
from Tkinter import *
import tkMessageBox

#==== Main Window ====#
root=Tk()
root.bg='#ffffff'
root.title('Yahtzee')
root.geometry('1000x600+400+20')
#===== Load Images =====#
roll_1=PhotoImage(file='images/1.gif')
roll_2=PhotoImage(file='images/2.gif')
roll_3=PhotoImage(file='images/3.gif')
roll_4=PhotoImage(file='images/4.gif')
roll_5=PhotoImage(file='images/5.gif')
roll_6=PhotoImage(file='images/6.gif')
select1=PhotoImage(file='images/1y.gif')
select2=PhotoImage(file='images/2y.gif')
select3=PhotoImage(file='images/3y.gif')
select4=PhotoImage(file='images/4y.gif')
select5=PhotoImage(file='images/5y.gif')
select6=PhotoImage(file='images/6y.gif')
reroll=PhotoImage(file='images/roll.gif')
nonselected=[roll_1,roll_2,roll_3,roll_4,roll_5,roll_6]
clicked=[select1, select2, select3, select4, select5, select6]
All=[roll_1,roll_2,roll_3,roll_4,roll_5,roll_6]
#========equal============#
no1=1
no2=2
no3=3
no4=4
no5=5
no6=6

#==== Functions =====#

def roll_all(0,6):
    button1.config(image= All[random.randrange(0,6)])
    button2.config(image= All[random.randrange(0,6)])
    button3.config(image= All[random.randrange(0,6)])
    button4.config(image= All[random.randrange(0,6)])
    button5.config(image= All[random.randrange(0,6)])
    button6.config(image= All[random.randrange(0,6)])
def select(x):
    if x==1:
       if no1==1:
            if orignal_1==1:
               button1.config(image=select1,command=lambda:select(1))
            if orignal_1==2:
               button1.config(image=select2,command=lambda:select(2))
            if orignal_1==3:
               button1.config(image=select3,command=lambda:select(3))
            if orignal_1==4:
               button1.config(image=select4,command=lambda:select(4))
            if orignal_1==5:
               button1.config(image=select5,command=lambda:select(5))
            if orignal_1==6:
               button1.config(image=select6,command=lambda:select(6))
    else:
        pass
            
            
                
            
            
    if x==2:
        button2.config(image=clicked[random.randrange(0,6)])
    if x==3:
        button3.config(image=clicked[random.randrange(0,6)])
    if x==4:
        button4.config(image=clicked[random.randrange(0,6)])
    if x==5:
        button5.config(image=clicked[random.randrange(0,6)])
    if x==6:
        button6.config(image=clicked[random.randrange(0,66)])
  
#=== Makes Buttons ===#
button1=Button(image=All[random.randrange(0,5)],command=lambda:select(1))
if button1== Button(image=roll_1,command=lambda:select(1)):
    orignal_1=1
if button1== Button(image=roll_2,command=lambda:select(1)):
    orignal_1=2
if button1== Button(image=roll_3,command=lambda:select(1)):
    orignal_1=3
if button1== Button(image=roll_4,command=lambda:select(1)):
    orignal_1=4
if button1== Button(image=roll_5,command=lambda:select(1)):
    orignal_1=5
if button1== Button(image=roll_6,command=lambda:select(1)):
    orignal_1=6
button1=Button(image=All[random.randrange(0,6)],command=lambda:select(1))
button1.grid(row=1,column=1)
button2=Button(image=All[random.randrange(0,6)],command=lambda:select(2))
button2.grid(row=1,column=2)
button3=Button(image=All[random.randrange(0,6)],command=lambda:select(3))
button3.grid(row=1,column=3)
button4=Button(image=All[random.randrange(0,6)],command=lambda:select(4))
button4.grid(row=1,column=4)
button5=Button(image=All[random.randrange(0,6)],command=lambda:select(5))
button5.grid(row=1,column=5)
reroll=Button(text='reroll',command=roll_all)
reroll.grid(row=2,column=1)




root.mainloop()
