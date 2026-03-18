# Week 9: Classes & Objects

# --- Exercise 1 ---
class Student:
    """
    Create a Student class with:
    - __init__(self, name, student_id): store name, student_id, and empty grades list
    - add_grade(self, grade): append grade to grades list
    - get_average(self): return average of grades, or 0 if no grades
    - is_passing(self): return True if average >= 60
    - __str__(self): return "Student(name, ID: student_id, Avg: X.X)"
    """
    pass


# --- Exercise 2 ---
class BankAccount:
    """
    Create a BankAccount class with:
    - __init__(self, owner, balance=0): store owner and balance
    - deposit(self, amount): add amount if positive, return new balance
    - withdraw(self, amount): subtract if sufficient funds, return new balance
      If insufficient, return "Insufficient funds"
    - transfer(self, other_account, amount): withdraw from self, deposit to other
      Return True if successful, False if insufficient funds
    - __str__(self): return "Account(owner: $balance)"
    """
    pass


# --- Exercise 3 ---
class TodoList:
    """
    Create a TodoList class with:
    - __init__(self): empty list of tasks (each task is a dict with "task" and "done" keys)
    - add_task(self, task): add {"task": task, "done": False}
    - complete_task(self, index): mark task at index as done, return True. Return False if invalid index.
    - get_pending(self): return list of undone task strings
    - get_completed(self): return list of done task strings
    - __str__(self): return "TodoList: X pending, Y completed"
    """
    pass


# --- Exercise 4 ---
class Inventory:
    """
    Create an Inventory class for a store:
    - __init__(self): empty dict of items {name: {"price": float, "quantity": int}}
    - add_item(self, name, price, quantity): add or update item
    - sell_item(self, name, quantity): reduce quantity, return total sale price
      Return "Item not found" or "Not enough stock" if applicable
    - get_value(self): return total inventory value (sum of price * quantity for all items)
    - low_stock(self, threshold=5): return list of item names with quantity <= threshold
    """
    pass


# --- Exercise 5 ---
class GradeBook:
    """
    Create a GradeBook class:
    - __init__(self): empty dict of students {name: [grades]}
    - add_student(self, name): add student with empty grades
    - add_grade(self, name, grade): add grade to student. Return False if student not found.
    - get_class_average(self): return average across all students
    - get_top_student(self): return name of student with highest average
    - get_report(self): return list of dicts [{"name": str, "average": float, "grade": str}]
      Grade: A (90+), B (80-89), C (70-79), D (60-69), F (<60)
    """
    pass
