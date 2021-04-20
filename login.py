# import statement
from tkinter import *
from tkinter.ttk import *
import re
from main import main_account_screen

# screen variable
main_screen1 = None
login_screen = None
register_screen = None

# login variables
input_username = None
input_password = None

# registration variables
fname = None
lname = None
username = None
password = None

entry_password = None
entry_login = None

'''                                            Functions                                               '''


# appending to user data to database named database.txt
def registration():
    file = open("database.txt", "r+")
    line = file.readlines()

    # checking password strength
    fl = 0
    while True:
        if (len(password.get()) < 8):
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
            password_valid_label = Label(register_screen, text="Valid password").pack()
            break
    if fl == -1:
        password_invalid_label = Label(register_screen, text="Password Not Valid").pack()
    else:
        try:
            index = line.index("Username:-" + username.get() + "\n")
            already_exist_label = Label(register_screen, text="User Already Exists!!").pack()
        except:
            file.write("Name:-" + fname.get() + " " + lname.get() + "\nUsername:-" +
                       username.get() + "\nPassword:-" + password.get() + "\n")
            successfully_done_label = Label(register_screen, text="Successfully Registered").pack()
    file.close()


# validating the credentials
def validation():
    # formatting the username and password
    formated_username = "Username:-" + input_username.get() + "\n"
    formated_password = "Password:-" + input_password.get() + "\n"

    file = open("database.txt", "r")
    line = file.readlines()
    try:
        username_index = line.index(formated_username)
        for i in range(len(line)):
            if formated_username == line[username_index]:
                if formated_password == line[username_index + 1]:
                    congo = Label(login_screen, text="Congratulations").pack()
                    main_account_screen()
                    break
                else:
                    password_incorrect = Label(login_screen, text="Password Incorrect").pack()
                    break
    except:
        user_not_found = Label(login_screen, text="User not Found").pack()
    file.close()



"""                                           Screens                                                  """


# login screen
def loginScreen():
    global login_screen
    global input_username
    global input_password
    global entry_login
    global entry_password

    login_screen = Toplevel(main_screen1)
    login_screen.title("Login")
    input_username = StringVar()
    input_password = StringVar()

    entry_login = Entry(login_screen, textvariable=input_username).pack()

    entry_password = Entry(login_screen, textvariable=input_password, show='*').pack()

    button_login = Button(login_screen, text="Login", command=validation).pack()

    button_to_main_screen = Button(login_screen, text="Main Screen", command=main_account_screen).pack()


# register screen
def registerScreen():
    global register_screen
    register_screen = Toplevel(main_screen1)
    register_screen.title("Register")

    global fname
    global lname
    global username
    global password

    fname = StringVar()
    lname = StringVar()
    username = StringVar()
    password = StringVar()

    entry_fname = Entry(register_screen, textvariable=fname).pack()

    entry_lname = Entry(register_screen, textvariable=lname).pack()

    entry_username = Entry(register_screen, textvariable=username).pack()

    entry_key = Entry(register_screen, textvariable=password).pack()

    button_register = Button(register_screen, text="Register", command=registration).pack()

    button_to_main_screen = Button(register_screen, text="Main Screen", command=main_account_screen).pack()


# main screen
def main_account_screen():
    global main_screen1
    main_screen1 = Tk()
    main_screen1.geometry("300x250")
    main_screen1.title("Account Login")

    Label(main_screen1, text="Select Your Choice").pack()
    Label(main_screen1, text="").pack()
    Button(main_screen1, text="Log In", width="30", command=loginScreen).pack()
    Label(main_screen1, text="").pack()
    Button(main_screen1, text="Register", width="30", command=registerScreen).pack()
    main_screen1.mainloop()


# main screen function calling
main_account_screen()