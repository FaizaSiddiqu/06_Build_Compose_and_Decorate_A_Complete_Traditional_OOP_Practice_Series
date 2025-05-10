# 18. Property Decorators: @property, @setter, and @deleter
# Assignment:
# Create a class Product with a private attribute _price. Use @property to get the price,
# @price.setter to update it, and @price.deleter to delete it.

class Product:
    def __init__(self, price):
        self.price = price
        
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        self._price = value
        
    @price.deleter
    def price(self):
        del self._price
        
p = Product(100)
print(p.price)  # Accessing the price using the property
p.price = 150  # Updating the price using the setter
print(p.price)  # Accessing the updated price
del p.price  # Deleting the price using the deleter        
        

