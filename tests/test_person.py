import pytest

from models.person import Person


def test_person_is_created():
    """Test that a Person object is created correctly."""

    person = Person("Alex", "alex@gmail.com")

    assert person.name == "Alex"
    assert person.email == "alex@gmail.com"


def test_empty_name_raises_error():
    """Test that an empty name raises a ValueError."""

    with pytest.raises(ValueError):
        Person("", "alex@gmail.com")


def test_invalid_email_raises_error():
    """Test that an invalid email raises a ValueError."""

    with pytest.raises(ValueError):
        Person("Alex", "alexgmail.com")


def test_string_representation():
    """Test the __str__ method."""

    person = Person("Alex", "alex@gmail.com")

    assert str(person) == "Alex (alex@gmail.com)"