# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 00:37:39 2022

@author: MD. TASRIF KHAN
"""

from tkinter import *
from tkinter.ttk import *
from time import strftime

root= Tk()
root.title('Clock')

def time():
    string=strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

label=Label(root,font=('ds-digital',80),background='black',foreground='cyan')
label.pack(anchor='center')
time()
mainloop()