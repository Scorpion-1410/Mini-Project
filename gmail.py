# Import Statements
import pywhatkit
from tkinter import *
from tkinter.ttk import *

# Global Variable is Declared and Initialize as None
sender_mail = None
sender_pass = None
receiver_mail = None
message = None
gmail_screen = None
main_screen = None


# Function for User Interface for Gmail Screen
def user_interface():
    # Global variable Assigned Datatype
    global main_screen
    global gmail_screen
    global sender_mail
    global sender_pass
    global receiver_mail
    global message

    sender_mail = StringVar()
    sender_pass = StringVar()
    receiver_mail = StringVar()
    message = StringVar()

    # New Gmail Screen is Created
    gmail_screen = Toplevel(main_screen)
    gmail_screen.title("Gmail")

    # Sender Mail Label & Box
    q = Label(gmail_screen, text="Sender Mail", width=15)
    q.grid(row=0, column=0)
    q.configure(background="black", foreground="white")
    Entry(gmail_screen, textvariable=sender_mail, width=10).grid(row=0, column=2)
    Label(gmail_screen, text="", width=20).grid(row=1, column=0)

    # Sender Password Label & Box
    w = Label(gmail_screen, text="Sender Password", width=15)
    w.grid(row=2, column=0)
    w.configure(background="black", foreground="white")
    Entry(gmail_screen, textvariable=sender_pass, show="*", width=10).grid(row=2, column=2)
    Label(gmail_screen, text="", width=20).grid(row=3, column=0)

    # Receiver Mail Label & Box
    e = Label(gmail_screen, text="Receiver Mail", width=15)
    e.grid(row=4, column=0)
    e.configure(background="black", foreground="white")
    Entry(gmail_screen, textvariable=receiver_mail, width=10).grid(row=4, column=2)
    Label(gmail_screen, text="", width=20).grid(row=5, column=0)

    # Message Label & Box
    r = Label(gmail_screen, text="Message", width=15)
    r.grid(row=6, column=0)
    r.configure(background="black", foreground="white")
    Entry(gmail_screen, textvariable=message, width=10).grid(row=6, column=2)
    Label(gmail_screen, text="", width=20).grid(row=7, column=0)

    # Send Button for Sending Mail
    Button(gmail_screen, text="Send", command=do_send_mail).grid(row=8, column=1)


# Function for Sending Mail
def do_send_mail():
    pywhatkit.mainfunctions.sendMail(sender_mail.get(), sender_pass.get(), receiver_mail.get(), message.get())
    Label(gmail_screen, text="\U0001f44d \U0001f44d", width=10).grid(row=11, column=1)
