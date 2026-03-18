# Week 7: Functions

# --- Exercise 1 ---
def apply_operation(a, b, operation):
    """
    Apply the given operation to a and b.
    operation is a string: "add", "subtract", "multiply", or "divide"
    For divide, return float. If dividing by zero, return "error".
    Example: apply_operation(10, 3, "add") → 13
    Example: apply_operation(10, 0, "divide") → "error"
    """
    pass

# --- Exercise 2 ---
def create_counter():
    """
    Return a list [increment, get_count] where:
    - increment() adds 1 to the count
    - get_count() returns the current count
    Use a list to store state since we haven't covered closures.
    
    Usage:
        counter = create_counter()
        counter[0]()  # increment
        counter[0]()  # increment
        counter[1]()  # returns 2
    """
    count = [0]
    def increment():
        count[0] += 1
    def get_count():
        return count[0]
    # Return the two functions — students study this pattern
    return [increment, get_count]

# --- Exercise 3 ---
def password_generator(length=12, include_upper=True, include_digits=True):
    """
    Generate a random password of given length.
    - Always include lowercase letters
    - include_upper: add uppercase letters to pool
    - include_digits: add digits to pool
    Return the password string.
    (Use import random)
    """
    pass

# --- Exercise 4 ---
def recursive_sum(lst):
    """
    Calculate the sum of a list using recursion (no loops).
    Example: recursive_sum([1, 2, 3, 4]) → 10
    Example: recursive_sum([]) → 0
    """
    pass

# --- Exercise 5 ---
def validate_data(data, rules):
    """
    Validate a dictionary against a rules dictionary.
    Rules format: {"field_name": {"type": str/int/float, "required": True/False}}
    Return a list of error messages. Empty list = valid.
    
    Example: 
        data = {"name": "Alice", "age": "twenty"}
        rules = {"name": {"type": str, "required": True}, "age": {"type": int, "required": True}}
        → ["age: expected int, got str"]
    """
    pass

# --- Exercise 6 ---
def compose_functions(func1, func2):
    """
    Return a new function that applies func1 then func2.
    Example: 
        double = lambda x: x * 2
        add_one = lambda x: x + 1
        double_then_add = compose_functions(double, add_one)
        double_then_add(5) → 11  (5*2=10, 10+1=11)
    """
    pass

# --- Exercise 7 ---
def memoize_factorial(n):
    """
    Calculate factorial using a cache dictionary for efficiency.
    Return the factorial of n.
    Example: memoize_factorial(5) → 120
    Example: memoize_factorial(0) → 1
    """
    pass

# --- Exercise 8 ---
def mini_gradebook():
    """
    Return a dictionary of functions that manage a gradebook:
    {
        "add_student": func(name) → adds student with empty grades list,
        "add_grade": func(name, grade) → adds grade to student,
        "get_average": func(name) → returns average grade,
        "get_all": func() → returns the entire gradebook dict
    }
    """
    gradebook = {}
    # Build the functions and return them
    pass
