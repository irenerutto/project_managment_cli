class Person:
    """
    This is Base class representing a person.

    This class stores common information shared by users,
    such as name and email, and validates the values
    using properties.
    """

    def __init__(self, name, email):
        # Assign values through properties so validation runs
        self.name = name
        self.email = email

    @property
    def name(self):
        """
        Returns the person's name.
        """
        return self._name

    @name.setter
    def name(self, value):
        """
        Validates and sets the person's name.

        A name cannot be empty.
        """
        if value.strip():
            self._name = value
        else:
            raise ValueError("Name cannot be empty.")

    @property
    def email(self):
        """
        Returns the person's email address.
        """
        return self._email

    @email.setter
    def email(self, value):
        """
        Validates and sets the person's email.

        The email must contain an @ symbol.
        """
        if "@" in value:
            self._email = value
        else:
            raise ValueError("Invalid email address.")

    def __str__(self):
        """
        Returns a readable string representation
        of the person object.
        """
        return f"{self.name} ({self.email})"