from tkinter import *
from tkinter.ttk import *

# import pywhatkit

from whatsapp import user_interface

main_screen = None


def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Account Login")
    Label(text="Select Your Choice").pack()
    Label(text="").pack()
    Button(text="WhatsApp", command=user_interface).pack()

    main_screen.mainloop()


main_account_screen()
