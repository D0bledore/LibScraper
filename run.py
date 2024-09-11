# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import os

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


#Helper function to clean-up the terminal so things don't get messy ref: https://www.geeksforgeeks.org/clear-screen-python/
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Helper function to check if book exists before adding
def book_exists_in_personal_list(title, author):
    personal_books_data = personal_books.get_all_values()
    for row in personal_books_data[1:]:  # Skip header row
        if row[1].lower() == title.lower() and row[2].lower() == author.lower():
            return True
    return False

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

    # This Code block will Loop until the user no longer wants to take any books from the "library" (book_list worksheet) anymore and add it to his personal_list worksheet
    while True: 
        print("\nBook Categories:")
        print("--------------------------")
        # Initialize counter for numbered list
        indx = 0
        # Displays all categories
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
                
                # Check if choice is within range of categories then display all books within that category
                if 1 <= category_choice <= len(categories):
                    selected_category = categories[category_choice - 1]
  
                    # Print the name of the selected category
                    print(f"\nBooks in {selected_category}:")
                    print("--------------------------")
                    # Initialize counter for numbered list
                    indx = 0
                    # Display all books inside selected category list
                    for book in dictionary_books[selected_category]:
                        indx += 1
                        print(f"{indx}. {book['title']} by {book['author']}")
                    print("--------------------------")
                    # This code block will Loop until valid number input for a book has been selected (or 'q' to quit)
                    while True: 

                        book_choice = input("\nOptions:\n- [Enter] for more categories\n- [q] to quit\n\nType the number of the book to add:\n").strip().lower()
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

                                #Helper function to prevent duplicates
                                if book_exists_in_personal_list(title, author):
                                    print(f"-----------------------------------------\n{title} by {author}\n-----------------------------------------\nis already in your personal list.")
                                else:
                                    # Create new row with selected book variables
                                    new_row = [category, title, author]
                                    personal_books.append_row(new_row)
                                    print(f'-----------------------------------------\n{title} by {author}\n-----------------------------------------\nhas been added to your personal list.')

                                add_another = input("\nIf you'd like to add another book, simply enter 'y'!\n").strip().lower()
                                if add_another != 'y':
                                    return  # Exit the function if the user doesn't want to add another book
                            else:
                                print(f'\n"{book_choice}" is an invalid book number. Please try again.')
                        except ValueError:
                            print(f'\n"{book_choice}" is not a number. Please enter a number.')
                    break # Exit and return to category selection
                # Print this if input out of range
                else:
                    print(f'\n"{category_choice}" is an invalid category number. Please try again.')
            # If convert to integer not possible, print this
            except ValueError:
                print(f'\n"{category_choice}" is not a number. Please enter a number.')

        print("--------------------------")
    
# Function to update and see current personal_list worksheet 
def view_personal_list():
    print("\nYour Personal Book List:")
    print("--------------------------")

    # Update data on local system from the sheet
    global updated_personal_books_data
    updated_personal_books_data = personal_books.get_all_values()
    
    # Initialize counter for numbered list        
    indx = 0
    empty_list = True  # Flag to check if the entire personal list is empty

    # Skip the header row (index 0) and Loop through personal_list worksheet
    for row in updated_personal_books_data[1:]:
        # Check if the title (second column) is empty
        if row[1].strip() == '':
            continue  # Skip this row if title is empty

        # If we reach here, we have a non-empty title
        empty_list = False
        # Initialize counter for numbered list        
        indx += 1

        title = row[1]  # Column 2 (index 1) is the title
        author = row[2]  # Column 3 (index 2) is the author
        print(f"{indx}. {title} by {author}")
  
    print("--------------------------")

    return empty_list

# Functionality to delete a book entry from the personal_list worksheet
def delete_book():
    while True:
        del_choice = input("\nPlease enter the number of the book you want to delete \npress Enter to exit:\n").strip()
        if del_choice == '':
            return # Exit the function
        try:
            del_index = int(del_choice)
            if 1 <= del_index <= len(updated_personal_books_data) - 1:

                # Get book data at the specified index
                deleted_book = updated_personal_books_data[del_index]

                # Get title and author of book to be deleted
                deleted_title = deleted_book[1]
                author_of_deleted_book = deleted_book[2] 

                # Delete row from spreadsheet, which is +1 indexed
                personal_books.delete_rows(del_index + 1)
                print(f'Book on row {del_index}: "{deleted_title} by {author_of_deleted_book}" has been deleted.')
                return True 
            else:
                print(f'\n"{del_index}" is an invalid book number. Please try again.')
        except ValueError:
            print(f'\n"{del_choice}" is not a number. Please enter a number.')


def display_menu():
    print("\nOptions:")
    print('---------------------------')
    print("1: Search for books in library")
    print("2: View personal list")
    print("3: Quit")
    print('---------------------------')

def main():
        # This function is essentially the Game Loop
    print('\nWelcome to LibScraper, developed by D0bledore')
    display_menu()
    while True:
        print("------")
        print(" HOME:")
        print("------")
        print("\nType 'help' to display options.")
        choice = input("Enter your choice (1-3):\n").strip()

        if choice == '1':
            search_books()
        elif choice == '2':
            while True:
                empty_list = view_personal_list()
                if empty_list:
                    print("Personal book list is empty. Exiting...")
                    break # Return home 

                choice = input("\nIf you want to delete a book, enter 'd':\n").lower().strip()
                if choice == 'd':
                    deleted = delete_book() #returns True when deletion successful
                    if deleted: 
                        continue  # Refresh personal_list and repeat input so user can decide to delete another book
                else:
                    break  # Exit the program
        elif choice == '3':
            print("----------------------------------------------")
            print("Thank you for using the LibScraper. Goodbye!")
            print("----------------------------------------------")
            break
        elif choice.lower() == 'help':
            display_menu()
        else:
            print(f'\nYou entered "{choice}", which is not a valid option!')


main()