import pytest

from models.task import Task


def test_task_is_created():
    """
    Test that a Task object is created correctly.
    """

    task = Task(
        "Write tests",
        "Alex"
    )

    assert task.title == "Write tests"
    assert task.assigned_to == "Alex"
    assert task.status == "Pending"


def test_empty_task_title():
    """
    Test that an empty task title raises a ValueError.
    """

    with pytest.raises(ValueError):
        Task(
            "",
            "Alex"
        )


def test_invalid_status():
    """
    Test that an invalid status raises a ValueError.
    """

    with pytest.raises(ValueError):
        Task(
            "Write tests",
            "Alex",
            "Finished"
        )


def test_complete_task():
    """
    Test that complete_task changes the status.
    """

    task = Task(
        "Write tests",
        "Alex"
    )

    task.complete_task()

    assert task.status == "Completed"


def test_task_string_representation():
    """
    Test the __str__ method.
    """

    task = Task(
        "Write tests",
        "Alex"
    )

    assert str(task) == f"Task {task.id}: Write tests (Pending)"