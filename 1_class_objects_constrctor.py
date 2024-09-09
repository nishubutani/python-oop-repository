# This code demonstrates the concept of Object-Oriented Programming (OOP) in Python.
# The key OOP principle used here is encapsulation, where data (attributes) and
# behaviors (methods) are bundled together within a class. The `Employee` class
# defines a template for creating employee objects, each with specific properties
# such as first name, last name, and salary. This approach ensures that related
# data and functionality are organized into reusable and modular structures.


"""
Concepts Used:
Class: The blueprint for creating objects.
Object: An instance of a class (in this case, Nishant and Rohan are objects of the Employee class).
Constructor (__init__): A special method used to initialize the attributes of the class when an object is created.
Encapsulation: Keeping related data (attributes) and functions (methods) together within a class to maintain a modular structure.
"""

class Employee:
    # The __init__ method is a constructor that initializes an Employee object with the provided values
    # for fname, lname, and salary. 'self' refers to the instance of the class being created.
    def __init__(self, fname, lname, salary):
        self.fname = fname  # Attribute to store the first name of the employee
        self.lname = lname  # Attribute to store the last name of the employee
        self.salary = salary  # Attribute to store the salary of the employee


# Creating two instances (objects) of the Employee class
Nishant = Employee("Nishant", "butani", 54000)
Rohan = Employee("Rohan", "savaliya", 40000)

# Accessing and printing the fname attribute of both objects
print(Nishant.fname, Rohan.fname)
