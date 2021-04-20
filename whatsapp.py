# Import Statements
import pywhatkit
from tkinter import *
from tkinter.ttk import *

# Global Variable is Declared and Initialize as None
receiverId = None
hour = None
minutes = None
message = None
whatsapp_screen = None
main_screen = None


# Function for User Interface for Whatsapp Screen
def user_interface():
    # Global variable Assigned Datatype
    global main_screen
    global whatsapp_screen
    global receiverId
    global hour
    global minutes
    global message

    receiverId = StringVar()
    hour = IntVar()
    minutes = IntVar()
    message = StringVar()

    # New Whatsapp Screen is Created
    whatsapp_screen = Toplevel(main_screen)
    whatsapp_screen.title("Whatsapp")

    # Number Label & Box
    l = Label(whatsapp_screen, text="ReceiverID", width=10)
    l.grid(row=0, column=0)
    l.configure(background="black", foreground="white")
    Entry(whatsapp_screen, textvariable=receiverId).grid(row=0, column=2)
    Label(whatsapp_screen, text=" ", width=10).grid(row=1, column=0)

    # Hour Label & Box
    q = Label(whatsapp_screen, text="Hour", width=10)
    q.grid(row=2, column=0)
    q.configure(background="black", foreground="white")
    Entry(whatsapp_screen, textvariable=hour).grid(row=2, column=2)
    Label(whatsapp_screen, text=" ", width=10).grid(row=3, column=0)

    # Minutes Label & Box
    r = Label(whatsapp_screen, text="Minute", width=10)
    r.grid(row=4, column=0)
    r.configure(background="black", foreground="white")
    Entry(whatsapp_screen, textvariable=minutes).grid(row=4, column=2)
    Label(whatsapp_screen, text=" ", width=10).grid(row=5, column=0)

    # Message Label & Box
    y = Label(whatsapp_screen, text="Message", width=10)
    y.grid(row=6, column=0)
    y.configure(background="black", foreground="white")
    Entry(whatsapp_screen, textvariable=message).grid(row=6, column=2)
    Label(whatsapp_screen, text=" ", width=10).grid(row=7, column=0)

    # Submit Button for Personal Message
    Button(whatsapp_screen, text="Personal", command=do_send_personal).grid(row=10, column=1)

    # Submit Button for Group Message
    Button(whatsapp_screen, text="Group", command=do_send_group).grid(row=10, column=2)
    # Label(whatsapp_screen, text="\U0001f44d \U0001f44d", width=10).grid(row=11, column=1)


# Function for Sending Personal Message
def do_send_personal():
    x = receiverId.get()
    x = "+91" + x
    pywhatkit.sendwhatmsg(x, message.get(), hour.get(), minutes.get(), wait_time=10)
    Label(whatsapp_screen, text="\U0001f44d \U0001f44d", width=10).grid(row=11, column=1)


# Function for Sending Group Message
def do_send_group():
    pywhatkit.sendwhatmsg_to_group(receiverId.get(), message.get(), hour.get(), minutes.get(), wait_time=20)
    Label(whatsapp_screen, text="\U0001f44d \U0001f44d", width=10).grid(row=11, column=2)
