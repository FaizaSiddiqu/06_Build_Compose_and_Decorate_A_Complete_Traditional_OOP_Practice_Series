# 7. Access Modifiers: Public, Private, and Protected
# Assignment:
# Create a class Employee with:
# a public variable name,
# a protected variable _salary, and
# a private variable __ssn
# Try accessing all three variables from an object of the class and document what happens.


class Employee:
    def __init__(self, name, salery, ssn):
        self.name = name    #pblic variable
        self._salery = salery  # protected variable 
        self.__ssn  = ssn    # private varible
        
        
emp = Employee("Faiza", 50000, "123-45-6789")
print(emp.name)      # Accessing public variable
print(emp._salery)   # Accessing protected variable  
# print(emp._ssn)      # Accessing private variable (will raise an error)
print(emp._Employee__ssn)      # correct way to access private     
    