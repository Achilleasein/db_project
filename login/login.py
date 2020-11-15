from tkinter import *
from tkinter import messagebox
import bcrypt
from database import Database
db = Database()
db.createTable()
class Login:

    """
        Class for Login
        @param username
        @param password
    """

    def __init__(self):
        self.username = input("\t\tEnter Your Username: ")
        self.password = getpass(prompt="\t\tEnter Your Password: ")

    def validate(self):
        data = (self.username,)
        inputData = (self.username, self.password,)
        if (db.validateData(data, inputData)):
            print("Logged In Successfully")
        else:
            print("Wrong Credentials")



print("\t\tWelcome to App")

while True:
    print("")
    print("\t\t1. Login")

    option = int(input("\t\tEnter Your Option: "))

    if option == 1:
        login = Login()
        login.validate()

    elif option == 2:
        register = Register()
        register.add()

    else: