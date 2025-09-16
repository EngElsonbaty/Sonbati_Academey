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


class ClassRoomsTableManager(BaseTemplates):
    def __init__(self):
        super().__init__("class_rooms")
        self.rows = ["id", "classroom_name", "classroom_code", "counter"]

    @log_and_execute_time_with
    def create(self, id, data):
        return super().create(id, data, False, 0, False, 0)

    @log_and_execute_time_with
    def update(self, emp_id, data):
        return super().update(emp_id, data, False, False)

    @log_and_execute_time_with
    def delete(self, emp_id):
        return super().delete(emp_id, False, False)

    @log_and_execute_time_with
    def get(self, emp_id, all_data=False):
        if all_data:
            results = db.get(self.table_name, "", True, False, *self.rows)
            return results
        else:
            results = super().get(emp_id, False, False, *self.rows)
            if results:
                data_table = {
                    "id": results[0][0],
                    "classroom_name": results[0][1],
                    "classroom_code": results[0][2],
                    "counter": results[0][3],
                }
                return data_table
            else:
                return None
