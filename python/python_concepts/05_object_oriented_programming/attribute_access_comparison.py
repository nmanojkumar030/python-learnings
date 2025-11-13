"""Comprehensive Comparison of Public, Protected, and Private Attributes"""


# 1. PUBLIC ATTRIBUTES (no underscore)
class PersonPublic:
    def __init__(self, fn, ln):
        self.fn = fn  # Public attribute
        self.ln = ln  # Public attribute

    def get_info(self):
        print("First Name:", self.fn)
        print("Last Name:", self.ln)


# 2. PROTECTED ATTRIBUTES (single underscore)
class PersonProtected:
    def __init__(self, fn, ln):
        self._fn = fn  # Protected attribute (convention)
        self._ln = ln  # Protected attribute (convention)

    def get_first_name(self):
        return self._fn

    def set_first_name(self, fn):
        if isinstance(fn, str) and fn.strip():
            self._fn = fn.strip()
        else:
            raise ValueError("First name must be a non-empty string")

    def get_last_name(self):
        return self._ln

    def set_last_name(self, ln):
        if isinstance(ln, str) and ln.strip():
            self._ln = ln.strip()
        else:
            raise ValueError("Last name must be a non-empty string")

    def get_info(self):
        print("First Name:", self._fn)
        print("Last Name:", self._ln)


# 3. PRIVATE ATTRIBUTES (double underscore)
class PersonPrivate:
    def __init__(self, fn, ln):
        self.__fn = fn  # Private attribute (name mangling)
        self.__ln = ln  # Private attribute (name mangling)

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
    print("=" * 60)
    print("COMPARISON OF ATTRIBUTE ACCESS LEVELS")
    print("=" * 60)

    # Test Public Attributes
    print("\n1. PUBLIC ATTRIBUTES (self.fn, self.ln)")
    print("-" * 40)
    p1 = PersonPublic("Manoj", "Kumar")

    print("✓ Direct access works:")
    print(f"  p1.fn = {p1.fn}")
    print(f"  p1.ln = {p1.ln}")

    print("✓ Direct modification works (no validation):")
    p1.fn = ""
    p1.ln = 123
    print(f"  After modification: p1.fn = '{p1.fn}', p1.ln = {p1.ln}")

    # Test Protected Attributes
    print("\n2. PROTECTED ATTRIBUTES (self._fn, self._ln)")
    print("-" * 40)
    p2 = PersonProtected("Manoj", "Kumar")

    print("✓ Getter/setter methods work:")
    print(f"  p2.get_first_name() = {p2.get_first_name()}")
    print(f"  p2.get_last_name() = {p2.get_last_name()}")

    print("⚠ Direct access works (but not recommended):")
    print(f"  p2._fn = {p2._fn}")
    print(f"  p2._ln = {p2._ln}")

    print("✓ Validation in setters:")
    try:
        p2.set_first_name("")
    except ValueError as e:
        print(f"  Validation error: {e}")

    # Test Private Attributes
    print("\n3. PRIVATE ATTRIBUTES (self.__fn, self.__ln)")
    print("-" * 40)
    p3 = PersonPrivate("Manoj", "Kumar")

    print("✓ Property access works:")
    print(f"  p3.first_name = {p3.first_name}")
    print(f"  p3.last_name = {p3.last_name}")

    print("✗ Direct access fails:")
    try:
        print(f"  p3.__fn = {p3.__fn}")
    except AttributeError as e:
        print(f"  AttributeError: {e}")

    print("✓ Validation in property setters:")
    try:
        p3.first_name = ""
    except ValueError as e:
        print(f"  Validation error: {e}")

    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print("Public (self.fn):     Direct access ✓, No validation ✗")
    print("Protected (self._fn): Direct access ⚠, Convention only")
    print("Private (self.__fn):  Direct access ✗, Name mangling ✓")
    print(
        "\nRecommendation: Use private attributes with properties for best encapsulation!"
    )
