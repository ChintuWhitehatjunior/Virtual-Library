class Library:
    def __init__(self, ListOfBooks):
        self.books = ListOfBooks

    def Details(self):
        print("Books available in library are:-")
        no = 1
        for i in self.books:
            print(f"{no}:- {i}")
            no += 1

    def Borrow(self, bookname):
        if bookname in self.books:
            print(f"{bookname} has been issued to you!, please return it safely")
            self.books.remove(bookname)      
        else:
            print("The book you requested to issue is not available right now or has been already issued, Sorry")
            

    def Give(self, bookname):
        self.books.append(bookname)
        print(f"Thanks for returning/donating {bookname} in the library!")

class Student:
    def __init__(self):
        self.booklist = []

    def Reqest(self):
        self.book = input("Enter the name of the book you want to issue:- ")
        self.booklist.append(self.book)
        return self.book
        
    def Return(self):
        self.book = input("Enter the name of the book you want to return/donate :- ")
        if self.book in self.booklist:
            self.booklist.remove(self.book)
        else:
            self.booklist.append(self.book)
        return self.book

    def Taken(self):
        print("Books you are currently having:-")
        no = 1
        if self.booklist == []:
            print("You dont have a book in ur booklist, use request a book option to get some books")
        else:
            for i in self.booklist:
                print(f"{no}:- {i}")
                no += 1
        
VirtualLibrary = Library(["The White Tiger","Sapiens: A Brief History of Humankind","The God of Small Things","The Promise"])
student = Student()
while(True):
    print('''||======= Welcome to Virtual Library =======||
    Please choose an option:-
    1. List all the available books in the Library
    2. Check out your books
    3. Request a book
    4. Return/Donate a book
    5. Exit
    ''')

    a = int(input("Enter a choice:- "))
    if a == 1:
        VirtualLibrary.Details()
    elif a == 2:
        student.Taken()
    elif a == 3:
        VirtualLibrary.Borrow(student.Reqest())
    elif a == 4:
        VirtualLibrary.Give(student.Return())
    elif a == 5:
        print("Thanks for using Virtual Library, Have a great day ahead!")
        exit()
    else:
        print("Enter a valid option!")