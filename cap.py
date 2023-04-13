
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



