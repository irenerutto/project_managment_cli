import pytest

from models.project import Project
from models.task import Task


def test_project_is_created():
    """
    Test that a Project object is created correctly.
    """

    project = Project(
        "CLI Tool",
        "Python CLI project",
        "2026-08-01"
    )

    assert project.title == "CLI Tool"
    assert project.description == "Python CLI project"
    assert project.due_date == "2026-08-01"
    assert project.tasks == []


def test_empty_project_title():
    """
    Test that an empty title raises a ValueError.
    """

    with pytest.raises(ValueError):
        Project(
            "",
            "Description",
            "2026-08-01"
        )


def test_add_task():
    """
    Test adding a task to a project.
    """

    project = Project(
        "CLI Tool",
        "Python CLI project",
        "2026-08-01"
    )

    task = Task(
        "Write tests",
        "Alex"
    )

    project.add_task(task)

    assert len(project.tasks) == 1
    assert project.tasks[0] == task


def test_list_tasks():
    """
    Test listing project tasks.
    """

    project = Project(
        "CLI Tool",
        "Python CLI project",
        "2026-08-01"
    )

    task = Task(
        "Write tests",
        "Alex"
    )

    project.add_task(task)

    assert project.list_tasks() == [task]


def test_project_string_representation():
    """
    Test the __str__ method.
    """

    project = Project(
        "CLI Tool",
        "Python CLI project",
        "2026-08-01"
    )

    assert str(project) == f"Project {project.id}: CLI Tool"