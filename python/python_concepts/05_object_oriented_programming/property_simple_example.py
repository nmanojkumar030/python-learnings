"""Simple @property Example - Easy to Understand"""


class Temperature:
    def __init__(self, celsius):
        self.__celsius = celsius  # Private attribute
    
    # @property makes this method look like an attribute
    @property
    def celsius(self):
        """Getter - accessed like: temp.celsius"""
        return self.__celsius
    
    @celsius.setter
    def celsius(self, value):
        """Setter - accessed like: temp.celsius = 25"""
        if value < -273.15:  # Absolute zero
            raise ValueError("Temperature cannot be below absolute zero")
        self.__celsius = value
    
    @property
    def fahrenheit(self):
        """Computed property - calculated from celsius"""
        return (self.__celsius * 9/5) + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        """Setter for fahrenheit - converts to celsius"""
        celsius = (value - 32) * 5/9
        self.celsius = celsius  # Uses the celsius setter with validation


# Demonstrate the @property decorator
if __name__ == "__main__":
    print("=== @property DECORATOR EXPLAINED ===")
    
    # Create a temperature object
    temp = Temperature(25)
    
    print("\n1. ACCESSING PROPERTIES (looks like attributes)")
    print(f"temp.celsius = {temp.celsius}")      # Calls the getter
    print(f"temp.fahrenheit = {temp.fahrenheit}")  # Calls the computed getter
    
    print("\n2. SETTING PROPERTIES (looks like attributes)")
    temp.celsius = 30  # Calls the setter
    print(f"After setting celsius to 30: {temp.celsius}°C = {temp.fahrenheit}°F")
    
    temp.fahrenheit = 86  # Calls the fahrenheit setter
    print(f"After setting fahrenheit to 86: {temp.fahrenheit}°F = {temp.celsius}°C")
    
    print("\n3. VALIDATION IN SETTERS")
    try:
        temp.celsius = -300  # This will fail validation
    except ValueError as e:
        print(f"Error: {e}")
    
    print("\n4. COMPUTED PROPERTIES UPDATE AUTOMATICALLY")
    temp.celsius = 0
    print(f"0°C = {temp.fahrenheit}°F")
    
    temp.celsius = 100
    print(f"100°C = {temp.fahrenheit}°F")
    
    print("\n=== KEY POINTS ===")
    print("• @property makes methods look like attributes")
    print("• temp.celsius calls the getter method")
    print("• temp.celsius = 25 calls the setter method")
    print("• Can add validation in setters")
    print("• Computed properties calculate values on-the-fly")
    print("• Clean, intuitive interface")
