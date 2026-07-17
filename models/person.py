class Person:
    """
    Base class representing a person.
    """

    def __init__(self, name, email):
        self.name = name
        self.email = email

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value.strip():
            self._name = value
        else:
            raise ValueError("Name cannot be empty.")

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if "@" in value:
            self._email = value
        else:
            raise ValueError("Invalid email address.")

    def __str__(self):
        return f"{self.name} ({self.email})"