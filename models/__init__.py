#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""

import os

storage_type = os.getenv('HBNB_TYPE_STORAGE', default='file')

if storage_type == 'db':
    from models.engine.db_storage import DBStorage

    storage = DBStorage()
    storage.reload()
else:
    from models.engine.file_storage import FileStorage

    storage = FileStorage()
    storage.reload()
    Base = {}

from models.base_model import BaseModel
from models.state import State
from models.place import Place
from models.user import User
from models.amenity import Amenity
from models.review import Review
from models.city import City
