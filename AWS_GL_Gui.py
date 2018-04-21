#!/usr/bin/env python3
import tkinter as tk
import sys
import os

class Application(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.pack()
		self.create_widgets()
		
	def create_widgets(self):
		self.aws_gl = tk.Button(self, fg="green", bg="lightgrey", bd="5", padx="15", pady="12", relief="raised", font=("helvetica", "16", "bold"),activebackground="orange", width="20")
		self.aws_gl["text"] = "Launch AWS Glacier BU"
		self.aws_gl["command"] = self.aws_bu
		self.aws_gl.pack(side="top")
		
		self.aws_gl = tk.Button(self, fg="darkgrey", bg="lightgrey", bd="5", padx="15", pady="12", relief="raised", font=("helvetica", "16", "bold"), activebackground="orange", width="20")
		self.aws_gl["text"] = "Nothing button"
		self.aws_gl["command"] = self.aws_nothing
		self.aws_gl.pack(side="top")
		
		self.quit = tk.Button(self, text="QUIT", fg="red", bg="lightgrey", bd="5",padx="15", pady="12", relief="raised", font=("helvetica", "16", "bold"), activebackground="orange", width="20", command=root.destroy)
		self.quit.pack(side="bottom")
		
	def aws_bu(self):
		print("\nEventually, this could be used to launch an automated AWS Glacier backup!")
		print("\nHere is the the version of the AWS CLI you are currently running: ")
		os.system('aws --version')
		#os.system('aws glacier list-vaults') NOTE - will need to add the --account-id in order for the command to function
		
	def aws_nothing(self):
		print("\nThis button doesn't do anyting useful for the moment, but could be configured to do so...")
		
		
root = tk.Tk()
root.title("AWS Glacier Backup GUI")
root.geometry("400x275+250+225")
root.configure(background="#D6D6D6")
#root.iconbitmap(r'Z:\PSS\TUP.ico') 
app = Application(master=root)
app.mainloop()
