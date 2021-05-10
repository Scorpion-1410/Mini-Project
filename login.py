# import statement
import logging
from tkinter import *
from tkinter.ttk import *
import re
from main import home_page_screen

# import tkinter.font

# screen variable
main_screen = None
login_screen = None
register_screen = None

# login variables
input_username = None
input_password = None

# registration variables
first_name = None
last_name = None
username = None
password = None

entry_password = None
entry_login = None


# appending to user data to database named database.txt
def registration():
    file = open("database.txt", "r+")
    line = file.readlines()

    # checking password strength
    # fl = 0
    while True:
        if len(password.get()) < 8:
            fl = -1
            break
        elif not re.search("[a-z]", password.get()):
            fl = -1
            break
        elif not re.search("[A-Z]", password.get()):
            fl = -1
            break
        elif not re.search("[0-9]", password.get()):
            fl = -1
            break
        elif not re.search("[_@$]", password.get()):
            fl = -1
            break
        elif re.search("\s", password.get()):
            fl = -1
            break
        else:
            fl = 0
            Label(register_screen, text="Valid password").pack()
            break
    if fl == -1:
        Label(register_screen, text="Password Not Valid").pack()
    else:
        try:
            line.index("Username:-" + username.get() + "\n")
            Label(register_screen, text="User Already Exists!!").pack()
        except Exception as e:
            logging.exception(e)
            file.write("Name:-" + first_name.get() + " " + last_name.get() + "\nUsername:-" +
                       username.get() + "\nPassword:-" + password.get() + "\n")
            Label(register_screen, text="Successfully Registered").pack()
    file.close()


# validating the credentials
def validation():
    # formatting the username and password
    formatted_username = "Username:-" + input_username.get() + "\n"
    formatted_password = "Password:-" + input_password.get() + "\n"

    file = open("database.txt", "r")
    line = file.readlines()
    try:
        username_index = line.index(formatted_username)
        for i in range(len(line)):
            if formatted_username == line[username_index]:
                if formatted_password == line[username_index + 1]:
                    Label(login_screen, text="Congratulations").pack()
                    home_page_screen()
                    break
                else:
                    Label(login_screen, text="Password Incorrect").pack()
                    break
    except Exception as e:
        logging.exception(e)
        Label(login_screen, text="User not Found").pack()
    file.close()


# login screen
def login_screen_ui():
    global login_screen
    global input_username
    global input_password
    global entry_login
    global entry_password

    login_screen = Toplevel(main_screen)
    login_screen.geometry("500x500")
    login_screen.title("Login")
    input_username = StringVar()
    input_password = StringVar()

    Label(login_screen, text="Username", width=10).pack()
    Entry(login_screen, textvariable=input_username).pack()
    Label(text="").pack()
    Label(text="", width=10).pack()
    Label(login_screen, text="Password", width=10).pack()
    Entry(login_screen, textvariable=input_password, show='*').pack()

    Label(login_screen, text="", width=10).pack()
    Button(login_screen, text="Login", command=validation).pack()

    Label(login_screen, text="", width=10).pack()
    Button(login_screen, text="Main Screen", command=main_account_screen).pack()


# register screen
def register_screen_ui():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")

    global first_name
    global last_name
    global username
    global password

    first_name = StringVar()
    last_name = StringVar()
    username = StringVar()
    password = StringVar()

    Label(register_screen, text="First Name").pack()
    Entry(register_screen, textvariable=first_name).pack()

    Label(register_screen, text="Last Name").pack()
    Entry(register_screen, textvariable=last_name).pack()

    Label(register_screen, text="User Name").pack()
    Entry(register_screen, textvariable=username).pack()

    Label(register_screen, text="Password").pack()
    Entry(register_screen, textvariable=password).pack()

    Button(register_screen, text="Register", command=registration).pack()

    Button(register_screen, text="Main Screen", command=main_account_screen).pack()


# main screen
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("1000x600")
    main_screen.title("Account Login")

    tr = Label(main_screen, text="Welcome to Social Media Utility Tool")
    tr.pack()
    font_tuple = ("Comic Sans MS", 20, "bold")
    tr.configure(font=font_tuple)
    d = Label(main_screen, text="Select Your Choice :")
    d.pack()
    d.configure(background="black", foreground="white")
    Label(main_screen, text="").pack()
    Button(main_screen, text="Log In", width="30", command=login_screen_ui).pack()
    Label(main_screen, text="").pack()
    Button(main_screen, text="Register", width="30", command=register_screen_ui).pack()
    main_screen.mainloop()


# main screen function calling
main_account_screen()
