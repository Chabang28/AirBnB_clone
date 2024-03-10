#!/usr/bin/python3
"""
Module for the Amenity class.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Represents an Amenity.

    Attributes:
        name (str): The name of the Amenity.
    """

    def __init__(self, *args, **kwargs):
        """Initialize Amenity instance."""
        super().__init__(*args, **kwargs)
        self.name = ""

