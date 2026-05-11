import math
from datetime import datetime
from helper import read_hr_data


def remove_null_salaries(data):
    """
    Remove all records where Salary (index 4) is NaN or missing.
    
    Modifies the data list in place. Returns the list of removed entries.
    
    Args:
        data (list): 2D list of employee records
        
    Returns:
        list: List of removed employee records
    """
    #List that will store the list without invalid entries
    cleaned_data =[]

    for entry in data:
        salary = entry[4]# get the salary, which is the fourth element in each entry(employee record)
    
        if salary == float('nan') or salary == '' or salary != salary: # checks if salary is missing or where salary is NaN
            continue #skip entries with invalid salaries ( missing or NaN)
        else:
            cleaned_data.append(entry) #add the entries with valid salaries to the cleaned_data list

    return cleaned_data #returns cleaned_data list which is the dataset without invalid entries    

def standardize_departments(data):
    """
    Convert all Department names (index 1) to lowercase.
    
    Modifies the data list in place. Returns nothing.
    
    Args:
        data (list): 2D list of employee records
    """
    # Loop through each entry(employee record) in the data
    for entry in data:
        entry[1] = entry[1].lower() #get the department, which is the first element in each entry(employee record) and use lower() to convert it to lowercase
    
    pass # return nothing

def remove_invalid_performance_ratings(data):
    """
    Remove records with Performance_Rating (index 6) outside range [0, 5].
    
    Modifies the data list in place. Returns the list of removed entries.
    
    Args:
        data (list): 2D list of employee records
        
    Returns:
        list: List of removed employee records
    """
    cleaned_data = [] # new list to store the data set without invalid performance ratings

    for entry in data:
        perform_rating = entry[6] #performance rating is the 6th element in each entry(employee record)
        
        #skip the enteries where the condition that checks if the performance entry is less
        # than 0 or more than 5 or is not a number is true and add the entries where the 
        # condition is false to the cleaned_data list
        if perform_rating < 0 or perform_rating > 5  or perform_rating == float('nan'):
            continue
        else:
            cleaned_data.append(entry)
    
    return cleaned_data



def fix_format_dates(data):
    """
    Fix the formatting of hire dates that are not in YYYY-MM-DD format.
    
    Some dates may be in DD/MM/YYYY format; convert these to YYYY-MM-DD.
    Expected format: YYYY-MM-DD
    
    Modifies the data list in place. Returns nothing.
    
    Args:
        data (list): 2D list of employee records
    """
    for entry in data:
        date_entry = entry[9] # get the hire date, which is the 10th element in each entry (employee record)

        if date_entry.count('/') == 2:# checks if the date is in DD/MM/YYYY format (contains two '/')
            day, month, year = date_entry.split('/') # split the date into day, month, and year
            entry[9] = f"{year}-{month}-{day}" # rearrange into YYYY-MM-DD format and update the entry
        else:
            pass # do nothing if the date is already in the correct format


def remove_invalid_dates(data):
    """
    Remove records with invalid hire dates.
    
    Removes entries where:
    - The year is before 2015 (company was founded in 2015)
    - The year is after 2025 (future dates beyond company scope)
    - The date is logically invalid:
      - Days less than 1 or greater than 30
      - For February: check leap year (29 days in leap years, 28 otherwise)
      - Months less than 1 or greater than 12
    
    Modifies the data list in place. Returns the list of removed entries.
    
    Args:
        data (list): 2D list of employee records
        
    Returns:
        list: List of removed employee records
    """
    cleaned_data = []  # list that will store entries with valid dates
    
    for entry in data:
        date_entry = entry[9] # get the hire date, which is the 10th element in each entry (employee record)

        year,month,day = date_entry.split("-") # split the date into year, month, and day
        year, month, day = int(year), int(month), int(day) # convert year, month, and day into integers for comparison



        if year < 2015 or year > 2025:  # check if year is outside valid company range before 2015 or after 2025
            continue # skip entries with invalid year
            
        if month < 1 or month > 12: # check if month is outside valid range (1–12)
            continue # skip entries with invalid month

        if month == 2:
            # Leap year logic
            leap = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
            max_day = 29 if leap else 28 # set max days for February depending on leap year
        elif month in [4, 6, 9, 11]:
            max_day = 30
        else:
            max_day = 31

        if day < 1 or day > max_day: # check if day is outside valid range for that month
            continue  # check if day is outside valid range for that month
        
        cleaned_data.append(entry)  # check if day is outside valid range for that month
    
    return cleaned_data # return dataset without invalid date entries


if __name__ == "__main__":
    # Load uncleaned data from CSV file
    data = read_hr_data('uncleaned_dataset.csv')
    print(f"Loaded {len(data)} employee records\n")
    
    print("=" * 70)
    print("DATA CLEANING")
    print("=" * 70)
    
    # Test data cleaning functions
    # Uncomment the lines below to test each cleaning function
    # You can modify the function arguments to test different inputs
    
    # 1. Remove null salaries
    removed_salaries = remove_null_salaries(data)
    print(f"Removed {len(removed_salaries)} records with null salaries")
    print(f"Remaining records: {len(data)}\n")
    
    # 2. Standardize departments
    standardize_departments(data)
    print("Standardized department names to lowercase\n")
    
    # 3. Remove invalid performance ratings
    removed_ratings = remove_invalid_performance_ratings(data)
    print(f"Removed {len(removed_ratings)} records with invalid performance ratings")
    print(f"Remaining records: {len(data)}\n")
    
    # 4. Fix hire date formatting
    fix_format_dates(data)
    print("Fixed hire date formatting\n")
    
    # 5. Remove invalid dates
    removed_dates = remove_invalid_dates(data)
    print(f"Removed {len(removed_dates)} records with invalid dates")
    print(f"Remaining records: {len(data)}\n")
