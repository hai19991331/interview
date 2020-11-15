import os
import sys
from typing import Dict, List, Tuple

from .base_database import DatabaseFactory

class Music_id_database:
    def __init__(self, config):
        self.config = config

        # initialize db
        db_cls = DatabaseFactory.get_database(config.get("database_type", "mysql").lower())

        self.db = db_cls(**config.get("database", {}))
        self.db.setup()


