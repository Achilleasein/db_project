### IMPORTS ###
import os
from tkinter import *
import tkinter as tk
import time
import mysql.connector
import inspect
# import login
###############

### Global Variables ###
HEIGHT = "800"
WIDTH = "640"
########################

## Class declaration ##
class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Welcome to the publisher DBMS.")
        self.selected = tk.IntVar()
        self.selected.set(0)

        self.login = tk.Button(self, text = 'Login', command = self.clicked)
        self.mainloop()

    def clicked(self):
        print(f'clicked {self.selected.get()}')

        v = self.selected.get()
        if v == 0:
            login()
        else:
            print('an error occurred, the wrong value was received')


    def submitact(self, username, password): 
        
        user = username.get() 
        passw = password.get() 

        print(f"The name entered by you is {user} {passw}") 

        find_user(user, passw) 

    def run(self):
        self.app.mainloop()


## Function declaration ##
# setting size for main_window
def setwinsize(main_window):
    main_window.geometry(HEIGHT + "x" + WIDTH )
    return main_window

# Handle the connection to mysql db
def mysql_connection():
    db_connection = mysql.connector.connect(
        host = 'localhost',
        user = 'achilleas',
        password = '0lagiat0pr0ject',
        database = 'newspaper_publisher'
    )
    return db_connection

# find the user in mysql
def find_user(username, password):
    curframe = inspect.currentframe()
    calframe = inspect.getouterframes(curframe, 2)
    print('caller name:', calframe[1][3])
    
    db_connection = mysql_connection()
    print(db_connection)
    db_cursor = db_connection.cursor()
	# out = "<html>%(head)s%(prologue)s%(query)s%(tail)s</html>" % locals()
    query = "select * from db_users where username LIKE %s and password LIKE %s" % (username, password)

    try:
        db_cursor.execute(query)
        myresult = db_cursor.fetchall()
        for x in myresult:
            print(x)
        print("Query executed successfully")
    except:
        # db_connection.rollback()
        print("Error occured")

# Login functionality
def login(): #db_cursor
    main_window = tk.Tk(className="Publisher DB")
    main_window = setwinsize(main_window)
    greeting = tk.Label(text = "Welcome to the database.", bg="#0E4A63", font=("Calibri",14))

    C = Canvas(main_window, bg ="blue", height = 250, width = 300) 

    # Definging the first row 
    lblfrstrow = tk.Label(main_window, text ="Username -", ) 
    lblfrstrow.place(x = 50, y = 20) 

    username = tk.Entry(main_window, width = 35) 
    username.place(x = 150, y = 20, width = 100) 

    lblsecrow = tk.Label(main_window, text ="Password -") 
    lblsecrow.place(x = 50, y = 50) 

    password = tk.Entry(main_window, width = 35) 
    password.place(x = 150, y = 50, width = 100) 

    submitbtn = tk.Button(main_window, text ="Login", 
                        bg ='blue', command = submitact(username, password)) 
    submitbtn.place(x = 150, y = 135, width = 55) 
    
    return main_window



# Submit function
def submitact( username, password): 
    
    user = username.get() 
    passw = password.get() 

    print(f"The name entered by you is {user} {passw}") 

    find_user(user, passw) 


## main class
if __name__ == "__main__":
    
    login_register_window = MainWindow()

    login_register_window.run() 
