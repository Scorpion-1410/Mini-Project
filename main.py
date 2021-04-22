from tkinter import *
from tkinter.ttk import *
from whatsapp import user_interface as wui
from gmail import user_interface as gui
from google_ import do_google
from youtube import do_youtube

main_screen = None


def main_account_screen():
    Label(text="*******************", width=10).pack()
    Label(text="Select Your Choice:").pack()
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
    Button(text="Youtube", command=do_youtube).pack()
    Label(text="", width=10).pack()
    Label(text="", width=10).pack()
