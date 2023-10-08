
allBooks = [
                ['9780596007126',"The Earth Inside Out","Mike B",2,['Ali'],True],
                ['9780134494166',"The Human Body","Dave R",1,[],False],
                ['9780321125217',"Human on Earth","Jordan P",1,['David','b1','user123'],True],
           ]


def print_menu():
    print('\n######################')
    print('1: (A)dd a new book.')
    print('2: Bo(r)row books.')
    print('3: Re(t)urn a book.')
    print('4: (L)ist all books.')
    print('5: E(x)it.')
    print('######################\n')

def search_modes(name,term):
    # contains
    book = 0
    if term.find('*') != -1:
        substring = ''
        # first find the sub-string user wants to search for
        for i in range(term.find('*')):
            substring += term[i]
        # search for books with the substring
        substring = substring.lower()
        for j in range(len(allBooks)):
            if ((allBooks[j])[1].lower()).find(substring) != -1 and (allBooks[j])[5] == False:
                print("- " + (allBooks[j])[1] + " is borrowed!")
                (allBooks[j])[4].append(name)
                book += 1
        if book < 1:
            print("No books found!")


    # starts with
    elif term.find('%') != -1:
        substring = ''
        # again find the sub-string user wants to search for
        for i in range(term.find('%')):
            substring += term[i]
        substring = substring.lower()

        for j in range(len(allBooks)):
            # search for the word in the beginning of the book name
            if (((allBooks[j])[1].lower()).find(substring,0,len(substring))) != -1 and (allBooks[j])[5] == False:
                print("- " + (allBooks[j])[1] + " is borrowed!")
                (allBooks[j])[4].append(name)
                book += 1
        if book < 1:
            print("No books found!")

    # exact method
    else:

        for i in range(len(allBooks)):
            if term.lower() == (allBooks[i])[1].lower() and (allBooks[i])[5] == False:
                print(("- " + (allBooks[i])[1] + " is borrowed!"))
                (allBooks[i])[4].append(name)
                book += 1
        if book < 1:
            print("No books found!")





def add():
    # function to add books

    # gather and validate user input for book name
    not_valid = True
    book_name = input("Book Name>")
    # SEE IF WE CAN MAKE FUNCION TO DO THIS
    while not_valid:
        # while inputted strings contain % or * continuously ask user for book name
        if book_name.find('*') != -1 or book_name.find('%') != -1:
            print('Invalid book name!')
            book_name = input("Book Name>")
        else:
            # else break
            break
    author = input("Author Name>")
    edition = input("Edition>")
    while not_valid:
        try:
            int(edition)
        except ValueError:
            print("Please enter a valid edition")
            edition = input("Edition>")
        else:
            break


    ISBN = (input("ISBN>"))

    # validate the ISBN
    sum = 0
    while not_valid:
        # check if ISBN is valid integer
        while isinstance(ISBN,str) == False or len(ISBN) != 13:
            print("Invalid ISBN!")
            ISBN = input("ISBN>")

        # calculate ISBN value
        for i in range(len(ISBN)):
            # if i is odd, multiply digit by 1 else if 3 is even multiply digit by 3
            if i % 2 == 0:
                sum += int(ISBN[i]) * 1
            else:
                sum += int(ISBN[i]) * 3
        # check if sum is multiple of 10
        if sum % 10 != 0:
            print("Invalid ISBN!")
            ISBN = input("ISBN>")
        else:
            break

    # finally check if ISBN already exists
    for i in range(len(allBooks)-1):
        if (allBooks[i])[0] == ISBN:
            return True

    # Insert into new books assuming no dublicate
    allBooks.append([ISBN,book_name,author,edition,[''],False])

    # closing statement
    print("\nA new book is added successfully.")

def borrow():
    # ask name of borrower
    name = input("Enter the borrower name>")
    search_term = input("Search term>")
    search_modes(name,search_term)



def return_books():
    # function to return books
    ISBN = int(input("ISBN>"))
    for i in range(len(allBooks)):
        if (allBooks[i])[0] != ISBN:
            print("No book is found!")
        else:
            (allBooks[i])[5] = False
            print((allBooks[i])[1] + " is returned.")

def list_book():
    # function that lists all books
    for i in range(len(allBooks)):
        print("---------------\n")
        if (allBooks[i])[5] == False:
            print("[Available]\n")
        else:
            print("[Unavailable]\n")
        print((allBooks[i])[1] + " - " + (allBooks[i])[2])
        print("\nE: " + str((allBooks[i])[3]) + " " + "ISBN: " + (allBooks[i])[0])
        print("\nBorrowed by: ",end="")
        print((allBooks[i])[4])
def start():
    exit = True
    while exit:
        print_menu()
        action = input("Your Selection> ")
        if action == "1" or action.lower() == "a":
            add()
        elif action == "2" or action.lower() == "r":
            borrow()
        elif action == "3" or action.lower() == "t":
            return_books()
        elif action == "4" or action.lower() == "l":
            list_book()
        elif action == "5" or action.lower() == "x":
            print("$$$$$$$$ FINAL LIST OF BOOKS $$$$$$$$")
            list_book()
            exit()


start()

