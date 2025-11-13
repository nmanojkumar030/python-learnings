"""
Polymorphism Examples in Python

Polymorphism is one of the four fundamental principles of Object-Oriented Programming (OOP).
It allows objects of different classes to be treated as objects of a common superclass.

Types of Polymorphism in Python:
1. Method Overriding (Runtime Polymorphism)
2. Method Overloading (Compile-time Polymorphism) - Limited in Python
3. Duck Typing
4. Operator Overloading
"""

# ============================================================================
# 1. METHOD OVERRIDING (Runtime Polymorphism)
# ============================================================================

class Animal:
    """Base class for animals"""
    
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        """Base method that will be overridden by subclasses"""
        return "Some animal sound"
    
    def move(self):
        """Base method that will be overridden by subclasses"""
        return f"{self.name} is moving"
    
    def get_info(self):
        """Method that uses the overridden methods"""
        return f"Name: {self.name}, Sound: {self.make_sound()}, Movement: {self.move()}"


class Dog(Animal):
    """Dog class that overrides Animal methods"""
    
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    
    def make_sound(self):
        """Override the make_sound method"""
        return "Woof! Woof!"
    
    def move(self):
        """Override the move method"""
        return f"{self.name} is running on four legs"
    
    def fetch(self):
        """Dog-specific method"""
        return f"{self.name} is fetching the ball"


class Cat(Animal):
    """Cat class that overrides Animal methods"""
    
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color
    
    def make_sound(self):
        """Override the make_sound method"""
        return "Meow! Meow!"
    
    def move(self):
        """Override the move method"""
        return f"{self.name} is walking gracefully"
    
    def climb(self):
        """Cat-specific method"""
        return f"{self.name} is climbing the tree"


class Bird(Animal):
    """Bird class that overrides Animal methods"""
    
    def __init__(self, name, wingspan):
        super().__init__(name)
        self.wingspan = wingspan
    
    def make_sound(self):
        """Override the make_sound method"""
        return "Tweet! Tweet!"
    
    def move(self):
        """Override the move method"""
        return f"{self.name} is flying in the sky"


# ============================================================================
# 2. DUCK TYPING EXAMPLE
# ============================================================================

class Car:
    """Car class that has a drive method"""
    
    def __init__(self, model):
        self.model = model
    
    def drive(self):
        return f"{self.model} is driving on the road"


class Bicycle:
    """Bicycle class that has a drive method"""
    
    def __init__(self, brand):
        self.brand = brand
    
    def drive(self):
        return f"{self.brand} bicycle is being pedaled"


class Boat:
    """Boat class that has a drive method"""
    
    def __init__(self, name):
        self.name = name
    
    def drive(self):
        return f"{self.name} is sailing on water"


# ============================================================================
# 3. OPERATOR OVERLOADING EXAMPLE
# ============================================================================

class Point:
    """Point class demonstrating operator overloading"""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        """String representation"""
        return f"Point({self.x}, {self.y})"
    
    def __repr__(self):
        """Detailed string representation"""
        return f"Point(x={self.x}, y={self.y})"
    
    def __add__(self, other):
        """Overload the + operator"""
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        elif isinstance(other, (int, float)):
            return Point(self.x + other, self.y + other)
        else:
            raise TypeError(f"Cannot add Point and {type(other).__name__}")
    
    def __sub__(self, other):
        """Overload the - operator"""
        if isinstance(other, Point):
            return Point(self.x - other.x, self.y - other.y)
        elif isinstance(other, (int, float)):
            return Point(self.x - other, self.y - other)
        else:
            raise TypeError(f"Cannot subtract {type(other).__name__} from Point")
    
    def __eq__(self, other):
        """Overload the == operator"""
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False
    
    def __lt__(self, other):
        """Overload the < operator (compare by distance from origin)"""
        if isinstance(other, Point):
            return (self.x**2 + self.y**2) < (other.x**2 + other.y**2)
        return NotImplemented


# ============================================================================
# 4. METHOD OVERLOADING SIMULATION
# ============================================================================

class Calculator:
    """Calculator class demonstrating method overloading simulation"""
    
    def add(self, *args):
        """Add method that can handle different numbers of arguments"""
        if len(args) == 0:
            return 0
        elif len(args) == 1:
            return args[0]
        else:
            return sum(args)
    
    def multiply(self, *args):
        """Multiply method that can handle different numbers of arguments"""
        if len(args) == 0:
            return 1
        elif len(args) == 1:
            return args[0]
        else:
            result = 1
            for arg in args:
                result *= arg
            return result


# ============================================================================
# DEMONSTRATION FUNCTIONS
# ============================================================================

def demonstrate_method_overriding():
    """Demonstrate method overriding (runtime polymorphism)"""
    print("=" * 60)
    print("METHOD OVERRIDING (Runtime Polymorphism)")
    print("=" * 60)
    
    # Create different animal objects
    dog = Dog("Buddy", "Golden Retriever")
    cat = Cat("Whiskers", "Orange")
    bird = Bird("Tweety", 20)
    
    # Store them in a list of Animal type (polymorphism)
    animals = [dog, cat, bird]
    
    # Call the same method on different objects
    for animal in animals:
        print(f"\n{type(animal).__name__}:")
        print(f"  {animal.get_info()}")
        
        # Call specific methods if they exist
        if hasattr(animal, 'fetch'):
            print(f"  {animal.fetch()}")
        if hasattr(animal, 'climb'):
            print(f"  {animal.climb()}")


def demonstrate_duck_typing():
    """Demonstrate duck typing"""
    print("\n" + "=" * 60)
    print("DUCK TYPING")
    print("=" * 60)
    
    # Create different vehicle objects
    car = Car("Toyota Camry")
    bicycle = Bicycle("Trek")
    boat = Boat("Sea Explorer")
    
    # Function that works with any object that has a drive method
    def test_drive(vehicle):
        """Function that demonstrates duck typing"""
        return vehicle.drive()
    
    # Call the same function with different objects
    vehicles = [car, bicycle, boat]
    for vehicle in vehicles:
        print(f"{type(vehicle).__name__}: {test_drive(vehicle)}")


def demonstrate_operator_overloading():
    """Demonstrate operator overloading"""
    print("\n" + "=" * 60)
    print("OPERATOR OVERLOADING")
    print("=" * 60)
    
    # Create Point objects
    p1 = Point(3, 4)
    p2 = Point(1, 2)
    p3 = Point(5, 6)
    
    print(f"p1 = {p1}")
    print(f"p2 = {p2}")
    print(f"p3 = {p3}")
    
    # Demonstrate various operators
    print(f"\np1 + p2 = {p1 + p2}")
    print(f"p1 - p2 = {p1 - p2}")
    print(f"p1 + 5 = {p1 + 5}")
    print(f"p1 == p2: {p1 == p2}")
    print(f"p1 < p3: {p1 < p3}")
    
    # Demonstrate comparison
    points = [p3, p1, p2]
    print(f"\nPoints before sorting: {points}")
    points.sort()
    print(f"Points after sorting: {points}")


def demonstrate_method_overloading():
    """Demonstrate method overloading simulation"""
    print("\n" + "=" * 60)
    print("METHOD OVERLOADING SIMULATION")
    print("=" * 60)
    
    calc = Calculator()
    
    # Demonstrate add method with different numbers of arguments
    print(f"calc.add() = {calc.add()}")
    print(f"calc.add(5) = {calc.add(5)}")
    print(f"calc.add(1, 2) = {calc.add(1, 2)}")
    print(f"calc.add(1, 2, 3, 4, 5) = {calc.add(1, 2, 3, 4, 5)}")
    
    # Demonstrate multiply method with different numbers of arguments
    print(f"\ncalc.multiply() = {calc.multiply()}")
    print(f"calc.multiply(5) = {calc.multiply(5)}")
    print(f"calc.multiply(2, 3) = {calc.multiply(2, 3)}")
    print(f"calc.multiply(2, 3, 4) = {calc.multiply(2, 3, 4)}")


def demonstrate_polymorphic_collections():
    """Demonstrate polymorphism with collections"""
    print("\n" + "=" * 60)
    print("POLYMORPHIC COLLECTIONS")
    print("=" * 60)
    
    # Create a collection of different objects
    objects = [
        Dog("Max", "German Shepherd"),
        Cat("Luna", "Black"),
        Bird("Polly", 15),
        Car("Honda Civic"),
        Point(10, 20)
    ]
    
    print("Processing different objects in a collection:")
    for i, obj in enumerate(objects, 1):
        print(f"\n{i}. {type(obj).__name__}: {obj}")
        
        # Call common methods if they exist
        if hasattr(obj, 'make_sound'):
            print(f"   Sound: {obj.make_sound()}")
        if hasattr(obj, 'drive'):
            print(f"   Drive: {obj.drive()}")
        if hasattr(obj, 'move'):
            print(f"   Move: {obj.move()}")


# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    print("POLYMORPHISM EXAMPLES IN PYTHON")
    print("=" * 60)
    
    # Run all demonstrations
    demonstrate_method_overriding()
    demonstrate_duck_typing()
    demonstrate_operator_overloading()
    demonstrate_method_overloading()
    demonstrate_polymorphic_collections()
    
    print("\n" + "=" * 60)
    print("POLYMORPHISM SUMMARY")
    print("=" * 60)
    print("""
Key Polymorphism Concepts Demonstrated:

1. Method Overriding (Runtime Polymorphism):
   - Different classes implement the same method differently
   - The correct method is called based on the object's actual type at runtime

2. Duck Typing:
   - "If it walks like a duck and quacks like a duck, it's a duck"
   - Objects are used based on their behavior, not their type
   - Any object with the required method can be used

3. Operator Overloading:
   - Custom classes can define how operators work with their objects
   - Examples: +, -, ==, <, >, etc.

4. Method Overloading Simulation:
   - Python doesn't support true method overloading like Java/C++
   - But we can simulate it using default arguments and variable arguments

5. Polymorphic Collections:
   - Collections can hold objects of different types
   - Each object responds to method calls according to its own implementation
    """)
