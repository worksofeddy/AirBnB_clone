#!/usr/bin/python3
'''
represents the class BaseModel
'''
import uuid
from datetime import datetime
import models


class BaseModel:
    '''
    represents the base class
    '''
    def __init__(self, *args, **kwargs):
        '''
        Initializes the base model class
        '''
        time = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, time))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()

        models.storage.new(self)

    def save(self):
        '''
        updates the public instance attribute
        updated_at with the current datetime
        '''
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        '''
        returns a dictionary containing all
        keys/values of __dict__ of the instance
        '''
        dict_cpy = self.__dict__.copy()
        dict_cpy["__class__"] = self.__class__.__name__
        dict_cpy["created_at"] = self.created_at.isoformat()
        dict_cpy["updated_at"] = self.updated_at.isoformat()

        return dict_cpy

    def __str__(self):
        '''
        represents the string format
        '''
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
