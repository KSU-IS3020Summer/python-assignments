# Week 8: File I/O & Error Handling

# --- Exercise 1 ---
def count_lines(filename):
    """
    Count the number of non-empty lines in a file.
    If file doesn't exist, return -1.
    Example: count_lines("sample.txt") → 5
    """
    pass

# --- Exercise 2 ---
def find_in_file(filename, search_term):
    """
    Search for a term in a file. Return list of (line_number, line_text) tuples 
    where the term appears (case-insensitive). Line numbers start at 1.
    If file doesn't exist, return empty list.
    Example: find_in_file("sample.txt", "python") → [(3, "Python is great")]
    """
    pass

# --- Exercise 3 ---
def write_report(filename, data):
    """
    Write a report file from a list of dictionaries.
    Each dict has "name" and "score" keys.
    Format: one student per line as "name: score"
    Last line: "Average: X.X"
    
    Example data: [{"name": "Alice", "score": 90}, {"name": "Bob", "score": 80}]
    File content:
        Alice: 90
        Bob: 80
        Average: 85.0
    """
    pass

# --- Exercise 4 ---
def safe_divide(a, b):
    """
    Divide a by b with error handling.
    Return the result as a float.
    If b is 0, return "Cannot divide by zero"
    If a or b is not a number, return "Invalid input"
    
    Example: safe_divide(10, 3) → 3.333...
    Example: safe_divide(10, 0) → "Cannot divide by zero"
    Example: safe_divide("abc", 2) → "Invalid input"
    """
    pass

# --- Exercise 5 ---
def parse_csv_string(csv_text):
    """
    Parse a CSV-formatted string (not a file) into a list of dictionaries.
    First line is the header.
    
    Example: parse_csv_string("name,age,city\\nAlice,30,NYC\\nBob,25,LA")
    → [{"name": "Alice", "age": "30", "city": "NYC"}, 
       {"name": "Bob", "age": "25", "city": "LA"}]
    """
    pass

# --- Exercise 6 ---
def log_message(filename, message, level="INFO"):
    """
    Append a log entry to a file in format: "[LEVEL] message"
    Create the file if it doesn't exist.
    
    Example: log_message("app.log", "Server started", "INFO")
    Appends: "[INFO] Server started\n"
    """
    pass

# --- Exercise 7 ---
def merge_files(file_list, output_file):
    """
    Merge multiple text files into one output file.
    Add a separator "--- filename ---" before each file's content.
    Skip files that don't exist (don't crash).
    Return the number of files successfully merged.
    """
    pass

# --- Exercise 8 ---
def word_count_file(filename):
    """
    Read a file and return a dictionary of word: count (case-insensitive).
    Strip punctuation (.,!?;:) from words.
    If file doesn't exist, return empty dict.
    
    Example file content: "Hello, hello! World."
    → {"hello": 2, "world": 1}
    """
    pass
