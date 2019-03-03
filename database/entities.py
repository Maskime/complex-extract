import os
import sqlite3
from abc import ABC, abstractmethod
from typing import List

from config import configuration
from src.application_logger import get_logger
from src.errors import ComplexExtractException

file_path = os.path.realpath(__file__)
app_path = os.path.join(file_path, '..')
database_path = os.path.join(app_path, 'database', configuration.database['name'])


class BaseEntity(ABC):
    connection: sqlite3.Connection
    logger = get_logger('main', term_log=True)


    def __init__(self) -> None:
        super().__init__()

    def open_connection(self) -> sqlite3.Connection:
        try:
            self.connection = sqlite3.connect(database=database_path)
            return self.connection
        except sqlite3.Error as e:
            self.logger.error('Error when opening db connection [%s]', e)
            raise ComplexExtractException(e)

    @abstractmethod
    def create_query(self):
        pass


class DelugeCalls(BaseEntity):
    call_id: int
    torrent_name: str
    torrent_id: str
    save_path: str

    def __init__(self) -> None:
        super().__init__()

    def create_query(self):
        return """
        CREATE TABLE IF NOT EXISTS deluge_calls (
            call_id INTEGER PRIMARY KEY,
            torrent_name text not null,
            torrent_id text not null,
            save_path text not null
        );
        """

    def insert(self, torrent_name, torrent_id, save_path) -> int:
        self.torrent_id = torrent_id
        self.torrent_name = torrent_name
        self.save_path = save_path
        try:
        except ComplexExtractException:
        finally:

