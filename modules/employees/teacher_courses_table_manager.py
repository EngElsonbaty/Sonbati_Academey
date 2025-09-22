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


class TeacherCoursesTableManager(BaseTemplates):
    def __init__(self) -> None:
        super().__init__("teacher_courses")
        self.rows = [
            "id",
            "teacher_id",
            "course_id",
            "class_room_id",
            "day_of_week",
            "start_time",
            "end_time",
            "fees" "created_at",
        ]

    @log_and_execute_time_with
    def create(self, emp_id: int, data: dict):
        last_id = db.get_last_row(self.table_name, "id") + 1
        data_table = {"teacher_id": emp_id}
        data_table.update(data)
        return super().create(last_id, data_table, False, 0, False, 0)

    @log_and_execute_time_with
    def update(self, emp_id: int, data: dict):
        return super().update(emp_id, data, is_teacher=True)

    @log_and_execute_time_with
    def delete(self, emp_id: int):
        return super().delete(emp_id, False, False)

    @log_and_execute_time_with
    def get(self, emp_id: int, all_data: bool = False, all_table: bool = False):
        if all_data:
            results = db.get(
                self.table_name, f"teacher_id = {emp_id}", False, True, *self.rows
            )
            return results if results != [] else None
        elif all_table:
            results = db.get(self.table_name, "", True, False, *self.rows)
            return results if results != [] else None
        else:
            results = super().get(emp_id, False, False, *self.rows)
            if results:
                data_table = {
                    "id": results[0][0],
                    "teacher_id": results[0][1],
                    "course_id": results[0][2],
                    "class_room_id": results[0][3],
                    "day_of_week": results[0][4],
                    "start_time": results[0][5],
                    "end_time": results[0][6],
                    "fees": results[0][7],
                    "created_at": results[0][8],
                }
                return data_table
            else:
                return None
