#!/usr/bin/python3
"""This module instantiates the storage based on the environment variable """
from os import getenv


storage_type = getenv('HBNB_TYPE_STORAGE')

if storage_type == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

# Reload the storage
storage.reload()
