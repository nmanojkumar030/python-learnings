"""Comprehensive Explanation of @property Decorator"""


class Person:
    def __init__(self, first_name, last_name, age):
        self.__first_name = first_name  # Private attribute
        self.__last_name = last_name    # Private attribute
        self.__age = age                # Private attribute

    # 1. Basic Property (Read-only)
    @property
    def full_name(self):
        """Read-only property that combines first and last name"""
        return f"{self.__first_name} {self.__last_name}"
    
    # 2. Property with Getter and Setter
    @property
    def first_name(self):
        """Getter for first name"""
        return self.__first_name
    
    @first_name.setter
    def first_name(self, value):
        """Setter for first name with validation"""
        if isinstance(value, str) and value.strip():
            self.__first_name = value.strip()
        else:
            raise ValueError("First name must be a non-empty string")
    
    # 3. Property with Getter, Setter, and Deleter
    @property
    def age(self):
        """Getter for age"""
        return self.__age
    
    @age.setter
    def age(self, value):
        """Setter for age with validation"""
        if isinstance(value, int) and 0 <= value <= 150:
            self.__age = value
        else:
            raise ValueError("Age must be an integer between 0 and 150")
    
    @age.deleter
    def age(self):
        """Deleter for age"""
        print("Age cannot be deleted, setting to 0")
        self.__age = 0
    
    # 4. Computed Property (calculated on-the-fly)
    @property
    def is_adult(self):
        """Computed property that returns True if person is adult"""
        return self.__age >= 18
    
    @property
    def initials(self):
        """Computed property that returns initials"""
        return f"{self.__first_name[0]}.{self.__last_name[0]}."


def demonstrate_properties():
    """Demonstrate different types of properties"""
    print("=" * 60)
    print("PROPERTY DECORATOR EXPLANATION")
    print("=" * 60)
    
    # Create a person
    person = Person("Manoj", "Kumar", 25)
    
    print("\n1. READ-ONLY PROPERTY (full_name)")
    print("-" * 40)
    print(f"person.full_name = {person.full_name}")
    try:
        person.full_name = "John Doe"  # This will fail - no setter
    except AttributeError as e:
        print(f"Cannot set read-only property: {e}")
    
    print("\n2. PROPERTY WITH GETTER AND SETTER (first_name)")
    print("-" * 40)
    print(f"Current first_name: {person.first_name}")
    person.first_name = "John"  # Uses setter
    print(f"After setting: {person.first_name}")
    
    try:
        person.first_name = ""  # Validation will fail
    except ValueError as e:
        print(f"Validation error: {e}")
    
    print("\n3. PROPERTY WITH GETTER, SETTER, AND DELETER (age)")
    print("-" * 40)
    print(f"Current age: {person.age}")
    person.age = 30  # Uses setter
    print(f"After setting: {person.age}")
    
    try:
        person.age = 200  # Validation will fail
    except ValueError as e:
        print(f"Validation error: {e}")
    
    del person.age  # Uses deleter
    print(f"After deletion: {person.age}")
    
    print("\n4. COMPUTED PROPERTIES")
    print("-" * 40)
    person.age = 25  # Reset age
    print(f"Age: {person.age}")
    print(f"Is adult: {person.is_adult}")
    print(f"Initials: {person.initials}")
    
    # Change age and see computed properties update
    person.age = 16
    print(f"After changing age to 16:")
    print(f"Is adult: {person.is_adult}")


def compare_without_property():
    """Show how the same functionality would look without properties"""
    print("\n" + "=" * 60)
    print("COMPARISON: WITH vs WITHOUT @property")
    print("=" * 60)
    
    # Without @property (traditional getter/setter methods)
    class PersonWithoutProperty:
        def __init__(self, first_name, last_name):
            self.__first_name = first_name
            self.__last_name = last_name
        
        def get_first_name(self):
            return self.__first_name
        
        def set_first_name(self, value):
            if isinstance(value, str) and value.strip():
                self.__first_name = value.strip()
            else:
                raise ValueError("First name must be a non-empty string")
        
        def get_full_name(self):
            return f"{self.__first_name} {self.__last_name}"
    
    # With @property
    class PersonWithProperty:
        def __init__(self, first_name, last_name):
            self.__first_name = first_name
            self.__last_name = last_name
        
        @property
        def first_name(self):
            return self.__first_name
        
        @first_name.setter
        def first_name(self, value):
            if isinstance(value, str) and value.strip():
                self.__first_name = value.strip()
            else:
                raise ValueError("First name must be a non-empty string")
        
        @property
        def full_name(self):
            return f"{self.__first_name} {self.__last_name}"
    
    print("\nUSAGE COMPARISON:")
    print("-" * 40)
    
    # Without property
    p1 = PersonWithoutProperty("Manoj", "Kumar")
    print("Without @property:")
    print(f"  p1.get_first_name() = {p1.get_first_name()}")
    p1.set_first_name("John")
    print(f"  p1.get_full_name() = {p1.get_full_name()}")
    
    # With property
    p2 = PersonWithProperty("Manoj", "Kumar")
    print("\nWith @property:")
    print(f"  p2.first_name = {p2.first_name}")
    p2.first_name = "John"
    print(f"  p2.full_name = {p2.full_name}")
    
    print("\nADVANTAGES OF @property:")
    print("-" * 40)
    print("1. Cleaner syntax - looks like accessing attributes")
    print("2. Can add validation without changing interface")
    print("3. Can make read-only properties")
    print("4. Can compute values on-the-fly")
    print("5. Backward compatibility")


def property_advanced_examples():
    """Show advanced property usage patterns"""
    print("\n" + "=" * 60)
    print("ADVANCED PROPERTY EXAMPLES")
    print("=" * 60)
    
    class Rectangle:
        def __init__(self, width, height):
            self.__width = width
            self.__height = height
        
        @property
        def width(self):
            return self.__width
        
        @width.setter
        def width(self, value):
            if value > 0:
                self.__width = value
            else:
                raise ValueError("Width must be positive")
        
        @property
        def height(self):
            return self.__height
        
        @height.setter
        def height(self, value):
            if value > 0:
                self.__height = value
            else:
                raise ValueError("Height must be positive")
        
        @property
        def area(self):
            """Computed property - calculated each time"""
            return self.__width * self.__height
        
        @property
        def perimeter(self):
            """Computed property - calculated each time"""
            return 2 * (self.__width + self.__height)
        
        @property
        def is_square(self):
            """Computed property - boolean"""
            return self.__width == self.__height
    
    rect = Rectangle(5, 3)
    print(f"Rectangle: {rect.width} x {rect.height}")
    print(f"Area: {rect.area}")
    print(f"Perimeter: {rect.perimeter}")
    print(f"Is square: {rect.is_square}")
    
    # Change dimensions and see computed properties update
    rect.width = 4
    rect.height = 4
    print(f"\nAfter changing to 4x4:")
    print(f"Area: {rect.area}")
    print(f"Perimeter: {rect.perimeter}")
    print(f"Is square: {rect.is_square}")


if __name__ == "__main__":
    demonstrate_properties()
    compare_without_property()
    property_advanced_examples()
    
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print("@property decorator allows you to:")
    print("• Make methods look like attributes")
    print("• Add validation to attribute access")
    print("• Create read-only properties")
    print("• Compute values on-the-fly")
    print("• Maintain clean, intuitive interfaces")
    print("• Provide backward compatibility")
