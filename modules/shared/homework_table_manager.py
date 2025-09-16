# The 'os' module provides functions for interacting with the operating system.
import os

# The 'sys' module provides access to system-specific parameters and functions.
import sys

from datetime import datetime

# Get the absolute path of the directory containing the current file.
# The 'os.path.dirname' function is called three times to navigate up
# the directory tree to the project's root folder.
root_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
# Add the project's root directory to the Python path.
# This allows for direct imports from any location within the project.
sys.path.append(root_path)
# Import the custom BaseTemplates class from the base_templates module.
# This class provides the generic database management logic.
from modules.base_tamplates import BaseTemplates
from modules.database_manager import db

# Import the custom decorator 'log_and_execute_time_with' from the logging utilities module.
from core.log_utils import log_and_execute_time_with


class HomeworkTableManager:
    def __init__(self) -> None:
        self.table_name = "homework"
        self.rows = [
            "id",
            "course_id",
            "teacher_id",
            "class_room_id",
            "file_pdf",
            "finally_grade",
            "date",
            "create_at",
        ]

    @log_and_execute_time_with
    def create(self, id: int, data: dict):
        return db.insert(self.table_name, data)

    @log_and_execute_time_with
    def update(self, id: int, data: dict):
        return db.update(self.table_name, f"id = {id}", data)

    @log_and_execute_time_with
    def delete(self, id: int):
        return db.delete(self.table_name, f"id = {id}")

    @log_and_execute_time_with
    def get(self, id: int, all_data: bool = False, all_table: bool = False):
        if all_data:
            return db.get(self.table_name, f"course_id = {id}", False, True, *self.rows)
        elif all_table:
            return db.get(self.table_name, "", True, False, *self.rows)
        else:
            return db.get(self.table_name, f"id = {id}", False, False, *self.rows)
