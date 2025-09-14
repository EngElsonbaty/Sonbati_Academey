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
from modules.students.base_tamplates_students import BaseTemplatesStudents
from modules.database_manager import db
from datetime import datetime

# Import the custom decorator 'log_and_execute_time_with' from the logging utilities module.
from core.log_utils import log_and_execute_time_with


class StudentDetailsTableManager(BaseTemplatesStudents):
    def __init__(self) -> None:
        super().__init__("student_details")
        self.rows = [
            "id",
            "student_id",
            "address",
            "nationality_id",
            "governorate_id",
            "email",
            "phone_number",
            "fees",
        ]

    def create(self, id: int, student_id: int, data: dict):
        return super().create(id, student_id, data)

    def update(self, student_id: int, data: dict):
        return super().update(student_id, data)

    def delete(self, student_id: int):
        return super().delete(student_id)

    def get(self, student_id: int):
        return super().get(student_id, True, False, False, *self.rows)
