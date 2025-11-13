"""Person Class with Protected Attributes"""


class Person:

    def __init__(self, fn, ln):
        self._fn = fn  # Protected attribute with single underscore
        self._ln = ln  # Protected attribute with single underscore

    def get_first_name(self):
        """Getter method for first name"""
        return self._fn

    def set_first_name(self, fn):
        """Setter method for first name"""
        if isinstance(fn, str) and fn.strip():
            self._fn = fn.strip()
        else:
            raise ValueError("First name must be a non-empty string")

    def get_last_name(self):
        """Getter method for last name"""
        return self._ln

    def set_last_name(self, ln):
        """Setter method for last name"""
        if isinstance(ln, str) and ln.strip():
            self._ln = ln.strip()
        else:
            raise ValueError("Last name must be a non-empty string")

    def get_info(self):
        print("First Name:", self._fn)
        print("Last Name:", self._ln)


if __name__ == "__main__":
    p = Person("Manoj", "Kumar")
    p.get_info()

    # Demonstrate getter methods
    print(f"First name: {p.get_first_name()}")
    print(f"Last name: {p.get_last_name()}")

    # Demonstrate setter methods
    p.set_first_name("John")
    p.set_last_name("Doe")
    p.get_info()

    # Protected attributes CAN be accessed directly (but shouldn't be)
    print(f"Direct access (not recommended): {p._fn} {p._ln}")

    # Demonstrate validation
    try:
        p.set_first_name("")  # This will raise ValueError
    except ValueError as e:
        print(f"Validation error: {e}")

    try:
        p.set_last_name(123)  # This will raise ValueError
    except ValueError as e:
        print(f"Validation error: {e}")

    # Valid modifications work
    p.set_first_name("Jane")
    p.set_last_name("Smith")
    print(f"After valid modification: {p.get_first_name()} {p.get_last_name()}")

    print("\n=== PROTECTED ATTRIBUTES SUMMARY ===")
    print("Protected attributes (_fn, _ln):")
    print("- Can be accessed directly: p._fn")
    print("- Convention indicates 'don't access directly'")
    print("- No actual enforcement by Python")
    print("- Should use getter/setter methods instead")
