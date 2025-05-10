# 2 - Using cls
# Assignment:
# Create a class Counter that keeps track of how many objects have been created.Use a class 
# variable and a class method with cls to manage and display the count.


class Counter: 
    count = 0                                   #  inside the class is a class variable
    def __init__(self):                          # constructor
        Counter.count += 1
        
    @classmethod                     # decorator  class variables ko access karne ke liye class method use hota hai
    def show_count(cls):
        print(f"Total Object created : {cls.count}")
        
obj1 = Counter()
obj2 = Counter()
obj3 = Counter()
obj4 = Counter()
        
Counter.show_count()