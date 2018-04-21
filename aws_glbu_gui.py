#!/usr/bin/env python3
import sys
import os
from tkinter import *

def launch_glbu():
   print("Sending archive %s to AWS Glacier..." % (e1.get()))
   os.system('aws glacier upload-archive --account-id - --vault-name examplevault --body '+(e1.get()))

master = Tk()
Label(master, font=("helvetica", "14", "bold"), text="Input Archive Name").grid(row=0)

e1 = Entry(master)

e1.grid(row=0, column=1)

Button(master, text='Quit', fg="red", bd="5", font=("helvetica", "14", "bold"), activebackground="orange", command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Send Archive',fg="green", bd="5", font=("helvetica", "14", "bold"), activebackground="orange", command=launch_glbu).grid(row=3, column=1, sticky=W, pady=4)

master.title("AWS Glacier Backup GUI")
master.geometry("400x150+250+225")
mainloop( )
