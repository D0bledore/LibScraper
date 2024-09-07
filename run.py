# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


#This code is referenced from the Love Sandwiches - Essential Project
#BEGIN of ref.
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('personal_library')
#END of ref.

all_books = SHEET.worksheet('book_list')
all_books_data = all_books.get_all_values()

personal_books = SHEET.worksheet('personal_list')
personal_books_data = personal_books.get_all_values()

def search_books():

    # Update data on local system from sheet
    updated_all_books_data = all_books.get_all_values()

    # Create a dictionary to store categories and their books: title and author 
    dictionary_books = {} 

    # Initialize counter for numbered list
    indx = 0
    # Skip the header row (index 0) and Loop through book_list worksheet
    for row in updated_all_books_data[1:]:
        indx += 1
        # Assign rows to variables  
        category, title, author = row[0], row[1], row[2]

        # Creates a list variable for each category if it does not exist
        if category not in dictionary_books:
            dictionary_books[category] = []
        
        # Add book to the category's list inside Loop
        dictionary_books[category].append({
            "title": title,
            "author": author,
            "row_index": indx
        })

    # Sort keys alphabetically and assign to new variable
    categories = sorted(dictionary_books.keys())

    # This Code block will Loop until the user no longer wants to add 'take'* (*add) any books anymore from the "library" (book_list worksheet) to his personal_list worksheet
    while True: 
        print("\nBook Categories:")
        print("--------------------------")
        # Initialize counter for numbered list
        indx = 0
        # Display all categories
        for category in categories:
            indx += 1
            print(f'{indx}. {category}')
        
        print("--------------------------")

        # This Code block will Loop until valid number input for a category has been selected (or 'q' to quit)
        while True:
            category_choice = input("Enter the number of the category you want to explore (or 'q' to quit):\n").strip().lower()
            if category_choice == 'q':
                return # Exit the function
            
            # Try to convert input to integer, ValueError if not possible
            try:
                category_choice = int(category_choice)
                
                # Check if choice is within range of categories then display all books in category and wait for user input
                if 1 <= category_choice <= len(categories):
                    selected_category = categories[category_choice - 1]
  
                    # This code block will Loop until valid number input for a book has been selected (or 'q' to quit)
                    while True: 
                        # Print the name of the selected category
                        print(f"\nBooks in {selected_category}:")
                        print("--------------------------")
                        # Initialize counter for numbered list
                        indx = 0
                        # Display all books inside category list
                        for book in dictionary_books[selected_category]:
                            indx += 1
                            print(f"{indx}. {book['title']} by {book['author']}")
                        print("--------------------------")

                        book_choice = input("\nPress Enter to return to category selection (or 'q' to quit)\nEnter the number of the book you want to add:\n").strip().lower()
                        if book_choice == '':
                            break  # Exit inner Loop
                        elif book_choice == 'q':
                            return # Exit the function
                        try:
                            book_choice = int(book_choice)
                            if 1 <= book_choice <= len(dictionary_books[selected_category]):
                                selected_book = dictionary_books[selected_category][book_choice - 1]
                                # Get selected book variables
                                category = selected_category
                                title = selected_book['title']
                                author = selected_book['author']
                                # Create new row with selected book variables
                                new_row = [category, title, author]
                                personal_books.append_row(new_row)
                                print(f'"{title} by {author}" has been added to your personal list.')

                                add_another = input("Do you want to add another book? (y/n): ").strip().lower()
                                if add_another != 'y':
                                    return  # Exit the function if the user doesn't want to add another book
                            else:
                                print(f'"\n{book_choice}" is an invalid book number. Please try again.')
                        except ValueError:
                            print(f'"\n{book_choice}" is not a number. Please enter a number.')
                    break # Exit and return to category selection
                # Print this if input out of range
                else:
                    print(f'"\n{category_choice}" is an invalid category number. Please try again.')
            # If convert to integer not possible, print this
            except ValueError:
                print(f'"\n{category_choice}" is not a number. Please enter a number.')

        print("--------------------------")
    

def view_personal_list():
    print("\nYour Personal Book List:")
    print("--------------------------")

    # Update data on local system from the sheet
    updated_personal_books_data = personal_books.get_all_values()

    indx = 0
    # Skip the header row (index 0) and Loop through personal_list worksheet
    for row in updated_personal_books_data[1:]:
            # Initialize counter for numbered list
            indx += 1

            # Assign rows to variables
            title = row[1]  # Column 2 (index 1) is the title
            author = row[2]  # Column 3 (index 2) is the author
            print(f"{indx}. {title} by {author}")
    
    print("--------------------------")
    #Functionality to delete a row per desire
    while True:
        choice = input("Enter 'del' to delete a book, or press Enter to return to main menu:\n").lower().strip()
        if choice == 'del':
            while True:
                del_choice = input("Enter the number of the book you want to delete or press Enter to return:\n").strip()
                if del_choice == '':
                    return # Exit the function
                try:
                    del_index = int(del_choice)
                    if 1 <= del_index <= indx:
                        # Get row of book to be deleted
                        deleted_book = updated_personal_books_data[del_index]
                        # Get title of book to be deleted
                        deleted_title = deleted_book[1]
                        author_of_deleted_book = deleted_book[2] 
                        # Delete row from spreadsheet, which is +1 indexed
                        personal_books.delete_rows(del_index + 1)
                        print(f'Book on row {del_index}: "{deleted_title} by {author_of_deleted_book}" has been deleted.')
                        return  # Exit the function after successful deletion
                    else:
                        print(f'"\n{del_index}" is an invalid book number. Please try again.')
                except ValueError:
                    print(f'"\n{del_choice}" is not a number. Please enter a number.')
        elif choice == '':
            return  # Exit the function
        else:
            print(f'\nYou entered "{choice}", which is not a valid input!')


def display_menu():
    print("\nMenu:")
    print('---------------------------')
    print("1: Search for books")
    print("2: View personal list")
    print("3: Quit")
    print('---------------------------')

def main():
        # This function is essentially the Game Loop

    print('\nWelcome to LibScraper, developed by D0bledore')
    display_menu()
    while True:
        print("\nType 'help' to display menu.")
        choice = input("Enter your choice (1-3):\n").strip()

        if choice == '1':
            search_books()
        elif choice == '2':
            view_personal_list()
        elif choice == '3':
            print("Thank you for using the LibScraper. Goodbye!") 
            break
        elif choice.lower() == 'help':
            display_menu()
        else:
            print(f'\nYou entered "{choice}", which is invalid!')

main()