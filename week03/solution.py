# Week 3: Strings & String Methods

# --- Exercise 1 ---
def count_vowels(text):
    """
    Count the number of vowels (a, e, i, o, u) in the text. Case-insensitive.
    Example: count_vowels("Hello World") → 3
    """
    pass

# --- Exercise 2 ---
def reverse_words(sentence):
    """
    Reverse the order of words in a sentence.
    Example: reverse_words("Hello World") → "World Hello"
    Example: reverse_words("I love Python") → "Python love I"
    """
    pass

# --- Exercise 3 ---
def is_palindrome(text):
    """
    Check if text is a palindrome (reads same forwards and backwards).
    Ignore case and spaces.
    Example: is_palindrome("racecar") → True
    Example: is_palindrome("Race Car") → True
    Example: is_palindrome("hello") → False
    """
    pass

# --- Exercise 4 ---
def censor_word(text, word):
    """
    Replace all occurrences of word with asterisks of same length. Case-insensitive.
    Example: censor_word("I love cats and Cats love me", "cats") → "I love **** and **** love me"
    """
    pass

# --- Exercise 5 ---
def title_case(text):
    """
    Convert text to title case (first letter of each word capitalized).
    Do NOT use the built-in .title() method.
    Example: title_case("hello world") → "Hello World"
    Example: title_case("python is fun") → "Python Is Fun"
    """
    pass

# --- Exercise 6 ---
def extract_emails(text):
    """
    Extract all email addresses from a text string.
    An email contains @ and has text before and after it (split by spaces).
    Return a list of emails found.
    Example: extract_emails("Contact john@gmail.com or jane@yahoo.com") → ["john@gmail.com", "jane@yahoo.com"]
    """
    pass

# --- Exercise 7 ---
def pig_latin(word):
    """
    Convert a word to pig latin:
    - If starts with vowel: add "yay" to end → "apple" → "appleyay"
    - If starts with consonant: move first letter to end, add "ay" → "hello" → "ellohay"
    Example: pig_latin("apple") → "appleyay"
    Example: pig_latin("hello") → "ellohay"
    """
    pass

# --- Exercise 8 ---
def compress_string(text):
    """
    Compress a string by counting consecutive repeated characters.
    Example: compress_string("aaabbbcc") → "a3b3c2"
    Example: compress_string("abcd") → "a1b1c1d1"
    """
    pass
