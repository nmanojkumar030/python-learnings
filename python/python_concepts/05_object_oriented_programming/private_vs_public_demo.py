"""Demonstration of Public vs Private Attributes"""

# Original Person class with public attributes
class PersonPublic:
    def __init__(self, fn, ln):
        self.fn = fn  # Public attribute
        self.ln = ln  # Public attribute
    
    def get_info(self):
        print("First Name:", self.fn)
        print("Last Name:", self.ln)


# New Person class with private attributes
class PersonPrivate:
    def __init__(self, fn, ln):
        self.__fn = fn  # Private attribute
        self.__ln = ln  # Private attribute
    
    @property
    def first_name(self):
        return self.__fn
    
    @first_name.setter
    def first_name(self, fn):
        if isinstance(fn, str) and fn.strip():
            self.__fn = fn.strip()
        else:
            raise ValueError("First name must be a non-empty string")
    
    @property
    def last_name(self):
        return self.__ln
    
    @last_name.setter
    def last_name(self, ln):
        if isinstance(ln, str) and ln.strip():
            self.__ln = ln.strip()
        else:
            raise ValueError("Last name must be a non-empty string")
    
    def get_info(self):
        print("First Name:", self.__fn)
        print("Last Name:", self.__ln)


if __name__ == "__main__":
    print("=== PUBLIC ATTRIBUTES DEMO ===")
    p1 = PersonPublic("Manoj", "Kumar")
    
    # Direct access to public attributes
    print(f"Direct access: {p1.fn} {p1.ln}")
    
    # Can modify directly (no validation)
    p1.fn = ""  # No validation - empty string allowed
    p1.ln = 123  # No validation - number allowed
    print(f"After direct modification: {p1.fn} {p1.ln}")
    
    print("\n=== PRIVATE ATTRIBUTES DEMO ===")
    p2 = PersonPrivate("Manoj", "Kumar")
    
    # Access through properties
    print(f"Property access: {p2.first_name} {p2.last_name}")
    
    # Cannot access private attributes directly
    try:
        print(p2.__fn)  # This will fail
    except AttributeError as e:
        print(f"Cannot access private attribute: {e}")
    
    # Properties provide validation
    try:
        p2.first_name = ""  # This will raise ValueError
    except ValueError as e:
        print(f"Validation error: {e}")
    
    try:
        p2.last_name = 123  # This will raise ValueError
    except ValueError as e:
        print(f"Validation error: {e}")
    
    # Valid modifications work
    p2.first_name = "John"
    p2.last_name = "Doe"
    print(f"After valid modification: {p2.first_name} {p2.last_name}")
    
    print("\n=== SUMMARY ===")
    print("Public attributes: Direct access, no validation")
    print("Private attributes: Controlled access, validation, encapsulation")
