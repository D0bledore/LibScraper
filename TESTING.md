# Testing

> [!NOTE]  
> Return back to the [README.md](README.md) file.

## Code Validation

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| Directory | File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
|  | run.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/D0bledore/LibScraper/main/run.py) | ![screenshot](documentation/validation/ci_py_linter.png) | No Errors |

## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

- [Ungoogled Chrome](https://github.com/ungoogled-software/ungoogled-chromium)
- [Firefox](https://www.mozilla.org/en-US/firefox/download/thanks/)
- [Brave](https://brave.com/download)
- [Opera](https://www.opera.com/download)


| Browser | Home | Search | View | Add | Delete | Quit | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Ungoogled Chrome | ![screenshot](documentation/browsers/browser-chrome-home.png) | ![screenshot](documentation/browsers/browser-chrome-search.png) | ![screenshot](documentation/browsers/browser-chrome-view.png) | ![screenshot](documentation/browsers/browser-chrome-add.png) | ![screenshot](documentation/browsers/browser-chrome-delete.png) | ![screenshot](documentation/browsers/browser-chrome-quit.png) | Works as expected |
| Firefox | ![screenshot](documentation/browsers/browser-firefox-home.png) | ![screenshot](documentation/browsers/browser-firefox-search.png) | ![screenshot](documentation/browsers/browser-firefox-view.png) | ![screenshot](documentation/browsers/browser-firefox-add.png) | ![screenshot](documentation/browsers/browser-firefox-delete.png) | ![screenshot](documentation/browsers/browser-firefox-quit.png) | Works as expected |
| Brave | ![screenshot](documentation/browsers/browser-brave-home.png) | ![screenshot](documentation/browsers/browser-brave-search.png) | ![screenshot](documentation/browsers/browser-brave-view.png) | ![screenshot](documentation/browsers/browser-brave-add.png) | ![screenshot](documentation/browsers/browser-brave-delete.png) | ![screenshot](documentation/browsers/browser-brave-quit.png) | Works as expected |
| Opera | ![screenshot](documentation/browsers/browser-opera-home.png) | ![screenshot](documentation/browsers/browser-opera-search.png) | ![screenshot](documentation/browsers/browser-opera-view.png) | ![screenshot](documentation/browsers/browser-opera-add.png) | ![screenshot](documentation/browsers/browser-opera-delete.png) | ![screenshot](documentation/browsers/browser-opera-quit.png) | Works as expected |

## Defensive Programming

This section illustrates the robust input validation mechanisms implemented in my program. The system is designed to provide clear guidance to users regarding available options while strictly enforcing input constraints.

My validation technique effectively handles both type checking (ensuring the input is a number or a valid option) and range checking (ensuring the number corresponds to an existing book). My code also provides clear feedback to the user in case of errors and confirms successful operations. My approach contributes to a robust and user-friendly interface for managing the personal book list.

| Place of occurence |Int validation | String validation |
| --- | --- | --- | 
| Home | ![screenshot](documentation/defensive/home_invalid_int.png) | ![screenshot](documentation/defensive/home_invalid_string.png) |
| Category select | ![screenshot](documentation/defensive/search_cat_invalid_int.png) | ![screenshot](documentation/defensive/search_cat_invalid_string.png) |
| Book select | ![screenshot](documentation/defensive/search_book_invalid_int.png) | ![screenshot](documentation/defensive/search_book_invalid_string.png) |
| Add another book? | ![screenshot](documentation/defensive/add_book_invalid_int.png) | ![screenshot](documentation/defensive/add_book_invalid_string.png) |
| Viewing personal list | ![screenshot](documentation/defensive/view_invalid_int.png) | ![screenshot](documentation/defensive/view_invalid_string.png) |
| Deleting | ![screenshot](documentation/defensive/del_book_invalid_int.png) | ![screenshot](documentation/defensive/del_book_invalid_string.png) |

**No Book to delete**

If the personal list is empty, the program will detect this condition, inform the user, and return them to the home menu without presenting any other options.

![screenshot](documentation/defensive/list_empty.png)

## Bugs

1. **Infinite Loop After Failed Deletion Attempt**

**Issue**: The program was stuck in a loop that continued even after a rejected or failed deletion attempt.

![screenshot](documentation/bugs/stuck_in_loop.png)

**Solution**: A break statement was added to exit the loop when a deletion fails, preventing an infinite loop scenario. 


2. **Preventing Deletion from Empty Personal List**

**Issue**: Users could attempt to delete books from an empty personal list, leading to confusion.

![screenshot](documentation/bugs/prevent_delete_empty.png)

**Solution**: The functionality for viewing the personal list and deleting a book was separated. The view_personal_list function now returns a boolean value indicating whether the list contains entries. This value is checked before allowing deletion, ensuring users can't attempt to delete from an empty list and preventing potential confusion. 

3. **Preventing Duplicate Entries**

**Issue**: The personal list worksheet could contain duplicate book entries, which was contrary to the program's purpose.

![screenshot](documentation/bugs/prevent_duplicates.png)

**Solution**: A helper function was implemented to compare the title and author of a selected book against all books already in the personal list. If a match is found, the function returns True, skipping the addition process and notifying the user. This prevents duplicate entries and maintains the integrity of the personal list.

![screenshot](documentation/bugs/prevent_duplicate_succesful.png) 




4. **'q' Not Exiting Category Selection**

**Issue**: The 'q' option failed to exit the user from the category selection process as intended.

![screenshot](documentation/bugs/q_returns_function_does_not_break_loop.png)
![screenshot](documentation/bugs/q_does_not_quit.png)

**Solution**: The input validation for the 'q' option was moved from within the function to the outer loop where the function is called. This ensures that selecting 'q' breaks the entire selection process, not just the function, allowing users to exit as expected.

![screenshot](documentation/bugs/q_to_quit.png)

5. **F-string Functionality Lost in Multi-line Print Statement**

**Issue**: The f-string functionality was lost when using multiple lines for a print statement.

    ![screenshot](documentation/bugs/f_string_on_new_line_code.png)

    ![screenshot](documentation/bugs/f_string_on_new_line.png)

**Solution**: The 'f' prefix was added to each line of the multi-line print statement. This ensures that all lines are properly interpreted as f-strings, maintaining the intended string formatting throughout the statement. 


6. **Python `E501 line too long` (80 > 79 characters)**

![screenshot](documentation/bugs/e501_error.png)

**Issue**: The Python linter reported E501 errors for lines exceeding 79 characters.

**Solution**: The line length was reduced, and parentheses were used to continue lines where necessary. This adjustment adheres to PEP 8 style guidelines, improving code readability while maintaining functionality.

![screenshot](documentation/bugs/e501_error_fix.png)




## Unfixed Bugs

> [!NOTE]  
> There are no remaining bugs that I am aware of.
