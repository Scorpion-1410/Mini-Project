from tkinter import *
from tkinter.ttk import *
from whatsapp import user_interface as wui
from gmail import user_interface as gui
from google_ import do_google

main_screen = None


def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("500x350")
    main_screen.title("Account Login")
    Label(text="Select Your Choice").pack()
    Label(text="").pack()
    Button(text="WhatsApp", command=wui).pack()
    Label(text="", width=10).pack()
    Label(text="", width=10).pack()
    Button(text="Gmail", command=gui).pack()
    Label(text="", width=10).pack()
    Label(text="", width=10).pack()
    Button(text="Google", command=do_google).pack()
    Label(text="", width=10).pack()
    Label(text="", width=10).pack()

    main_screen.mainloop()


main_account_screen()
