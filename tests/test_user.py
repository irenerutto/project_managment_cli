import pytest

from models.user import User
from models.project import Project


def test_user_is_created():
    """
    Test that a User object is created correctly.
    """

    user = User("Alex", "alex@gmail.com")

    assert user.name == "Alex"
    assert user.email == "alex@gmail.com"
    assert user.projects == []


def test_user_has_unique_id():
    """
    Test that each user gets a unique ID.
    """

    user1 = User("Alex", "alex@gmail.com")
    user2 = User("Jane", "jane@gmail.com")

    assert user1.id != user2.id


def test_add_project():
    """
    Test adding a project to a user.
    """

    user = User("Alex", "alex@gmail.com")

    project = Project(
        "CLI Tool",
        "Python CLI project",
        "2026-08-01"
    )

    user.add_project(project)

    assert len(user.projects) == 1
    assert user.projects[0] == project


def test_user_string_representation():
    """
    Test the __str__ method.
    """

    user = User("Alex", "alex@gmail.com")

    assert str(user) == f"User {user.id}: Alex"