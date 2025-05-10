
# Build_Compose_and_Decorate_A_Complete_Traditional_OOP_Practice_Series.

# 1-  Using Self
# Assignment:
# Create a class Student with attributes name and marks. Use the self keyword to initialize these
# values via a constructor. Add a method display() that prints student details.

class Student:
    def __init__(self, name, marks):
        self.name = name            # instance variable is created becouse of self and self is a instance of class
        self.marks = marks
        
    def display(self):
        print(f"Student Name: {self.name}")
        print(f"Marks: {self.marks}")
        
Student1 = Student("Faiza", 90)
Student1.display()





    
    






