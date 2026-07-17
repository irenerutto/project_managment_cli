class Task:
    """
    Represents a task within a project.
    """

    id_counter = 1

    def __init__(self, title, assigned_to, status="Pending"):
        self.id = Task.id_counter
        Task.id_counter += 1

        self.title = title
        self.assigned_to = assigned_to
        self.status = status

    @property
    def title(self):
        """Return the task title."""
        return self._title

    @title.setter
    def title(self, value):
        """Validate the task title."""
        if value.strip():
            self._title = value
        else:
            raise ValueError("Task title cannot be empty.")

    @property
    def status(self):
        """Return the task status."""
        return self._status

    @status.setter
    def status(self, value):
        """Allow only valid task statuses."""
        valid_statuses = ["Pending", "Completed"]

        if value in valid_statuses:
            self._status = value
        else:
            raise ValueError("Status must be 'Pending' or 'Completed'.")

    def complete_task(self):
        """Mark the task as completed."""
        self.status = "Completed"

    def __str__(self):
        """Return a readable string representation of the task."""
        return f"Task {self.id}: {self.title} ({self.status})"