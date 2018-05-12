from tkinter import *
import os

class bcolors:
    fail = '\033[91m'
    warn = '\033[93m'

def send_aws_bu():
  os.system('clear')
  if e1.get()=="":
    print (bcolors.fail +"\nNo input detected.  Please input a valid path and file name.")
     
  else:
    os.system('printf "\033[0m"')
    os.system('clear')
    print("\nUploading archive %s to AWS Glacier..." % (e1.get()))
    #os.system('aws glacier upload-archive --account-id - --vault-name my-vault --body ' +(e1.get)())
    print(bcolors.warn +"\nFunction to upload is not enabled.  \nPlease enable the function in order to upload archive to Glacier.")
	#print("Pinging... %s" % (e1.get()))
	#os.system('ping '+(e1.get)()) #Could configure this to do other tasks

def masterquit():
  os.system('clear')
  os.system('printf "\033[0m"')
  quit()

master = Tk()
Label(master, text="Please input the archive name: ", bd="6", font=("helvetica", "12", "bold")).grid(row=0)

e1 = Entry(master)

e1.grid(row=0, column=1)

Button(master, text='QUIT', fg="red", bd="6", font=("helvetica", "14", "bold"),activebackground="orange", width="20", relief="raised", command=masterquit).grid(row=3, column=0, sticky=W, pady=4, padx=4)
Button(master, text='Upload Archive', fg="green", bd="6", font=("helvetica", "14", "bold"),activebackground="orange", width="20", relief="raised", command=send_aws_bu).grid(row=3, column=1, sticky=W, pady=4, padx=4)

master.title("AWS Glacier Backup GUI")
master.geometry("530x150+250+225")
mainloop( )
