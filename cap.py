# import sqlite3

# import datetime


# def search():
#  if WHERE:
#   where=f"{where}%"
#   rows=cursor.execute(
#     SElECT*FROM Users
#   ); 

#   print("search")



# def add():

#   customer_email= input("Please enter your email:")
#   pass_word= input("Please eneter your password:")
#   first_name=input("Enter your first name:")
#   last_name=input("Enter your last name:")
#   phone=input("Please add working number to contact:")
#   hire_date=input("When were you hired?:")
#   user_type=input("User or Manager?:")
#   active=input("currently an active employee(Y/N)?:")
#   now=datetime.datetime.now()
#   date_created=now.strftime("%x")



#   print("add")

# def edit():
#   UPDATE Users:
#       query="update Users"
#       rows=cursor.execute(query).fetchall()

#       select=''
#       edit_dict={
#       "1":customer_email,
#       "2":pass_word,
#       "3":first_name,
#       "4":last_name,
#       "5":phone,
#       "6":hire_date,
#       "7":user_type,
#       "8":active,
#       "9":date_created,
#     }
#     headers = ["first_name", "last_name", "phone"]

#     for index, field  in enumerate(headers):
#       print(f"{index}: {field}")


#     user_choice = int(input("pick a number: "))

#     update_field = headers[user_choice]

#     query = f"UPDATE Users SET {update_field} = ?"
#     new_value = input('New value: ')
#     cursor.execute(query. [new_value])
#     connect.commit()

#   edit_user=input("enter email of user you would like to edit?")
#   print(1,2,3,4,5,6,7,8,9)
#   value_select=input("What would you like to select?")
  
#   new_value=edit_user.int()

#   SET  customer_email='new_value',
#   pass_word=,
#   first_name= 
#   last_name=,
#   phone=,
#   hire_date=,
#   user_type=,
#   active=,
#   date_created=,
  
#   WHERE customer_email=edit_user;





#   print("edit")

# def make_database(cursor):

#   with open("schema.SQL") as sql_file:
#     base = sql_file.read()
#     cursor.executescript(base)
#   connection.commit()  

# def pull_email():
#   query = "select customer_email from Users" 
#   rows = cursor.execute(query).fetchall()




#   for row in rows:
#     email_list.append(row)
#   if email_list == []:
#     empty_query = "insert into Users(customer_email,pass_word) values(?,?)" 
#     values = ("super-Admin","1234")
#     cursor.execute(empty_query, values) 
#     connection.commit()  

# connection = sqlite3.connect('capstone.db')

# cursor = connection.cursor()
# make_database(cursor)
# email_list =[]
# pull_email()
# user_input = input("Please enter email:")
# user_password = input("Please enter your password:")
# print('user_input: ',user_input)

# selection =""
# func_container={
#   "search": search,
#   "add"   : add,
#   "edit"  : edit
# }



# while True:
#   print("(1) to search User")
#   print("(2) to add new User")
#   print("(3) to edit User")
#   print("(4) to quit")
#   answer = input("Select an option:")
#   if answer == '1':
#     selection="search"
#     print("Enter User information:")
#   elif answer =='2':
#     selection ="add"
#     print("Enter user to add:")
#   elif answer =='3':
#     selection="edit"
#     print("Please enter user info to edit:")
#   elif answer == '4':
#     break  
#     print("Goodbye")
#   func_container[f"{selection}"]()

import sqlite3
import datetime

def search(cursor):
    where = input("Enter search query:")
    query = f"SELECT * FROM Users WHERE customer_email LIKE '{where}%'"
    rows = cursor.execute(query).fetchall()
    if rows == []:
        print("No results found.")
    else:
        print(rows)

def add(cursor):
    customer_email = input("Please enter your email:")
    pass_word = input("Please enter your password:")
    first_name = input("Enter your first name:")
    last_name = input("Enter your last name:")
    phone = input("Please add working number to contact:")
    hire_date = input("When were you hired?:")
    user_type = input("User or Manager?:")
    active = input("currently an active employee(Y/N)?:")
    now = datetime.datetime.now()
    date_created = now.strftime("%x")
    query = "INSERT INTO Users (customer_email, pass_word, first_name, last_name, phone, hire_date, user_type, active, date_created) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
    values = (customer_email, pass_word, first_name, last_name, phone, hire_date, user_type, active, date_created)
    cursor.execute(query, values)
    print(f"{cursor.rowcount} user added.")
    
def edit(cursor):
    edit_user = input("Enter email of user you would like to edit:")
    headers = ["customer_email", "pass_word", "first_name", "last_name", "phone", "hire_date", "user_type", "active", "date_created"]
    for index, field in enumerate(headers):
        print(f"{index}: {field}")
    user_choice = int(input("Pick a number: "))
    update_field = headers[user_choice]
    new_value = input("New value: ")
    query = f"UPDATE Users SET {update_field} = ? WHERE customer_email = ?"
    values = (new_value, edit_user)
    cursor.execute(query, values)
    print(f"{cursor.rowcount} user updated.")

def make_database(cursor):
    with open("schema.SQL") as sql_file:
        base = sql_file.read()
        cursor.executescript(base)

def pull_email(cursor):
    query = "SELECT customer_email FROM Users"
    rows = cursor.execute(query).fetchall()
    email_list = [row[0] for row in rows]
    if email_list == []:
        query = "INSERT INTO Users (customer_email, pass_word) VALUES (?, ?)"
        values = ("super-Admin", "1234")
        cursor.execute(query, values)
        print("Default user added.")
    else:
        print("Emails loaded.")
    return email_list

connection = sqlite3.connect('capstone.db')
cursor = connection.cursor()
make_database(cursor)
email_list = pull_email(cursor)

func_container = {
    "search": search,
    "add": add,
    "edit": edit
}

while True:
    print("(1) to search User")
    print("(2) to add new User")
    print("(3) to edit User")
    print("(4) to quit")
    answer = input("Select an option:")
    if answer == '1':
        func_container["search"](cursor)
    elif answer == '2':
        func_container["add"](cursor)
    elif answer == '3':
        func_container["edit"](cursor)
    elif answer == '4':
        break
    else:
        print("Invalid selection.")

connection.commit()
connection.close()



