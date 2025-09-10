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

# Import the custom decorator 'log_and_execute_time_with' from the logging utilities module.
from core.log_utils import log_and_execute_time_with


class AttendanceEmployeeTableManager(BaseTemplates):
    def __init__(self):
        super().__init__("attendance_employee")
        self.rows = ["id", "emp_id", "type", "time", "created_at"]

    def create(
        self, id, data, subtable=False, emp_id=0, permission_module=False, role_id=0
    ):
        return super().create(id, data, subtable, emp_id, permission_module, role_id)

    def get(self, emp_id):
        return super().get(emp_id, True, *self.rows)
