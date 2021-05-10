from tkinter import *
from tkinter.ttk import *
from whatsapp import user_interface as whatsapp_ui
from gmail import user_interface as gmail_ui
from google_ import user_interface as google_ui
from youtube import user_interface as youtube_ui

main_screen = None
home_screen = None


def home_page_screen():
    global main_screen
    global home_screen

    home_screen = Toplevel(main_screen)
    home_screen.title("Home Screen")

    Label(home_screen, text="Select Your Choice:").pack()
    Label(home_screen, text="*******************", width=10).pack()
    Label(home_screen, text="").pack()
    Button(home_screen, text="WhatsApp", command=whatsapp_ui).pack()
    Label(home_screen, text="", width=10).pack()
    Label(home_screen, text="", width=10).pack()
    Button(home_screen, text="Gmail", command=gmail_ui).pack()
    Label(home_screen, text="", width=10).pack()
    Label(home_screen, text="", width=10).pack()
    Button(home_screen, text="Google", command=google_ui).pack()
    Label(home_screen, text="", width=10).pack()
    Label(home_screen, text="", width=10).pack()
    Button(home_screen, text="Youtube", command=youtube_ui).pack()
    Label(home_screen, text="", width=10).pack()
    Label(home_screen, text="", width=10).pack()
