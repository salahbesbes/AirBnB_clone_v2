#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os

storage_type = os.getenv('HBNB_TYPE_STORAGE', default='file')
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel, Base

print(storage_type)
if storage_type == 'db':
    storage = DBStorage()
    storage.reload()
else:
    storage = FileStorage()
    storage.reload()
    Base = {}
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.user import User
from models.review import Review
from models.city import City
