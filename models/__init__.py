from .engine.file_storage import FileStorage
from .engine.db_storage import DBStorage
import os

storage_type = os.getenv('HBNB_TYPE_STORAGE')

if storage_type == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()
