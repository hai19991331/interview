import abc
from typing import Dict, List, Tuple

from .base_database import BaseDatabase
from .settings import *


class CommonDatabase(BaseDatabase, metaclass=abc.ABCMeta):
    # Since several methods across different databases are actually just the same
    # I've built this class with the idea to reuse that logic instead of copy pasting
    # over and over the same code.

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

    def setup(self) -> None:
        """
        Called on creation or shortly afterwards.
        """
        with self.cursor() as cur:
            cur.execute(self.CREATE_TABLE)

    
    def insert_value(self,pair,batch_size: int = 10):
        values = [(currency, int(value)) for currency, value  in pair]
        with self.cursor() as cur:
            for index in range(0, len(pair), batch_size):
                cur.executemany(self.INSERT_TABLE, values[index: index + batch_size])
                

