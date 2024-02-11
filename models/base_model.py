#!/usr/bin/python3
"""
module for Base class
"""


from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """
    Base class for all models
    """

    def __init__(self, *args, **kwargs):
        """
        initialize a new instance of Base
        Args:
            args: variable length argument list
            kwargs: arbitrary keyword arguments
        """

        time = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, time))
                elif key != '__class__':
                    setattr(self, key, value)
            if 'id' not in kwargs:
                setattr(self, 'id', str(uuid.uuid4()))
            if 'created_at' not in kwargs:
                setattr(self, 'created_at', datetime.now())
            if 'updated_at' not in kwargs:
                setattr(self, 'updated_at', datetime.now())
        else:
            setattr(self, 'id', str(uuid4()))
            setattr(self, 'created_at', datetime.now())
            setattr(self, 'updated_at', datetime.now())
            models.storage.new(self)

    def __str__(self):
        """ Returns a string representation of the object.

        Returns:
            str: A string containing the class name, the object's ID, and its
            attributes.
        """

        name = self.__class__.__name__
        return "[{}] ({}) {}".format(name, self.id, self.__dict__)

    def save(self):
        """ Updates the updated_at attribute with the current timestamp.

        Returns:
            None
        """

        setattr(self, 'updated_at', datetime.now())
        models.storage.save()

    def to_dict(self):
        """ Returns a dictionary representation of the object.

        Returns:
            dict: A dictionary containing the object's attributes and the
            "__class__" key with the class name. Datetime objects are
            converted to ISO formatted strings.
        """

        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
