# Week 6: Dictionaries & Sets

# --- Exercise 1 ---
def word_frequency(text):
    """
    Count the frequency of each word in the text (case-insensitive).
    Return a dictionary of word: count.
    Example: word_frequency("the cat and the dog") → {"the": 2, "cat": 1, "and": 1, "dog": 1}
    """
    pass

# --- Exercise 2 ---
def merge_dicts(dict1, dict2):
    """
    Merge two dictionaries. If a key exists in both, add the values together.
    Example: merge_dicts({"a": 1, "b": 2}, {"b": 3, "c": 4}) → {"a": 1, "b": 5, "c": 4}
    """
    pass

# --- Exercise 3 ---
def invert_dict(d):
    """
    Swap keys and values. If multiple keys have the same value, 
    store them as a list.
    Example: invert_dict({"a": 1, "b": 2, "c": 1}) → {1: ["a", "c"], 2: ["b"]}
    """
    pass

# --- Exercise 4 ---
def group_by_length(words):
    """
    Group words by their length.
    Example: group_by_length(["hi", "hey", "hello", "go", "bye"]) 
    → {2: ["hi", "go"], 3: ["hey", "bye"], 5: ["hello"]}
    """
    pass

# --- Exercise 5 ---
def phone_book(entries):
    """
    Given a list of tuples (name, number), create a phone book dictionary.
    If a name has multiple numbers, store them in a list.
    Example: phone_book([("Alice", "111"), ("Bob", "222"), ("Alice", "333")]) 
    → {"Alice": ["111", "333"], "Bob": ["222"]}
    """
    pass

# --- Exercise 6 ---
def student_rankings(scores):
    """
    Given a dict of student: score, return a list of (student, rank) tuples 
    sorted by rank (highest score = rank 1).
    Example: student_rankings({"Alice": 90, "Bob": 85, "Charlie": 95}) 
    → [("Charlie", 1), ("Alice", 2), ("Bob", 3)]
    """
    pass

# --- Exercise 7 ---
def set_operations(list1, list2):
    """
    Return a dictionary with set operations (use loops, not set built-ins):
    - "union": all unique elements from both lists
    - "intersection": elements in both lists
    - "difference": elements in list1 but not list2
    Return each as a sorted list.
    Example: set_operations([1,2,3], [2,3,4]) → {"union": [1,2,3,4], "intersection": [2,3], "difference": [1]}
    """
    pass

# --- Exercise 8 ---
def most_common(lst, n):
    """
    Return the n most common elements as a list of (element, count) tuples.
    Sorted by count descending.
    Example: most_common(["a","b","a","c","b","a"], 2) → [("a", 3), ("b", 2)]
    """
    pass
