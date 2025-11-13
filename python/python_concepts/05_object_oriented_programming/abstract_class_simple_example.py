"""Simple Abstract Class Example"""

from abc import ABC, abstractmethod


# Abstract base class
class Vehicle(ABC):
    """Abstract base class for all vehicles"""
    
    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model
    
    @abstractmethod
    def start_engine(self) -> str:
        """Abstract method - must be implemented by subclasses"""
        pass
    
    @abstractmethod
    def get_fuel_type(self) -> str:
        """Abstract method - must be implemented by subclasses"""
        pass
    
    def get_info(self) -> str:
        """Concrete method - can be used by all subclasses"""
        return f"{self.brand} {self.model}"


# Concrete class implementing Vehicle
class Car(Vehicle):
    def __init__(self, brand: str, model: str, fuel_type: str):
        super().__init__(brand, model)
        self.fuel_type = fuel_type
    
    def start_engine(self) -> str:
        return "Car engine started with key"
    
    def get_fuel_type(self) -> str:
        return self.fuel_type


# Concrete class implementing Vehicle
class Motorcycle(Vehicle):
    def __init__(self, brand: str, model: str):
        super().__init__(brand, model)
    
    def start_engine(self) -> str:
        return "Motorcycle engine started with button"
    
    def get_fuel_type(self) -> str:
        return "Petrol"


# Concrete class implementing Vehicle
class ElectricCar(Vehicle):
    def __init__(self, brand: str, model: str):
        super().__init__(brand, model)
    
    def start_engine(self) -> str:
        return "Electric motor activated silently"
    
    def get_fuel_type(self) -> str:
        return "Electric"


def demonstrate_abstract_class():
    """Demonstrate abstract class usage"""
    print("=== ABSTRACT CLASS EXAMPLE ===")
    
    # Create concrete vehicle objects
    car = Car("Toyota", "Camry", "Petrol")
    motorcycle = Motorcycle("Honda", "CBR")
    electric_car = ElectricCar("Tesla", "Model 3")
    
    vehicles = [car, motorcycle, electric_car]
    
    print("\nVehicle Information:")
    for vehicle in vehicles:
        print(f"\n{vehicle.get_info()}")
        print(f"Start: {vehicle.start_engine()}")
        print(f"Fuel: {vehicle.get_fuel_type()}")
    
    # Try to instantiate abstract class (this will fail)
    print("\n" + "=" * 40)
    print("CANNOT INSTANTIATE ABSTRACT CLASS")
    print("=" * 40)
    
    try:
        # This will raise TypeError
        vehicle = Vehicle("Test", "Test")
    except TypeError as e:
        print(f"Error: {e}")
        print("Abstract classes cannot be instantiated directly!")


def demonstrate_incomplete_implementation():
    """Show what happens when abstract methods are not implemented"""
    print("\n" + "=" * 40)
    print("INCOMPLETE IMPLEMENTATION")
    print("=" * 40)
    
    # This class only implements one abstract method
    class IncompleteVehicle(Vehicle):
        def __init__(self, brand: str, model: str):
            super().__init__(brand, model)
        
        def start_engine(self) -> str:
            return "Engine started"
        
        # Missing get_fuel_type method!
    
    try:
        incomplete = IncompleteVehicle("Test", "Test")
    except TypeError as e:
        print(f"Error: {e}")
        print("All abstract methods must be implemented!")


if __name__ == "__main__":
    demonstrate_abstract_class()
    demonstrate_incomplete_implementation()
    
    print("\n" + "=" * 40)
    print("KEY POINTS")
    print("=" * 40)
    print("• Abstract classes cannot be instantiated")
    print("• Subclasses must implement all abstract methods")
    print("• Abstract classes can have concrete methods")
    print("• Provides a common interface for related classes")
    print("• Enforces implementation of required methods")
