import abc
import importlib
from typing import Dict, List, Tuple, Union
from .settings import *


class BaseDatabase(object, metaclass=abc.ABCMeta):
    # Name of your Database subclass, this is used in configuration
    # to refer to your class
    type = None
    autocommit = True
    _cursor = None

    def __init__(self):
        super().__init__()


    def before_fork(self) -> None:
        """
        Called before the database instance is given to the new process
        """
        pass

    def after_fork(self) -> None:
        """
        Called after the database instance has been given to the new process

        This will be called in the new process.
        """
        pass

    def setup(self,sql_file) -> None:
        """
        Called on creation or shortly afterwards.
        """
        pass
    
    def insert_value(self,pair,batch_size: int = 10):
        pass

    # ------------------------------------------END UPDATE------------------------------------------


class DatabaseFactory():
    @staticmethod
    def get_database(database_type: str = "mysql") -> BaseDatabase:
        """
        Given a database type it returns a database instance for that type.

        :param database_type: type of the database.
        :return: an instance of BaseDatabase depending on given database_type.
        """
        try:
            path, db_class_name = DATABASES[database_type]
            print(path)
            db_module = importlib.import_module(path)
            print(db_module)
            db_class = getattr(db_module, db_class_name)
            return db_class
        except (ImportError, KeyError):
            message = "Unsupported database type supplied."
            raise TypeError(message)
