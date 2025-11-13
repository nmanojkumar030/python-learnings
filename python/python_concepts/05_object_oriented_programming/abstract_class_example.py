"""Abstract Class Example using Python's abc module"""

from abc import ABC, abstractmethod
from typing import List


# Abstract base class for shapes
class Shape(ABC):
    """Abstract base class for all shapes"""

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def area(self) -> float:
        """Abstract method that must be implemented by subclasses"""
        pass

    @abstractmethod
    def perimeter(self) -> float:
        """Abstract method that must be implemented by subclasses"""
        pass

    def describe(self) -> str:
        """Concrete method that can be used by all subclasses"""
        return (
            f"{self.name}: Area = {self.area():.2f}, Perimeter = {self.perimeter():.2f}"
        )


# Concrete class implementing the abstract Shape
class Circle(Shape):
    def __init__(self, radius: float):
        super().__init__("Circle")
        self.radius = radius

    def area(self) -> float:
        """Implementation of abstract area method"""
        import math

        return math.pi * self.radius**2

    def perimeter(self) -> float:
        """Implementation of abstract perimeter method"""
        import math

        return 2 * math.pi * self.radius


# Another concrete class implementing the abstract Shape
class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        super().__init__("Rectangle")
        self.width = width
        self.height = height

    def area(self) -> float:
        """Implementation of abstract area method"""
        return self.width * self.height

    def perimeter(self) -> float:
        """Implementation of abstract perimeter method"""
        return 2 * (self.width + self.height)


# Another concrete class implementing the abstract Shape
class Triangle(Shape):
    def __init__(self, base: float, height: float, side1: float, side2: float):
        super().__init__("Triangle")
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2

    def area(self) -> float:
        """Implementation of abstract area method"""
        return 0.5 * self.base * self.height

    def perimeter(self) -> float:
        """Implementation of abstract perimeter method"""
        return self.base + self.side1 + self.side2


# Abstract class with abstract properties
class Animal(ABC):
    """Abstract base class for animals"""

    def __init__(self, name: str):
        self.name = name

    @property
    @abstractmethod
    def sound(self) -> str:
        """Abstract property that must be implemented"""
        pass

    @property
    @abstractmethod
    def habitat(self) -> str:
        """Abstract property that must be implemented"""
        pass

    def make_sound(self) -> str:
        """Concrete method using abstract property"""
        return f"{self.name} says: {self.sound}"

    def describe(self) -> str:
        """Concrete method using abstract properties"""
        return f"{self.name} lives in {self.habitat} and makes sound: {self.sound}"


# Concrete class implementing Animal
class Dog(Animal):
    @property
    def sound(self) -> str:
        return "Woof!"

    @property
    def habitat(self) -> str:
        return "Domestic"


# Concrete class implementing Animal
class Cat(Animal):
    @property
    def sound(self) -> str:
        return "Meow!"

    @property
    def habitat(self) -> str:
        return "Domestic"


# Concrete class implementing Animal
class Bird(Animal):
    def __init__(self, name: str, bird_sound: str):
        super().__init__(name)
        self._sound = bird_sound

    @property
    def sound(self) -> str:
        return self._sound

    @property
    def habitat(self) -> str:
        return "Sky"


# Abstract class with abstract class methods
class Database(ABC):
    """Abstract base class for database operations"""

    @classmethod
    @abstractmethod
    def connect(cls, connection_string: str) -> "Database":
        """Abstract class method for database connection"""
        pass

    @abstractmethod
    def execute_query(self, query: str) -> List[dict]:
        """Abstract method for executing queries"""
        pass

    @abstractmethod
    def close(self) -> None:
        """Abstract method for closing connection"""
        pass


# Concrete implementation of Database
class SQLiteDatabase(Database):
    def __init__(self, connection_string: str):
        self.connection_string = connection_string
        self.connected = True

    @classmethod
    def connect(cls, connection_string: str) -> "SQLiteDatabase":
        return cls(connection_string)

    def execute_query(self, query: str) -> List[dict]:
        return [{"result": f"SQLite: {query}"}]

    def close(self) -> None:
        self.connected = False


def demonstrate_abstract_classes():
    """Demonstrate abstract class usage"""
    print("=" * 60)
    print("ABSTRACT CLASS EXAMPLES")
    print("=" * 60)

    # Test Shape abstract class
    print("\n1. SHAPE ABSTRACT CLASS")
    print("-" * 40)

    # Create concrete shape objects
    circle = Circle(5)
    rectangle = Rectangle(4, 6)
    triangle = Triangle(3, 4, 5, 5)

    shapes = [circle, rectangle, triangle]

    for shape in shapes:
        print(shape.describe())

    # Test Animal abstract class
    print("\n2. ANIMAL ABSTRACT CLASS")
    print("-" * 40)

    dog = Dog("Buddy")
    cat = Cat("Whiskers")
    bird = Bird("Polly", "Squawk!")

    animals = [dog, cat, bird]

    for animal in animals:
        print(animal.describe())
        print(animal.make_sound())

    # Test Database abstract class
    print("\n3. DATABASE ABSTRACT CLASS")
    print("-" * 40)

    db = SQLiteDatabase.connect("sqlite:///test.db")
    results = db.execute_query("SELECT * FROM users")
    print(f"Query results: {results}")
    db.close()

    # Demonstrate that you cannot instantiate abstract classes
    print("\n4. CANNOT INSTANTIATE ABSTRACT CLASSES")
    print("-" * 40)

    try:
        # This will raise TypeError
        shape = Shape("Test")
    except TypeError as e:
        print(f"Cannot instantiate abstract class Shape: {e}")

    try:
        # This will raise TypeError
        animal = Animal("Test")
    except TypeError as e:
        print(f"Cannot instantiate abstract class Animal: {e}")


def demonstrate_abstract_methods():
    """Show what happens when abstract methods are not implemented"""
    print("\n" + "=" * 60)
    print("ABSTRACT METHOD IMPLEMENTATION REQUIREMENTS")
    print("=" * 60)

    # Example of incomplete implementation
    class IncompleteShape(Shape):
        def __init__(self):
            super().__init__("Incomplete")

        # Only implementing area, not perimeter
        def area(self) -> float:
            return 10.0

        # Missing perimeter method - this will cause error

    try:
        incomplete = IncompleteShape()
    except TypeError as e:
        print(f"Cannot instantiate incomplete class: {e}")


if __name__ == "__main__":
    demonstrate_abstract_classes()
    demonstrate_abstract_methods()

    print("\n" + "=" * 60)
    print("ABSTRACT CLASS SUMMARY")
    print("=" * 60)
    print("✓ Abstract classes cannot be instantiated directly")
    print("✓ Subclasses must implement all abstract methods")
    print("✓ Abstract classes can have concrete methods")
    print("✓ Abstract methods can be properties, class methods, etc.")
    print("✓ Provides a common interface for related classes")
    print("✓ Enforces implementation of required methods")
