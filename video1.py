
class Employee:
    
    # initialize or its a constructor
    '''
    self is the instance: 'self.first = first' == 'emp_1.first = 'Bilbo'': it's the same thing
    when we create employee objects 'emp_1.first = 'Bilbo'' will be made automatically
    '''
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + '@company.com'
    
    # takes the instance
    # self will be the instance like emp_1 or emp_2
    # that is what is getting passed to the function
    def full_name(self):
        full_name = self.first + ', ' + self.last
        return full_name
        
''' 
difference between class and an instance of a class
    class: a blueprint for creating instances
    instance: contain data that is unique to each instance
 '''
# instances of class Employee
emp_1 = Employee('Bilbo', 'Baggins', 50000) # when the employee is made the instance is passed automatically, self is not needed
emp_2 = Employee('Test', 'User', 60000)

# print(emp_1.email)
# print(emp_2.email)

# fullName = emp_1.full_name()
# print(fullName)
# print(emp_2.full_name())

# these are the same thing
print(emp_1.full_name()) # has instance of self
print(Employee.full_name(emp_2)) # need to pass instance of emp_2 as self
