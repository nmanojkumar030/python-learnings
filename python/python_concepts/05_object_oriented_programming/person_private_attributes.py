"""Person Class with Private Attributes using Properties"""


class Person:

    def __init__(self, fn, ln):
        self.__fn = fn  # Private attribute with double underscore
        self.__ln = ln  # Private attribute with double underscore

    @property
    def first_name(self):
        """Property getter for first name"""
        return self.__fn

    @first_name.setter
    def first_name(self, fn):
        """Property setter for first name"""
        if isinstance(fn, str) and fn.strip():
            self.__fn = fn.strip()
        else:
            raise ValueError("First name must be a non-empty string")

    @property
    def last_name(self):
        """Property getter for last name"""
        return self.__ln

    @last_name.setter
    def last_name(self, ln):
        """Property setter for last name"""
        if isinstance(ln, str) and ln.strip():
            self.__ln = ln.strip()
        else:
            raise ValueError("Last name must be a non-empty string")

    def get_info(self):
        print("First Name:", self.__fn)
        print("Last Name:", self.__ln)


if __name__ == "__main__":
    p = Person("Manoj", "Kumar")
    p.get_info()

    # Demonstrate property access (looks like public attributes)
    print(f"First name: {p.first_name}")
    print(f"Last name: {p.last_name}")

    # Demonstrate property setters
    p.first_name = "John"
    p.last_name = "Doe"
    p.get_info()

    # This will raise an AttributeError - private attributes cannot be accessed directly
    # print(p.__fn)  # AttributeError: 'Person' object has no attribute '__fn'

    # Properties provide clean interface while keeping attributes private
    print(f"Full name: {p.first_name} {p.last_name}")

    # Demonstrate validation
    try:
        p.first_name = ""  # This will raise ValueError
    except ValueError as e:
        print(f"Validation error: {e}")

    try:
        p.last_name = 123  # This will raise ValueError
    except ValueError as e:
        print(f"Validation error: {e}")
