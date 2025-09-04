import os
import sys
import sqlite3


class DatabaseManager:
    __conn_db = None

    def __init__(self):
        pass

    @staticmethod
    def get_path():
        pass

    @staticmethod
    def get_connection():
        pass

    @property
    def save(self):
        pass

    @property
    def close(self):
        pass

    def create_table(self):
        pass

    def insert(self):
        pass

    def delete(self):
        pass

    def update(self):
        pass

    def get(self):
        pass

    def search(self):
        pass

    def get_last_row(self):
        pass
