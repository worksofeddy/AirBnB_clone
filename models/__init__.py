#!/usr/bin/python3
'''
import file_storage.py
create the variable storage, an instance of FileStorage
call reload() method on this variable
'''
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
