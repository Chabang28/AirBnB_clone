#!/usr/bin/python3
"""
Module for the Review class.
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Represents a customer review.

    Attributes:
        place_id (str): The ID of the place the review is for.
        user_id (str): The ID of the user who wrote the review.
        text (str): The content of the review.
    """

    def __init__(self, *args, **kwargs):
        """Initializes a Review instance."""
        super().__init__(*args, **kwargs)
        self.place_id = ""
        self.user_id = ""
        self.text = ""

