import pywhatkit
from tkinter import *
from tkinter.ttk import *

number = None
hour = None
minutes = None
message = None
whatsapp_screen = None
main_screen = None


def user_interface():
    global whatsapp_screen
    whatsapp_screen = Toplevel(main_screen)
    whatsapp_screen.title("Whatsapp")
    global number
    global hour
    global minutes
    global message

    number = StringVar()
    hour = IntVar()
    minutes = IntVar()
    message = StringVar()

    # Number label & box
    Label(whatsapp_screen, text="Number", width=10).grid(row=0, column=0)
    Entry(whatsapp_screen, textvariable=number).grid(row=0, column=2)
    Label(whatsapp_screen, text=" ", width=10).grid(row=1, column=0)

    # Hour label & box
    Label(whatsapp_screen, text="Hour", width=10).grid(row=2, column=0)
    Entry(whatsapp_screen, textvariable=hour).grid(row=2, column=2)
    Label(whatsapp_screen, text=" ", width=10).grid(row=3, column=0)

    # Minutes label & box
    Label(whatsapp_screen, text="Minute", width=10).grid(row=4, column=0)
    Entry(whatsapp_screen, textvariable=minutes).grid(row=4, column=2)
    Label(whatsapp_screen, text=" ", width=10).grid(row=5, column=0)

    # Message label & box
    Label(whatsapp_screen, text="Message", width=10).grid(row=6, column=0)
    Entry(whatsapp_screen, textvariable=message).grid(row=6, column=2)
    Label(whatsapp_screen, text=" ", width=10).grid(row=7, column=0)

    # Submit button
    Button(whatsapp_screen, text="Submit", command=do_send_personal).grid(row=8, column=1)


def do_send_personal():
    x = number.get()
    x = "+" + x
    pywhatkit.sendwhatmsg(x, message.get(), hour.get(), minutes.get())


def do_send_group():
    pass
