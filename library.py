import mysql.connector

password = 'admin'

def add_book():
    global cursor
    bookname = input("Enter Bookname: ")
    genre = input("Enter Genre")
    quantity = int(input("Enter Quantity: "))
    query = "INSERT into books(bookname,genre,quantity)" \
        "VALUES(%s,%s,%s)"

    vals = (bookname,genre,quantity)
    try:
        cursor.execute(query,vals)
        cnx.commit()
        print(f"Book {bookname} has been added")
    except:
        cnx.rollback()
        print("Something wrong, please try again")

def delete_book():
    global cursor
    bookname = input("Enter Bookname: ")
    query = "DELETE FROM books WHERE bookname=%s"
    val = (bookname,)
    try:
        cursor.execute(query,val)
        cnx.commit()
        print(f"Book {bookname} has been deleted")
    except:
        cnx.rollback()
        print("Something wrong, please try again.")

def update_quantity():
    global cursor
    bookname = input("Enter Bookname to edit quantity: ")
    new_quantity = int(input("New Quantity: "))
    query = """ UPDATE books
    SET quantity=(%s)
    WHERE bookname=(%s)"""
    val = (new_quantity,bookname)
    try:
        cursor.execure(query,val)
        cnx.commit()
        print(f"Quantity of the book {bookname} has been updated.")
    except:
        cnx.rollback()
        print("Something wrong, please try again.")

def change_genre():
    global cursor
    bookname = input("Enter bookname to edit quantity: ")
    new_genre = input("Enter new genre: ")
    query = """ UPDATE books
    SET genre=(%s)
    WHERE bookname=(%s)"""
    val = (new_genre,bookname)
    try:
        cursor.execute(query,val)
        cnx.commit()
        print(f"Genre of book {bookname} has been changed to {new_genre}")
    except:
        cnx.rollback()
        print("Something wrong, please try again.")

def search_book():
    available_book()
    bookname = input("Enter bookname to search: ")
    new_genre = input("Enter new genre: ")
    query = "select * from books where bookname=%s"
    val = (bookname,)
    try:
        cursor.execute(query,val)
        books_record = cursor.fetchall()
        print("BOOKS AVAILABLE \n BOOKNAME Genre Quantity")
        for book_details in books_record:
            print(book_details)
    except:
        cnx.rollback()
        print("Book Not Found, Please try again.")
    
def available_book():
    global cursor
    print("ALL AVAILABLE BOOK")
    print("BOOKNAME  GENRE  QUANTITY")
    cursor.execute("Select * from books;")
    books_record = cursor.fetchall()
    for book_details in books_record:
        print(book_details)

cnx = mysql.connection.connect(user = 'root',passwd='root',host='localhost',database='library')
if cnx.is_connected:
    cursor = cnx.cursor()

print("Welcome to Python Library Management")
user = input("Enter code to confirm user type \n 1. Client\n 2. Admin\n")
if user == '1':
    choice = input("Enter code to perform user operation \n 1. Search\n")
    search = 'y'
    while search == 'y':
        if choice == '1':
            search_book()
            search = input("Do you want to search for another book? (Y / N): ")
            print("Thank you for using Library Management System")

if user == '2':
    pass_check = input("Insert Admin Password to Proceed: ")
    if pass_check == password:
        print("Enter Code to perform Admin operation:\n 1. Add new book\n 2. Delete Book\n 3. Update Quantity\n 4. Change genre\n 5. Search Book ")
    option = 'Y'
    while option == 'Y':
        option = input("Enter Option: ")
        if option == '1':
            add_book()
        if option == '2':
            delete_book()
        if option == '3':
            update_quantity()
        if option == '4':
            change_genre()
        if option == '5':
            search_book()
        option = input("Do you want to do anything else? (Y/N)")
        options=options.upper()
    print("Sign out from the admin user")

else:
    print("Wrong Password: \n [+] Session Expired, try again!")

cnx.close()