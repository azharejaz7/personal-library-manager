from colorama import Fore, Style
# Add Variable and arrays
# tuple declare due to i dont want to change 
main_menu :tuple=["Add a book","Remove a book","Search for a book","Display all books","Display statistics","Exit"]
bookData : dict ={"book_title":None,"author":None,"publication_year":None,"genre":None,"read_or_unread":None}
def error_if_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty. Please enter a valid value.")
        
def addbook():
    
 
        
    bookData["book_title"]=error_if_empty("Enter the book title:")
    bookData["author"]=error_if_empty("Enter the author:")
    bookData["publication_year"]=error_if_empty("Enter the publication year:")
    bookData["genre"]=error_if_empty("Enter the genre:")
    bookData["read_or_unread"]=error_if_empty("Have you read this book? (yes/no) :")
    with open("book_file.txt","a") as file:
        file.write(str(bookData) + "\n")
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
        
    
        
           
# App Title
print("Personal Library Manager")

for index, menu in enumerate(main_menu,start=1):
   
    print(f"{index}.  {menu}." )


menu_choice = input("please Select A Menu from given number: ")   


if menu_choice == "1":
    addbook()
    print("Book added successfully!")
    
if menu_choice == "2":
    remove_book()
    
        
