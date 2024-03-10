#!/usr/bin/python3
"""
Initialize a unique FileStorage instance for the hbnb application.
"""
from models.engine.file_storage import FileStorage

# Create a single instance of FileStorage
storage = FileStorage()

# Ensure data is loaded into the storage instance
storage.reload()

