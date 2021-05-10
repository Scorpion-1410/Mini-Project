# Import Statements
# import pywhatkit
import smtplib
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
    sender_mail_label = Label(gmail_screen, text="Sender Mail", width=15)
    sender_mail_label.grid(row=0, column=0)
    sender_mail_label.configure(background="black", foreground="white")
    Entry(gmail_screen, textvariable=sender_mail, width=10).grid(row=0, column=2)
    Label(gmail_screen, text="", width=20).grid(row=1, column=0)

    # Sender Password Label & Box
    sender_pass_label = Label(gmail_screen, text="Sender Password", width=15)
    sender_pass_label.grid(row=2, column=0)
    sender_pass_label.configure(background="black", foreground="white")
    Entry(gmail_screen, textvariable=sender_pass, show="*", width=10).grid(row=2, column=2)
    Label(gmail_screen, text="", width=20).grid(row=3, column=0)

    # Receiver Mail Label & Box
    receiver_mail_label = Label(gmail_screen, text="Receiver Mail", width=15)
    receiver_mail_label.grid(row=4, column=0)
    receiver_mail_label.configure(background="black", foreground="white")
    Entry(gmail_screen, textvariable=receiver_mail, width=10).grid(row=4, column=2)
    Label(gmail_screen, text="", width=20).grid(row=5, column=0)

    # Message Label & Box
    message_label = Label(gmail_screen, text="Message", width=15)
    message_label.grid(row=6, column=0)
    message_label.configure(background="black", foreground="white")
    Entry(gmail_screen, textvariable=message, width=10).grid(row=6, column=2)
    Label(gmail_screen, text="", width=20).grid(row=7, column=0)

    # Send Button for Sending Mail
    Button(gmail_screen, text="Send", command=do_send_mail).grid(row=8, column=1)


try:
    def send_mail(my_mail, my_pass, mail_to, content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(my_mail, my_pass)
        server.sendmail(my_mail, mail_to, content)
        server.close()
except Exception as e:
    print(e)


# Function for Sending Mail
def do_send_mail():
    s_mail = sender_mail.get()+"@gmail.com"
    r_mail = receiver_mail.get()+"@gmail.com"
    send_mail(s_mail, sender_pass.get(), r_mail, message.get())
    Label(gmail_screen, text="Mail Sent Successfully").grid(row=11, column=1)
