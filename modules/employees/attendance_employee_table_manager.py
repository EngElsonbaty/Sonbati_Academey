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

# Import the custom decorator 'log_and_execute_time_with' from the logging utilities module.
from core.log_utils import log_and_execute_time_with


class AttendanceEmployeeTableManager(BaseTemplates):
    def __init__(self):
        super().__init__("attendance_employee")
        self.rows = ["id", "emp_id", "type", "time", "created_at"]

    @log_and_execute_time_with
    def create(self, emp_id: int, data: dict):
        last_id = db.get_last_row(self.table_name, "id") + 1
        return super().create(last_id, data, True, emp_id)

    @log_and_execute_time_with
    def update(self, emp_id: int, data: dict):
        return super().update(emp_id, data, True, False)

    @log_and_execute_time_with
    def delete(self, emp_id: int):
        return super().delete(emp_id, True, False, False)

    @log_and_execute_time_with
    def get(self, emp_id: int, all_data: bool = False, all_table: bool = False):
        if all_data:
            return db.get(
                self.table_name, f"emp_id = {emp_id}", False, True, *self.rows
            )
        elif all_table:
            return db.get(self.table_name, "", True, False, *self.rows)
        else:
            results = db.get(
                self.table_name, f"id = {emp_id}", False, False, *self.rows
            )
            if results:
                data_table = {
                    "id": results[0][0],
                    "emp_id": results[0][1],
                    "type": results[0][2],
                    "time": results[0][3],
                    "created_at": results[0][4],
                }
                return data_table
            else:
                return False
