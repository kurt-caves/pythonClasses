class Employee:
    
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first # these are instance variables
        self.last = last
        self.pay = pay
        self.email = first + "." + last + '@company.com'
        # the init method will run everytime we make an new employee
        # we dont want allow num_of_emps to be overwritten
        Employee.num_of_emps += 1
    
    
    def full_name(self):
        full_name = self.first + ', ' + self.last
        return full_name
    
    # take in the instance of self
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # take in the class not the instance
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod #alternative constructor
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
    @staticmethod # static methods dont take the class or instance as first arg
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
        


emp_1 = Employee('Bilbo', 'Baggins', 50000) # when the employee is made the instance is passed automatically, self is not needed
emp_2 = Employee('Test', 'User', 60000)

import datetime
my_date = datetime.date(2016, 7, 11)
print(Employee.is_workday(my_date))


# emp_str_1 = 'John-Doe-70000'
# emp_str_2 = 'Steve-Smith-30000'
# emp_str_3 = 'Jane-Doe-90000'

# new_emp_1 = Employee.from_string(emp_str_1)

# # first, last, pay = emp_str_1.split('-')
# # new_emp_1 = Employee(first, last, pay)
# print(new_emp_1.email)
# print(new_emp_1.full_name())


# Employee.set_raise_amt(1.10)

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)


# print(Employee.num_of_emps)