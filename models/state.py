#!/usr/bin/python3
"""State class inheriting from BaseModel"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    Represents a geographical state.

    Attributes:
        name (str): The name of the state.
    """

    def __init__(self, *args, **kwargs):
        """Initializes a State instance."""
        super().__init__(*args, **kwargs)
        self.name = ""
