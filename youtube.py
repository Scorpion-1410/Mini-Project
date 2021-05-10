from tkinter import *
from tkinter import StringVar
from tkinter.ttk import *
import pywhatkit
from pytube import YouTube

youtube_screen = None
youtube_search = None
youtube_link = None
main_screen = None


def user_interface():
    global youtube_screen
    global youtube_search
    global youtube_link
    youtube_screen = Toplevel(main_screen)
    youtube_screen.title("Youtube Search")
    youtube_screen.geometry("350x200")
    youtube_search = StringVar()
    youtube_link = StringVar()

    # Label for YouTube Search
    yt_label = Label(youtube_screen, text="YouTube", width=10)
    yt_label.grid(row=2, column=2)
    yt_label.configure(background="black", foreground="white")

    # Entry box for Youtube Search
    yt_entry = Entry(youtube_screen, textvariable=youtube_search)
    yt_entry.grid(row=2, column=3)

    # Label for Link
    link_label = Label(youtube_screen, text='Link', width=10)
    link_label.grid(row=5, column=2)
    link_label.configure(background="black", foreground="white")

    # Entry box for Youtube link
    yt_link = Entry(youtube_screen, textvariable=youtube_link)
    yt_link.grid(row=5, column=3)

    # Download Button which will call downloader()
    generate_link_button = Button(youtube_screen, text='Download', command=downloader, width=7)
    generate_link_button.grid(row=10, column=3)

    # Wiki Search Button which will call play_on_youtube()
    generate_yt_search_button = Button(youtube_screen, text="Search", command=play_on_youtube)
    generate_yt_search_button.grid(row=3, column=3)


def play_on_youtube():
    pywhatkit.playonyt(youtube_search.get())


def downloader():
    url = YouTube(str(youtube_link.get()))
    filters = url.streams.filter(progressive=True, file_extension='mp4')
    filters.get_highest_resolution().download(output_path="Downloaded file")
    Label(youtube_screen, text="\U0001f44d \U0001f44d", width=10).grid(row=11, column=3)
