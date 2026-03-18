# Week 2: Operators & Conditionals

# --- Exercise 1 ---
def grade_letter(score):
    """
    Return the letter grade for a numeric score.
    A: 90-100, B: 80-89, C: 70-79, D: 60-69, F: below 60
    
    Example: grade_letter(95) → "A"
    Example: grade_letter(73) → "C"
    """
    pass


# --- Exercise 2 ---
def is_leap_year(year):
    """
    Return True if the year is a leap year, False otherwise.
    Rules: divisible by 4, BUT not by 100, UNLESS also divisible by 400.
    
    Example: is_leap_year(2024) → True
    Example: is_leap_year(1900) → False
    Example: is_leap_year(2000) → True
    """
    pass


# --- Exercise 3 ---
def ticket_price(age, is_student):
    """
    Calculate movie ticket price:
    - Children (under 12): $8
    - Seniors (65+): $10
    - Students (any age, is_student=True): $11
    - Regular adults: $15
    Check in this order: child → senior → student → regular
    
    Example: ticket_price(10, False) → 8
    Example: ticket_price(70, False) → 10
    Example: ticket_price(20, True) → 11
    """
    pass


# --- Exercise 4 ---
def bmi_category(weight_kg, height_m):
    """
    Calculate BMI and return the category.
    BMI = weight_kg / (height_m ** 2)
    Categories: "Underweight" (<18.5), "Normal" (18.5-24.9), 
                "Overweight" (25-29.9), "Obese" (30+)
    
    Example: bmi_category(70, 1.75) → "Normal"
    """
    pass


# --- Exercise 5 ---
def fizzbuzz(n):
    """
    Classic FizzBuzz:
    - Return "FizzBuzz" if n is divisible by both 3 and 5
    - Return "Fizz" if divisible by 3 only
    - Return "Buzz" if divisible by 5 only
    - Return the number as a string otherwise
    
    Example: fizzbuzz(15) → "FizzBuzz"
    Example: fizzbuzz(9) → "Fizz"
    Example: fizzbuzz(7) → "7"
    """
    pass


# --- Exercise 6 ---
def triangle_type(a, b, c):
    """
    Given three side lengths, determine the triangle type.
    First check if it's a valid triangle (sum of any two sides > third side).
    Return: "equilateral" (all equal), "isosceles" (two equal), 
            "scalene" (none equal), or "invalid"
    
    Example: triangle_type(3, 3, 3) → "equilateral"
    Example: triangle_type(3, 4, 5) → "scalene"
    Example: triangle_type(1, 1, 10) → "invalid"
    """
    pass


# --- Exercise 7 ---
def password_strength(password):
    """
    Check password strength. Return "weak", "medium", or "strong".
    - Weak: less than 8 characters
    - Medium: 8+ characters but missing uppercase, lowercase, or digit
    - Strong: 8+ characters with at least one uppercase, one lowercase, and one digit
    
    Example: password_strength("abc") → "weak"
    Example: password_strength("abcdefgh") → "medium"
    Example: password_strength("Abcdef1x") → "strong"
    """
    pass


# --- Exercise 8 ---
def number_classifier(n):
    """
    Return a string describing the number:
    - "positive even", "positive odd", "negative even", "negative odd", or "zero"
    
    Example: number_classifier(4) → "positive even"
    Example: number_classifier(-3) → "negative odd"
    Example: number_classifier(0) → "zero"
    """
    pass
