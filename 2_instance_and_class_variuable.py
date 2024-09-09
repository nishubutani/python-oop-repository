# Title: Distance and Class Variable
# 
# This code demonstrates the use of class variables and instance variables in Python's 
# Object-Oriented Programming (OOP). Class variables are shared across all instances 
# of the class, whereas instance variables are unique to each object. In this example, 
# `increment` is a class variable that can be overridden by individual objects, and 
# `no_of_employees` is a class variable that keeps track of how many `Employee` objects 
# have been created. The `increase` method adjusts the employee's salary based on the 
# increment value.


"""
Concepts Used:
Class Variable: Shared by all instances of the class (increment, no_of_employees).
Instance Variable: Unique to each instance of the class (fname, lname, salary, and the overridden increment).
Class Method vs Instance Method: The increase method operates on instance variables, adjusting the salary based on the increment defined per instance.
Object Count Tracking: no_of_employees is a class variable used to track how many Employee objects have been created.

"""
class Employee:
    # Class variables shared by all instances of the class
    increment = 1.5
    no_of_employees = 0

    def __init__(self, fname, lname, salary):
        # Instance variables unique to each object
        self.fname = fname  # Attribute to store the first name of the employee
        self.lname = lname  # Attribute to store the last name of the employee
        self.salary = salary  # Attribute to store the salary of the employee

        # Overriding the class variable 'increment' with a custom value for this object
        self.increment = 1.4

        # Incrementing the count of employees each time an instance is created
        Employee.no_of_employees += 1

    # Method to increase the employee's salary based on the increment
    def increase(self):
        # Adjusting the salary using the instance's increment value
        self.salary = int(self.salary * self.increment)


# Creating two Employee objects
Nishant = Employee("Nishant", "butani", 54000)
Rohan = Employee("Rohan", "savaliya", 40000)

# Printing the dictionary representation of the Nishant object (shows instance variables)
print(Nishant.__dict__)

# Printing the dictionary representation of the Employee class (shows class variables)
print(Employee.__dict__)

# Increasing Nishant's salary and printing the updated salary
Nishant.increase()
print(Nishant.salary)

# Printing the total number of employees created so far
print(Employee.no_of_employees)
