from tkinter import *
from tkinter import StringVar
from tkinter.ttk import *
import pywhatkit

google_screen = None
google_search = None
main_screen = None


def do_google():
    global google_screen
    global google_search
    google_screen = Toplevel(main_screen)
    google_screen.title("Google Search")
    google_screen.geometry("500x200")
    google_search = StringVar()

    google_label = Label(google_screen, text="Google", width=20)
    google_label.grid(row=4, column=2)
    google_label.configure(background="black", foreground="white")

    # Entry box for Google Search
    google_entry = Entry(google_screen, textvariable=google_search)
    google_entry.grid(row=4, column=3)

    # Google Search Button which will call googleSearch()
    generate_google_search_button = Button(google_screen, text="Search", command=googleSearch)
    generate_google_search_button.grid(row=7, column=3)


def googleSearch():
    pywhatkit.search(google_search.get())
    google_screen.configure(background="yellow")
