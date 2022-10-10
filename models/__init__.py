#!/usr/bin/python3
"""This module instantiates an object of class FileStorage
or DBStorage"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
import os

storage = DBStorage() if os.getenv(
    'HBNB_TYPE_STORAGE') == 'db' else FileStorage()
"""A unique FileStorage/DBStorage instance for all models.
"""
storage.reload()


storage.reload()
