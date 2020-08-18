from tkinter import *
import sqlite3
from tkinter import messagebox


#popup messages for when logging in and creating an account
#if username entered does not match any in the database
def popup():
    #connect to the database and create the cursor
    connection = sqlite3.connect('accounts.db')
    #the cursor is the thing that you use to add/edit the database
    c = connection.cursor()
    c.execute('SELECT MAX(OID) FROM accounts')
    answer = c.fetchall()
    #tupcounter is used so the script knows when it reaches the last entry in the database and so once looped through all entries and no username match found, the error will be produced
    tupcount = (count,)
    if tupcount == answer[0]:
        messagebox.showerror('Error', 'Username does not exist')
    
#incorrect password error    
def popup1():
       messagebox.showerror('Error', 'Incorrect Password')
    
#successful login
def popup2():
    messagebox.showinfo('Hello World', 'Login Sucessful')
    root.destroy()
    
#non matching passwords upon creating an account
def popup3():
    messagebox.showerror('', 'Passwords do not match, try again')

root = Tk()
root.geometry('200x100')
root.title('Login System')

#create a login function
def login():
    
    
    #first you have to connect to the database and create the cursor
    connection = sqlite3.connect('accounts.db')
    #the cursor is the thing that you use to add/edit the database
    c = connection.cursor()
    
    #query the database
    c.execute('SELECT *, OID FROM accounts')
    #fetch all the records in databse
    records = c.fetchall()
    #print(records)
    
    #loop through records to see if username is in system and if its username matches the password
    global count
    login = True
    while login:
        count = 0
        for record in records:
            if record[3] == username.get():
                if record[4] == password.get():
                    login = False
                    popup2()
                    continue
                else:
                    login = False
                    popup1()
                    continue
                    
            else:
                login = False
                count+= 1
                popup()
                
    #commit changes
    connection.commit()
    #close database connection
    connection.close()
        
#create an account function
def create():
    new_account = Tk()
    new_account.geometry('300x180')
    
    global first_name
    global last_name
    global email
    global username
    global password
    global re_password
    
    
    #create entry fields and labels
    first_name = Entry(new_account)
    first_name.grid(row = 0 , column = 1)
    
    first_name_label = Label(new_account , text = 'First Name')
    first_name_label.grid(row = 0 , column = 0)
    
    last_name = Entry(new_account)
    last_name.grid(row = 1 , column = 1)
    
    last_name_label = Label(new_account , text = 'Last Name')
    last_name_label.grid(row = 1 , column = 0)
    
    email = Entry(new_account)
    email.grid(row = 2 , column = 1)
    
    email_label = Label(new_account , text = 'Email')
    email_label.grid(row = 2 , column = 0)
    
    username = Entry(new_account)
    username.grid(row = 3 , column = 1)
    
    username_label = Label(new_account , text = 'Username')
    username_label.grid(row = 3 , column = 0)
    
    password = Entry(new_account)
    password.grid(row = 4 , column = 1)
    
    password_label = Label(new_account , text = 'Password')
    bullet = "\u2022"
    password.config(show = bullet)
    password_label.grid(row = 4 , column = 0)
    
    re_password = Entry(new_account)
    re_password.grid(row = 5 , column = 1)
    
    re_password_label = Label(new_account , text = 'Re Enter Password')
    bullet = "\u2022"
    re_password.config(show = bullet)
    re_password_label.grid(row = 5 , column = 0)
    
    create = Button(new_account, text = 'Create Account', command = add)
    create.grid(row = 6 , column = 1 , columnspan = 1 , pady = 8, padx = 8, ipadx = 20)
    
    
    new_account.mainloop()
    

#function to add details to databse    
def add():
    
    #first you have to connect to the database and create the cursor
    connection = sqlite3.connect('accounts.db')
    #the cursor is the thing that you use to add/edit the database
    c = connection.cursor()
  
    
    if password.get() == re_password.get():
        #Insert into database table
        c.execute('INSERT INTO accounts VALUES(:first_name,:last_name,:email,:username,:password)',
             
             {
                 'first_name' : first_name.get(),
                 'last_name' : last_name.get(),
                 'email' : email.get(),
                 'username' : username.get(),
                 'password' : password.get(),   
             })
       
        
        #clear entry boxes
        first_name.delete(0, END)
        last_name.delete(0, END)
        email.delete(0, END)
        username.delete(0, END)
        password.delete(0, END)
        re_password.delete(0 , END)
        
        #commit changes
        connection.commit()
        #close database connection
        connection.close()
        
        
    else:
        popup3()
    


#prepare first window that will be displayed upon opening script - i.e option to login or create an account
#create username entry box
username = Entry(root)
username.grid(row = 0 , column = 1)
#create username entry label
username_label = Label(root, text = 'Username')
username_label.grid(row = 0 , column = 0)

#create password entry box
password = Entry(root)
password.grid(row = 1, column = 1)
bullet = "\u2022"
password.config(show = bullet)

#create label
password_label = Label(root, text = 'Password')
password_label.grid(row = 1 , column = 0)

#create login button
login_button = Button(root, text = 'Login', command = login)
login_button.grid(row = 2 , column = 0, columnspan = 3, padx = 5, pady = 5, ipadx = 10)

#create new account button
new_account = Button(root, text="Create new account",relief = 'flat', font= "Verdana 8 underline", command = create)
new_account.grid(row = 3, column = 0, columnspan = 5 , ipadx = 15)







root.mainloop()
