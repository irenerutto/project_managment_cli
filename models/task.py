class Task:
    """
    Represents a task within a project.

    A task stores information about the work to be completed,
    who it is assigned to, and its current completion status.
    """

    # Class variable used to create unique IDs for tasks
    id_counter = 1

    def __init__(self, title, assigned_to, status="Pending"):
        # Assign a unique ID to each task object
        self.id = Task.id_counter
        Task.id_counter += 1

        # Store task information through properties
        # so validation is applied
        self.title = title
        self.assigned_to = assigned_to
        self.status = status

    @property
    def title(self):
        """Return the task title."""
        return self._title

    @title.setter
    def title(self, value):
        """
        Validate and set the task title.

        A task must have a title that is not empty.
        """
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
        """
        Validate and set the task status.

        Tasks can only have two states:
        Pending or Completed.
        """
        valid_statuses = ["Pending", "Completed"]

        if value in valid_statuses:
            self._status = value
        else:
            raise ValueError("Status must be 'Pending' or 'Completed'.")

    def complete_task(self):
        """
        Mark the task as completed.

        Updates the status from Pending to Completed.
        """
        self.status = "Completed"

    def __str__(self):
        """
        Return a readable string representation
        of the task.
        """
        return f"Task {self.id}: {self.title} ({self.status})"