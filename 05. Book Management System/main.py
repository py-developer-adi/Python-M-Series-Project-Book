'''PYCODE'''

# ? 05. Book Management System
# ? Features: Add, delete, search, and update book records.

# * Source Code
import os

main_folder = "Books"
def init():
    os.mkdir(main_folder) if not(os.path.exists(main_folder)) else 0
    
init()

def addBook(title, pages, author):
    bookid = len(os.listdir(main_folder))
    with open(f"{main_folder}/{bookid}.txt", 'w') as f:
        f.writelines([f"{title}\n", f"{pages}\n", f"{author}\n"])
    print(f"Book ID: {bookid}")
    
def searchBook(bookid):
    with open(f"{main_folder}/{bookid}.txt", 'r+') as f:
        return f.readlines()
        
def updateBook(bookid, title='', pages='', author=''):
    data = searchBook(bookid)
    title = data[0][:-1] if title == '' else title
    pages = data[1][:-1] if pages == '' else pages
    author = data[2][:-1] if author == '' else author
    with open(f"{main_folder}/{bookid}.txt", "w") as f:
        f.writelines([f"{title}\n", f"{pages}\n", f"{author}\n"])     
        
def deleteBook(bookid):
    os.remove(f"{main_folder}/{bookid}.txt")
    
print("Book Management System")
while True:
    user = input(">>> ")
    
    if user == 'add':
        addBook(
            title=input('Title: '),
            pages=input('Pages: '),
            author=input('Author: ')
        )
        
    elif user == 'remove':
        deleteBook(
            bookid=input('Book ID: ')
        )
        
    elif user == 'search':
        data = searchBook(
            bookid=input('Book ID: ')
        )
        print(f"Title: {data[0]}", end="")
        print(f"Pages: {data[1]}", end="")
        print(f"Author: {data[2]}", end="")
        
    elif user == 'update':
        updateBook(
            bookid=input('Book ID: '),
            title=input('Title (Optional): '),
            pages=input('Pages (Optional): '),
            author=input('Author (Optional): ')
        )
        
    else:
        print(f"Invalid Command {user}")
