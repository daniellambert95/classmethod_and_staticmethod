#!/usr/bin/env python3

# @classmethod and @staticmethod below

#creating a class
class Employee:

    num_of_emps = 0
    raise_amt = 1.04

# initializing self and instances

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

        Employee.num_of_emps +=1

#creating a method

    def fullname(self):
        return self.first + self.last

#creating a method

    def apply_raise(self):
        self.pay = self.pay * self.raise_amt

# creating a classmethod, 'cls' is used instead of self so it calls the class
# second instance/argument will be entered in print statement (e.g. print(Employee.set_raise_amt(1.05)))
    
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

# creating a static method that takes a date (year, month, day) as an instance and returns 
# boolean values (based on a datetime statement (days of week stored as 0 - 6))

    @staticmethod
    def is_workday(day):
        if day.weekday() == 6 or day.weekday() == 6:
            return False
        return True

emp_1 = Employee('Daniel', 'Lambert', 25000)
emp_2 = Employee('Uliana', 'Kruk', 50000)

# calling the class method on the class with the instance of new raise amount
Employee.set_raise_amt(1.05)
# Showing it works by priting it here
print(Employee.raise_amt)

# importing date time and setting a variable that will be used as an instance in static method
import datetime
my_date = datetime.date(2021, 11, 19)
# printing the static method with the instance set in the line above
print(Employee.is_workday(my_date))