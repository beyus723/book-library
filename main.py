#Task 1

#Initial Menu system with the following options:

print("Welcome in our Library.\n")


class Books:
  book1 = {"Elo przyjacielu" : ["Borys Owsik"]}
  
  book2 = {"Borys przy zlamaniu" : ["Borys Owsik"]}
  
  book3 = {"Borys w natarciu" : ["Borys Owsik"]}
  
  book4 = {"Borys Rudy Zyd" : ["Borys Owsik"]}

  def book(title, author):
    title.book1 = book1[0]
    print()

    
                               
while True:
  print("""1. Library Books
        \n2. Borrow a Book dziwko
        \n3. Return a Book elomala
        \n4. Exit""")

  choice = input("\nPlease choose one of the following options: ")
      
  if choice == "1":
    print("\n", book , "\n")

    
  elif choice == "2":
    borrow_book()
  elif choice == "3":
    return_book()
  elif choice == "4":
    print("\nExiting program.")
    break
  else:
    print("\nInvalid choice. Try again.")




#Task 1a

#Make sure your menu is looped until the user selects to exit the program. Comment your code as you go. And you must use appropriate naming conventions for your variables.


""" 
Library Management System

You will be developing a Library management system, allowing users to borrow and return books from a library.

Task 1

Initial Menu system with the following options:

1. View Library Books

2. Borrow a Book

3. Return a Book

4. Exit

Task 1a

Make sure your menu is looped until the user selects to exit the program. Comment your code as you go. And you must use appropriate naming conventions for your variables.

Task 2

Code the view library Function. The system will need to store a minimum of 10 books in a dictionary using the author as the key and the name of the book as the value. In this function you will need to display the full list of the books by author in an ordered list on screen for the user.

Task 2a

The view function will also need to show the number of books currently available – you will need to work out how you will assign this value to each book.

Task 3

Code the borrow function for each book available. The screen should display the list of available books to borrow and the number remaining in stock. The user should then be able to select the book they wish to borrow and remove 1 from the list number of books in stock.

Task 3a

Include the option for the user to borrow more than one book.

Task 4

Code the return function for each book. The screen must display all books expected to be in the library regardless of if all books have been borrowed (some will show zero in stock). The user will then be able to select the book they wish to return. Adding one to the number in stock once processed.

Task 4a

Include the option for the user to return more than one book.

"""