#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os

storage_type = os.getenv('HBNB_TYPE_STORAGE', default='file')
if storage_type == 'db':
    storage = DBStorage()
    from models.engine.db_storage import DBStorage
    storage.reload()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
    Base = {}
