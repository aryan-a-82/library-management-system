import json
from pathlib import Path

class Library:
    def __init__(self, bookList, bookLendList):
        print("Welcome to the library")
        print("1 : Display the book List")
        print("2 : Search a book")
        print("3 : Lend the book")
        print("4 : Return the book")
        print("5 : Add a book")
        print("Q : Quit!")
        self.bookList = bookList
        self.bookLendList = bookLendList

    def displayBook(self):
        print("\nBook : Publication")
        print("===================")
        for i in sorted(self.bookList):
            print(i[0] + ' : ' + i[1])
        print("===================")

    def lendBook(self, book, publication, user):
        check = False
        for book_list in self.bookList:
            if(book == book_list[0] and publication == book_list[1]):
                check = True
                break
        if(check):
            book_info = [book, publication, user]
            for details in self.bookLendList:
                if(book in details and publication in details):
                    check = False
                    break
            if(check):
                self.bookLendList.append(book_info)
                # Updating Book Lend List
                with open(path_bLL, "w") as f:
                    json.dump(self.bookLendList, f, indent = 2)
                print("Book has been lent!")
            else:print("Book is not available for lending!")
        else:print("Book is not available in our Library!")

    def returnBook(self, book, publication):
        check = False
        for details in self.bookLendList:
            if(book in details and publication in details):
                check = True
                break
        if(check):
            self.bookLendList.pop(self.bookLendList.index(details))
            # Updating Book Lend List
            with open(path_bLL, "w") as f:
                json.dump(self.bookLendList, f, indent = 2)
            print("Thank you for returning the book!")
        else:
            print("This book has never been issued!")
    
    def addBook(self, book, publication):
        book_info = [book, publication]
        self.bookList.append(book_info)
        # Updating Book List
        with open(path_bL, "w") as f:
            json.dump(self.bookList, f, indent = 2)
        print("Book has been added to the library!")

    def searchBook(self, book):
        dct = {}
        i = 1
        for books in self.bookList:
            if(book in books):
                dct[i] = [books[0], books[1]]
                i += 1
        if(len(dct) == 0):return None
        else:return (dct,i)

# Loading Data
path_bL = Path(__file__).parent/"./bookList.json"
path_bLL = Path(__file__).parent/"./bookLendList.json"

with open(path_bL, "r") as f:
    bookList = sorted(json.load(f))

with open(path_bLL, "r") as f:
    bookLendList = json.load(f)

# Creating object
library = Library(bookList, bookLendList)

start = True
while(start == True):
    choice = input("\nEnter your choice : ").strip()
    while(choice not in ['1','2','3','4','5','Q']):
        print("Invalid choice!\n")
        choice = input("Enter your choice : ").strip()
    
    if(choice == '1'):
        library.displayBook()
    
    if(choice == '2'):
        book = input("Enter book name : ")
        res, i = library.searchBook(book)
        if(res == None): print("No books found!")
        else:
            print(f"{i-1} Book Found!")
            for i in res: print(str(i) + ' : ' + str(res[i]))

    if(choice == '3'):
        book = input("Enter book's name : ").strip().lower()
        publication = input("Enter book publication : ").strip().lower()
        user = input("Enter your name : ").strip().lower()
        library.lendBook(book, publication, user)

    if(choice == '4'):
        book = input("Enter book name : ").strip().lower()
        publication = input("Enter book's publication : ").strip().lower()
        library.returnBook(book, publication)

    if(choice == '5'):
        book = input("Enter book name : ").strip().lower()
        publication = input("Enter book's publication : ").strip().lower()
        library.addBook(book, publication)

    if(choice == 'Q' or choice == 'q'):
        print("Thank you for visiting!")
        start = False
        break

    print("\n1 : Display the book List")
    print("2 : Search a book")
    print("3 : Lend the book")
    print("4 : Return the book")
    print("5 : Add a book")
    print("Q : Quit!")