import math
from datetime import datetime
from helper import read_hr_data


def get_unique_departments(data):
    """
    Return a set of all unique department names in the dataset.
    
    Args:
        data (list): 2D list of employee records
        
    Returns:
        set: Set of department names
        
    Example:
        >>> get_unique_departments(data)
        {'engineering', 'sales', 'hr', 'marketing', 'product'}
    """
    
    depts = set()  # create a set to get the unique departments (sets remove remove duplicates automatically)
    
    for entry in data:  #The for loop looks at every employee record(entry) in the data
        depts.add(entry[1]) #add the departments(index 1) from your employee entries in the department set.
    
    return depts # Return the set of unique departments (The set removed duplicates)

def get_gender_distribution(data):
    """
    Return gender distribution (as percentages) for each department.
    
    All percentages should be rounded to 2 decimal places.
    
    Args:
        data (list): 2D list of employee records
        
    Returns:
        dict: Dictionary where each key is a department name and each value is a dictionary
              of gender percentages
        
    Example:
        >>> get_gender_distribution(data)
        {
            'engineering': {'Male': 45.5, 'Female': 35.2, 'Non-binary': 19.3},
            'sales': {'Male': 40.0, 'Female': 50.0, 'Non-binary': 10.0},
            ...
        }
    """
    #Create an empty disctionary to put your gender distributions for each department
    gender_dist = {}
    
    #Loop through each employee record(entry) in the dataset 
    for entry in data:
        # Extract the department and gender which are at index 1 and 2 respectively in each entry
        department = entry[1]
        gender = entry[2] 
        
        #Create a dictionary for the gender distribitions for the department that is not yet in the dictionary
        if department not in gender_dist:
            gender_dist[department] = {}
        
        # initialise the gender count if its not yet counted in the department
        if gender not in gender_dist[department]:
            gender_dist[department][gender] = 0
        
        # increment the gender count for the department by 1
        gender_dist[department][gender] += 1
    
    # Loop through each department in the dictionary - gender_dist
    for department in gender_dist:
        # the total count of the genders in each department is the sum of the counts of all genders in that department
        total = sum(gender_dist[department].values())
        
        # Loop through all the genders each department
        for gender in gender_dist[department]:
            # The percentage of the gender is the count of the gender divided by the total of all genders in the department multiplied by 100
            percentage = (gender_dist[department][gender] / total) * 100
            gender_dist[department][gender] = round(percentage, 2) # Round the percentage of the genders to two decimal places
    
    # return the dictionary showing the gender distribution or percetange per department
    return gender_dist


def get_avg_age_by_department(data):
    """
    Return average age for each department.
    
    All averages should be rounded to 2 decimal places.
    
    Args:
        data (list): 2D list of employee records
        
    Returns:
        dict: Dictionary where each key is a department name and each value is the average age
        
    Example:
        >>> get_avg_age_by_department(data)
        {'engineering': 38.5, 'sales': 35.2, 'hr': 42.1, 'marketing': 33.8, 'product': 36.9}
    """
    dept_ages = {} 

    for entry in data :  #collect all ages per department
        department = entry[1]
        age = entry [3]

        if department not in dept_ages:    #if department not in dictionary yet
            dept_ages [department] = []   # create an empty list for that department
        dept_ages [department].append(age) # add the age to the department's list

    avg_ages = {}   # add the age to the department's list

    for department in dept_ages:  
        ages = dept_ages [department]
        avg_ages [department] = round(sum(ages)/len(ages), 2)  # calculate and round the average age

    return avg_ages # return dictionary with average ages per department

    

def get_retention_rate(data):
    """
    Calculate overall retention rate as a percentage.
    
    Formula: (Active Employees / Total Employees) × 100
    
    Status column (index 8) contains 'Active' or 'Resigned'
    
    Result should be rounded to 2 decimal places.
    
    Args:
        data (list): 2D list of employee records
        
    Returns:
        float: Retention rate as a percentage (0-100)
        
    Example:
        >>> get_retention_rate(data)
        87.5
    """
    
    status_active = 0   #initialise the counter for active employees

    for entry in data: # loop through each employee record in the dataset
        if entry[8] == 'Active': # check the status column (index 8) for 'Active'
            status_active += 1 # increase count if employee is active
    
    total = len(data)  # get total number of employees in the dataset

    if total == 0:
        return 0
    
    retention_rate = round((status_active / total) * 100, 2) # calculate retention rate as % of active employees

    return retention_rate # return the final retention rate


def get_turnover_rate_by_department(data):
    """
    Calculate turnover rate for each department as a percentage.
    
    Formula (per department): (Resigned Employees in Department / Total Employees in Department) × 100
    
    All rates should be rounded to 2 decimal places.
    
    Args:
        data (list): 2D list of employee records
        
    Returns:
        dict: Dictionary where each key is a department name and each value is the turnover rate
        
    Example:
        >>> get_turnover_rate_by_department(data)
        {'engineering': 15.5, 'sales': 22.3, 'hr': 10.0, 'marketing': 18.5, 'product': 12.0}
    """
    dept_counts = {} # create a dictionary to store total employees and resigned employees per department 
    
    for entry in data: 
        dept = entry[1] 
        status = entry[8] 
        
        if dept not in dept_counts:# if department not in dictionary yet
            dept_counts[dept] = {'total': 0, 'resigned': 0} # create counters for total and resigned
        dept_counts[dept]['total'] += 1
        
        if status == 'Resigned':   # check if employee has resigned
            dept_counts[dept]['resigned'] += 1 # increase resigned count for that department
    
    turnover = {} 
    
    for dept, counts in dept_counts.items():
        turnover[dept] = round((counts['resigned'] / counts['total']) * 100, 2)  # calculate and round turnover rate
    
    return turnover  # return turnover rates for all departments


def get_avg_salary_by_age_range(data, min_age, max_age):
    """
    Return average salary for employees within an age range (inclusive).
    
    Result should be rounded to 2 decimal places.
    
    Args:
        data (list): 2D list of employee records
        min_age (int): Minimum age (inclusive)
        max_age (int): Maximum age (inclusive)
        
    Returns:
        float: Average salary for employees in the age range
        
    Example:
        >>> get_avg_salary_by_age_range(data, 25, 35)
        68500.75
    """ 
    total_salary = 0   # Variables to track total salary and number of employees in range
    count = 0

    for entry in data:
        age = entry[3] 
        salary = entry[4]  
 
        if min_age <= age <= max_age:  # Check if employee age falls within the given range (inclusive)
            total_salary += salary
            count += 1

    if count == 0:  # Avoid division by zero if no employees found in range
        return 0.0
    
    avg_salary = round(total_salary / count, 2)  # Calculating average salary rounded to 2 decimal places
    
    return avg_salary


def get_avg_dept_performance_by_training_range(data, min_hours, max_hours):
    """
    Return average performance rating for each department within a training hours range (inclusive).
    
    Calculates the average performance rating for employees within the specified training hours range,
    grouped by department.
    
    All ratings should be rounded to 2 decimal places.
    
    Args:
        data (list): 2D list of employee records
        min_hours (int): Minimum training hours (inclusive)
        max_hours (int): Maximum training hours (inclusive)
        
    Returns:
        dict: Dictionary where each key is a department name and each value is the average performance rating
              for employees in that department within the training hours range
        
    Example:
        >>> get_avg_dept_performance_by_training_range(data, 20, 40)
        {
            'engineering': 4.2,
            'sales': 3.9,
            'hr': 4.0,
            'marketing': 3.6,
            'product': 4.3
        }
    """
    all_departments = get_unique_departments(data)    # Get all unique departments from the dataset
    rating_totals = {}   # Dictionaries to store total ratings and counts per department
    matching_counts = {}

    for department in all_departments: # Start every department at zero so departments with no matches still appear
        rating_totals[department] = 0
        matching_counts[department] = 0

    for entry in data: 
        department = entry[1]    
        training_hours = entry[5]                        
        rating = entry[6]                               

        if min_hours <= training_hours <= max_hours:  # Only include employees whose training hours fall within the range
            rating_totals[department] += rating
            matching_counts[department] += 1

    averages = {}      # Calculate average performance rating for each department
    
    for department in all_departments:
        if matching_counts[department] == 0:   # If no employees found in range, set performance to 0
            averages[department] = 0.0
        else:
            averages[department] = round(rating_totals[department] / # Round average rating to 2 decimal places
                matching_counts[department], 2)
    
    return averages


if __name__ == "__main__":
    # Load cleaned data from CSV file
    data = read_hr_data('cleaned_dataset.csv')
    print(f"Loaded {len(data)} employee records\n")
    
    print("=" * 70)
    print("METRICS CALCULATION")
    print("=" * 70)
    
    # Test metrics functions
    # Uncomment the lines below to test each metrics function
    # You can modify the function arguments to test different inputs
    
    # 1. Get unique departments
    depts = get_unique_departments(data)
    print(f"\nUnique departments: {depts}")
    
    # 2. Get gender distribution per department
    gender_dist = get_gender_distribution(data)
    print(f"\nGender distribution by department:")
    for dept, dist in gender_dist.items():
         print(f"  {dept}: {dist}")
    
    # 3. Get average age per department
    avg_age = get_avg_age_by_department(data)
    print(f"\nAverage age by department:")
    for dept, age in avg_age.items():
        print(f"  {dept}: {age}")
    
    # 4. Get retention rate
    retention = get_retention_rate(data)
    print(f"\nOverall retention rate: {retention}%")
    
    # 5. Get turnover rate per department
    turnover = get_turnover_rate_by_department(data)
    print(f"\nTurnover rate by department:")
    for dept, rate in turnover.items():
        print(f"  {dept}: {rate}%")
    
    # 6. Get average salary for age range
    avg_sal_age = get_avg_salary_by_age_range(data, 25, 35)
    print(f"\nAverage salary for employees aged 25-35: ${avg_sal_age}")
    
    # 7. Get average department performance by training hours range
    avg_perf_training = get_avg_dept_performance_by_training_range(data, 20, 40)
    print(f"\nAverage performance rating by department for employees with 20-40 training hours:")
    for dept, rating in avg_perf_training.items():
        print(f"  {dept}: {rating}")
