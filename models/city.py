#!/usr/bin/python3
"""
Module for the City class, inheriting from BaseModel.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Represents a City.

    Attributes:
        state_id (str): The ID of the state to which the city belongs.
        name (str): The name of the city.
    """

    def __init__(self, *args, **kwargs):
        """Initializes City."""
        super().__init__(*args, **kwargs)
        self.state_id = ""
        self.name = ""
