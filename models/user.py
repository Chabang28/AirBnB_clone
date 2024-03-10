#!/usr/bin/python3
"""A class User that inherits from BaseModel"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    Represents a user.

    Attributes:
        email (str): The email address of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """

    def __init__(self, *args, **kwargs):
        """Initializes a User instance."""
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""

