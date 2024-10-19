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

print(Employee.num_of_emps)


emp_1 = Employee('Bilbo', 'Baggins', 50000) # when the employee is made the instance is passed automatically, self is not needed
emp_2 = Employee('Test', 'User', 60000)



print(Employee.num_of_emps)



'''
Class variables are shared among all instances of a class
'''

# change the raise amount for the class and all the instances
# Employee.raise_amount = 1.05
# will only work in the emp_1 instance
# emp_1.raise_amount = 1.06
# print(emp_1.__dict__)

# print out the name space
# will not contain rasie amount
# print(emp_1.__dict__)

# # will contain rasie amount
# print(Employee.__dict__)

# we can access the class variable from the Class and from the instance
# print(emp_1.raise_amount)
# print(Employee.raise_amount)
# print(emp_2.raise_amount)