# 12. Static Methods
# Assignment:
# Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that 
# returns the Fahrenheit value.

class Temperature:
    @staticmethod
    
    def celsius_to_fahrenhite(c):
        return (c * 9/5) + 32
    
print(Temperature.celsius_to_fahrenhite(25))  # Output: 77.0
        