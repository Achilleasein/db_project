import tkinter as tk
import time
import mysql.connector
import inspect

def mysql_connection():
    db_connection = mysql.connector.connect(
        host = 'localhost',
        user = 'achilleas',
        password = '0lagiat0pr0ject',
        database = 'newspaper_publisher'
    )
    return db_connection

def show_entry_fields():
    # print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
    db_connection = mysql_connection()
    print(db_connection)
    db_cursor = db_connection.cursor()
	# out = "<html>%(head)s%(prologue)s%(query)s%(tail)s</html>" % locals()
    query = "select * from db_users where username LIKE '%s' and password LIKE '%s'" % (e1.get(), e2.get())

    try:
        db_cursor.execute(query)
        myresult = db_cursor.fetchall()
        for x in myresult:
            print(x)
        print("Query executed successfully")
    except:
        # db_connection.rollback()
        print("Error occured")

master = tk.Tk()
tk.Label(master, 
         text="First Name").grid(row=0)
tk.Label(master, 
         text="Last Name").grid(row=1)

e1 = tk.Entry(master)
e2 = tk.Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

tk.Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=tk.W, pady=4)
tk.Button(master, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=tk.W, pady=4)


tk.mainloop()