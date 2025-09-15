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


class ExamsTableManager:
    def __init__(self) -> None:
        self.table_name = "exams"
        self.rows = [
            "id",
            "course_id",
            "teacher_id",
            "class_rooms_id",
            "finally_grade",
            "full_time",
            "start_time",
            "end_time",
            "file_pdf",
            "date",
            "create_at",
        ]

    def create(self, id: int, data: dict):
        return db.insert(self.table_name, data)

    def update(self, id: int, data: dict):
        return db.update(self.table_name, f"id = {id}", data)

    def delete(self, id: int):
        return db.delete(self.table_name, f"id = {id}")

    def get(self, id: int, all_data: bool = False, all_table: bool = False):
        if all_data:
            return db.get(self.table_name, f"course_id = {id}", False, True, *self.rows)
        elif all_table:
            return db.get(self.table_name, "", True, False, *self.rows)
        else:
            results = db.get(self.table_name, f"id = {id}", False, False, *self.rows)
            if results:
                data_table = {
                    "id": results[0][0],
                    "course_id": results[0][1],
                    "teacher_id": results[0][2],
                    "class_rooms_id": results[0][3],
                    "finally_grade": results[0][4],
                    "full_time": results[0][5],
                    "start_time": results[0][6],
                    "end_time": results[0][7],
                    "file_pdf": results[0][8],
                    "date": results[0][9],
                    "create_at": results[0][10],
                }
                return data_table
            else:
                return None
