from models.task import Task


class Project:
    """
    Represents a project containing multiple tasks.

    A project stores project details and manages
    a collection of related tasks.
    """

    # Class variable used to generate unique project IDs
    id_counter = 1

    def __init__(self, title, description, due_date):
        # Assign a unique ID to each project instance
        self.id = Project.id_counter
        Project.id_counter += 1

        # Store project information
        self.title = title
        self.description = description
        self.due_date = due_date

        # Each project starts with an empty list of tasks
        self.tasks = []

    @property
    def title(self):
        """Return the project title."""
        return self._title

    @title.setter
    def title(self, value):
        """
        Validate and set the project title.

        A project must have a title that is not empty.
        """
        if value.strip():
            self._title = value
        else:
            raise ValueError("Project title cannot be empty.")

    def add_task(self, task):
        """
        Add a task to the project.

        Tasks are stored inside the project's task list.
        """
        self.tasks.append(task)

    def list_tasks(self):
        """
        Return all tasks associated with this project.
        """
        return self.tasks

    def __str__(self):
        """
        Return a readable string representation
        of the project.
        """
        return f"Project {self.id}: {self.title}"