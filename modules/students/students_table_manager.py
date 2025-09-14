# The 'os' module provides functions for interacting with the operating system.
import os

# The 'sys' module provides access to system-specific parameters and functions.
import sys

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
from datetime import datetime

# Import the custom decorator 'log_and_execute_time_with' from the logging utilities module.
from core.log_utils import log_and_execute_time_with


class StudentsTableManager(BaseTemplates):
    def __init__(self) -> None:
        super().__init__("students")
        self.rows = [
            "id",
            "full_name",
            "national_id",
            "birthday",
            "gender",
            "id_photo",
            "photo",
        ]

    def create(self, id: int, data: dict):
        return super().create(id, data, False, 0, False, 0)

    def update(
        self, emp_id: int, data: dict, subtable: bool = False, role: bool = False
    ):
        return super().update(emp_id, data, subtable, role)

    def delete(self, emp_id: int, submodule: bool = False, role: bool = False):
        return super().delete(emp_id, submodule, role)

    def get(self, emp_id: int, all_table: bool = False):
        if all_table:
            results = db.get(self.table_name, "", True, False, *self.rows)
            return results
        else:
            results = super().get(emp_id, False, False, *self.rows)
            if results:
                data_table = {
                    "id": results[0][0],
                    "full_name": results[0][1],
                    "national_id": results[0][2],
                    "birthday": results[0][3],
                    "gender": results[0][4],
                    "id_photo": results[0][5],
                    "photo": results[0][6],
                }
                return data_table
            else:
                return None
