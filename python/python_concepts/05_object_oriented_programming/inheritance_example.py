"""Base Class"""


class Person:

    def __init__(self, fn, ln):
        self.fn = fn
        self.ln = ln

    def get_info(self):
        print("First Name:", self.fn)
        print("Last Name:", self.ln)


if __name__ == "__main__":
    p = Person("Manoj", "Kumar")
    p.get_info()
    print(f"Person first_name: {p.fn} and last_name: {p.ln}")


"""Derived Class 
Employee extends Person"""


class Employee(Person):

    # pass
    def __init__(self, eid, fn, ln):
        self.eid = eid
        super().__init__(fn, ln)

    def get_info(self):
        print("employee id :", self.eid)
        super().get_info()  # Invoke overriden method


if __name__ == "__main__":
    # e = Employee("Guido", "rossum")
    e = Employee(1, "Guido", "rossum")
    e.get_info()
