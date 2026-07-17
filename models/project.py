from models.task import Task


class Project:
    """
    Represents a project containing multiple tasks.
    """

    id_counter = 1

    def __init__(self, title, description, due_date):
        self.id = Project.id_counter
        Project.id_counter += 1

        self.title = title
        self.description = description
        self.due_date = due_date
        self.tasks = []

    @property
    def title(self):
        """Return the project title."""
        return self._title

    @title.setter
    def title(self, value):
        """Validate the project title."""
        if value.strip():
            self._title = value
        else:
            raise ValueError("Project title cannot be empty.")

    def add_task(self, task):
        """Add a task to the project."""
        self.tasks.append(task)

    def list_tasks(self):
        """Return all tasks in the project."""
        return self.tasks

    def __str__(self):
        """Return a readable string representation of the project."""
        return f"Project {self.id}: {self.title}"