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


class EvaluationEmployeeTableManager(BaseTemplates):
    def __init__(self):
        super().__init__("evaluation_employee")
        self.rows = ["id", "emp_id", "evaluation_type", "rating", "created_at"]

    @log_and_execute_time_with
    def create(self, id, data, emp_id=0):
        return super().create(id, data, True, emp_id)

    @log_and_execute_time_with
    def update(self, emp_id, data):
        return super().update(emp_id, data, True)

    @log_and_execute_time_with
    def delete(self, emp_id):
        return super().delete(emp_id, True)

    @log_and_execute_time_with
    def get(self, emp_id, *rows):
        return super().get(emp_id, True, False, *self.rows)
