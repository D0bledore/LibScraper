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
    pass

def view_personal_list():
    print("\nYour Personal Book List:")
    print("--------------------------")

    indx = 0
    # Skip the header row (index 0)
    for row in personal_books_data[1:]:
            indx += 1
            title = row[1]  # Column 2 (index 1) is the title
            author = row[2]  # Column 3 (index 2) is the author
            print(f"{indx}. {title} by {author}")
    
    print("--------------------------")

def display_menu():
    print("\nMenu:")
    print('---------------------------')
    print("1: Search for books")
    print("2: View personal list")
    print("3: Quit")
    print('---------------------------')

def main():
    '''
        This function is essentially the Game Loop
    '''
    print('\nWelcome to LibScraper, developed by D0bledore')
    display_menu()
    while True:
        print("\nType 'help' to display menu.")
        choice = input("Enter your choice (1-3):\n").strip()

        if choice == '1':
            search_books()
            print('Functionality to implemented yet')
        elif choice == '2':
            view_personal_list()
        elif choice == '3':
            print("Thank you for using the LibScraper. Goodbye!")
            break
        elif choice.lower() == 'help':
            display_menu()
        else:
            print(f'You entered "{choice}", which is invalid!')

main()