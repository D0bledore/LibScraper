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

def display_menu():
    print("\nMenu:")
    print('---------------------------')
    print("1: Search for books")
    print("2: View personal list")
    print("3: Quit")
    print('---------------------------')
