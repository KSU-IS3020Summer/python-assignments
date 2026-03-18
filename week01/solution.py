# Week 1: Variables, Data Types & Input/Output
# Complete each function below.

# --- Exercise 1 ---
# Create variables for a student profile and return them as a formatted string.
def student_profile():
    """
    Create the following variables:
    - name (str): your first name
    - age (int): your age
    - gpa (float): a GPA like 3.5
    - is_fulltime (bool): True or False
    
    Return a string: "Name: [name], Age: [age], GPA: [gpa], Full-time: [is_fulltime]"
    """
    # Write your code below:
    pass


# --- Exercise 2 ---
def celsius_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.
    Formula: F = C * 9/5 + 32
    Return the result as a float.
    
    Example: celsius_to_fahrenheit(0) → 32.0
    Example: celsius_to_fahrenheit(100) → 212.0
    """
    # Write your code below:
    pass


# --- Exercise 3 ---
def calculate_total(price, quantity, tax_rate):
    """
    Calculate the total cost with tax.
    Formula: total = price * quantity * (1 + tax_rate)
    Return the total rounded to 2 decimal places.
    
    Example: calculate_total(10.00, 3, 0.08) → 32.40
    """
    # Write your code below:
    pass


# --- Exercise 4 ---
def swap_values(a, b):
    """
    Swap the values of a and b.
    Return them as a tuple (b, a).
    
    Example: swap_values(1, 2) → (2, 1)
    Example: swap_values("hello", "world") → ("world", "hello")
    """
    # Write your code below:
    pass


# --- Exercise 5 ---
def string_info(text):
    """
    Given a string, return a dictionary with:
    - "length": the number of characters
    - "upper": the string in uppercase
    - "lower": the string in lowercase
    - "first": the first character
    - "last": the last character
    
    Example: string_info("Hello") → {"length": 5, "upper": "HELLO", "lower": "hello", "first": "H", "last": "o"}
    """
    # Write your code below:
    pass


# --- Exercise 6 ---
def number_types(value):
    """
    Given a numeric string (e.g., "42" or "3.14"), return a dictionary with:
    - "original": the original string
    - "as_int": the value converted to int (round down for floats)
    - "as_float": the value converted to float
    - "type": "integer" if the string has no decimal point, "decimal" if it does
    
    Example: number_types("42") → {"original": "42", "as_int": 42, "as_float": 42.0, "type": "integer"}
    Example: number_types("3.14") → {"original": "3.14", "as_int": 3, "as_float": 3.14, "type": "decimal"}
    """
    # Write your code below:
    pass


# --- Exercise 7 ---
def mad_libs(noun, verb, adjective, place):
    """
    Create a mad libs sentence using f-strings.
    Return: "The [adjective] [noun] decided to [verb] at the [place]."
    
    Example: mad_libs("cat", "dance", "purple", "library")
    → "The purple cat decided to dance at the library."
    """
    # Write your code below:
    pass


# --- Exercise 8 ---
def split_bill(total, num_people, tip_percent):
    """
    Calculate how much each person pays when splitting a bill with tip.
    Formula: each_pays = total * (1 + tip_percent / 100) / num_people
    Return the amount each person pays, rounded to 2 decimal places.
    
    Example: split_bill(100, 4, 20) → 30.00
    """
    # Write your code below:
    pass
