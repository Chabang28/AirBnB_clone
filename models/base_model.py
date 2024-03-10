#!/usr/bin/python3
"""
Attributes/Methods for BaseClass
- Public instance attributes:
    - id
    - created_at: datetime - assigned with the current datetime
    - updated_at: datetime - assigned with the current datetime
- Public instance methods:
    - save(self)
    - to_dict(self)
"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """BaseModel class serving as the foundation for other models"""

    def __init__(self, *args, **kwargs):
        """Initializes a new instance of BaseModel."""
        date_format = "%Y-%m-%dT%H:%M:%S.%f"

        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        value = datetime.strptime(value, date_format)
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        '''String representation of BaseModel instance'''
        return "[{}] ({}) {}".format(type(self).__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Updates the 'updated_at' instance attribute"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary representation of the instance."""
        base_dict = self.__dict__.copy()
        base_dict['created_at'] = self.created_at.isoformat()
        base_dict['updated_at'] = self.updated_at.isoformat()
        base_dict['__class__'] = type(self).__name__
        return base_dict
