"""
This is "__init.py" module of "models" package.

The __init__.py module makes Python treat directories\
containing the file as packages.
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
