import inquirer
import ast

# Add Variable and arrays
# tuple declare due to i dont want to change 
main_menu :tuple=["Add a book","Remove a book","Search for a book","Display all books","Display statistics","Exit"]
bookData : dict ={"book_title":None,"author":None,"publication_year":None,"genre":None,"read_or_unread":None}

# function to controll null value input by user
def error_if_empty(user_input):
    while True:
        value = input(user_input).strip()
        if value:
            return value
        print("Input cannot be empty. Please enter a valid value.")
        
def addbook():
    
 
        
    bookData["book_title"]=error_if_empty("Enter the book title: ")
    bookData["author"]=error_if_empty("Enter the author: ")
    bookData["publication_year"]=error_if_empty("Enter the publication year: ")
    bookData["genre"]=error_if_empty("Enter the genre: ")
    bookData["read_or_unread"] = inquirer.confirm(message="Have you read this book?:",)
   # bookData["read_or_unread"]=error_if_empty("Have you read this book? :")
    with open("book_file.txt","a") as file:
        file.write(str(bookData) + "\n")
    print("Book added successfully!")
    return bookData

# remove book method
def remove_book():
    Enter_book_title = error_if_empty("Enter the title of the book to remove:")
    with open("book_file.txt","r") as file:
        lines = file.readlines()
    updated_books = []
    removed =False
    for line in lines:
        book_data = eval(line)
     
        if book_data["book_title"] == Enter_book_title:
            removed =True
        else:
            updated_books.append(line)
    with open("book_file.txt","w") as file:
        file.writelines(updated_books)
        
    if removed:
        print(f"{Enter_book_title} has been removed.")
    else:
        print(f"Book '{Enter_book_title}' not found.")
        
# Search For book Method/Fucntion

def SearchforBoook():
    
    search_by = [
        inquirer.List('role', message="Please select search tye from below list",choices=['By_Title','By_Author'])
        ]
        
    
    
    search_selection = inquirer.prompt(search_by)
    print(search_selection)
    
    if search_selection['role'] == "By_Title":
        title_input =[inquirer.Text('Title',message="please Eneter Title to search By Title")]
        title =inquirer.prompt(title_input)
        search_selection.update(title)
     
        
        with open("book_file.txt","r", encoding="utf-8") as file:
            lines = file.readlines()
            for line in lines:
                book_data = ast.literal_eval(line) # ast.literal_eval(line) is used for contring string to dict
       
                if search_selection['Title'] == book_data['book_title']:
                     print("-----------Search Book Data --------------")   
                     for book_item in book_data:
                        print(f"{book_item} : {book_data[book_item]}")
                     print("------------ End --------------")  
                else:
                    print(f"Title not exist in libarary (Incorrect title {search_selection['Title']}).")     
                
        
    if search_selection['role'] == "By_Author":
        author_input =[inquirer.Text('Author',message="please Enter Author Name to Search all books by Author")]
        author = inquirer.prompt(author_input)
        search_selection.update(author)
        
        with open("book_file.txt","r") as file:
            lines = file.readlines()
            for line in lines:
                book_data = ast.literal_eval(line)
                if search_selection['Author']==book_data['author']:
                    print("-----------Search Book Data --------------")  
                    for book_item in book_data:
                        print(f"{book_item} : {book_data[book_item]}")
                    print("------------ End --------------")      
            else:
                print(f"Incorrect author name or authot not exist in library : {search_selection['Author']}")
                            
# display all books funtion
def display_all_books():
    print("------------ Show All Books--------------")
    with open("book_file.txt","r") as file:
        lines = file.readlines()
        for line in lines:
            print(line)    
                 
    print("------------ End --------------")   

# Display Statistics method

def display_statistics():
    print("------------ Display Statistics--------------")
    
    with open("book_file.txt","r") as file:
        lines = file.readlines()
        book_count=lines.__len__()
        count_read = 0
        count_unread = 0
        
        for line in lines:
            
            book_data = ast.literal_eval(line)
            if book_data["read_or_unread"] == True:
                count_read+=1
            else:
                count_unread +=1
            
        print(f"Total Number of Books are : {book_count}")
        read_percentage =count_read/book_count * 100
        print(f"Percentage of books that have been read : {read_percentage.__int__()}%")
    print("------------ End --------------") 
    
# App Title


while True:
    print("-------Personal Library Manager-------")

    for index, menu in enumerate(main_menu,start=1):
   
     print(f"{index}.  {menu}." )
    menu_choice = input("please Select A Menu from given number: ")   


    if menu_choice == "1":
        addbook()  
    if menu_choice == "2":
        remove_book()
    if menu_choice == "3":
        SearchforBoook()
    if menu_choice == "4":
        display_all_books()    
    if menu_choice=="5":
        display_statistics()
    if menu_choice =="6":
        print("your Entry Saved in data_file.txt")
        break
           
