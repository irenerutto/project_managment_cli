from models.person import Person


class User(Person):
    """
    Represents a user who owns projects.

    User inherits common attributes from Person
    and adds the ability to manage projects.
    """

    # Class variable used to generate unique user IDs
    id_counter = 1

    def __init__(self, name, email):
        # Initialize inherited Person attributes
        super().__init__(name, email)

        # Assign a unique ID to each user object
        self.id = User.id_counter
        User.id_counter += 1

        # Store projects that belong to this user
        self.projects = []

    def add_project(self, project):
        """
        Add a project to this user.

        Projects are stored in the user's project list.
        """
        self.projects.append(project)

    def __str__(self):
        """
        Return a readable string representation
        of the user.
        """
        return f"User {self.id}: {self.name}"