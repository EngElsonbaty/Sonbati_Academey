# This module defines the BaseTemplates class, a generic manager for
# database tables. It provides reusable methods for common database operations (CRUD).
# By inheriting from this class, other table managers (e.g., EmployeesTableManager)
# can reuse this core logic without code duplication.

# The 'os' module provides functions for interacting with the operating system.
import os

# The 'sys' module provides access to system-specific parameters and functions.
import sys

# Get the directory of the current file (__file__).
path_modules = os.path.dirname(os.path.dirname(__file__))
# Get the parent directory of 'path_modules', which is the root of the project.
root_path = os.path.dirname(path_modules)
# Add the 'modules' directory to the Python path to allow imports from it.
sys.path.append(path_modules)
# Add the project's root directory to the Python path.
sys.path.append(root_path)

# Import the custom decorator 'log_and_execute_time_with' from the logging utilities module.
from core.log_utils import log_and_execute_time_with

# Import the 'db' object from the database manager module, which handles
# connections and queries.
from modules.database_manager import db


class BaseTemplatesStudents:
    def __init__(self, table_name: str) -> None:
        self.table_name = table_name

    def create(self, id: int, student_id: int, data: dict):
        data_table = {
            "id": id,
            "student_id": student_id,
        }
        data_table.update(data)
        return db.insert(self.table_name, data_table)

    def update(self, student_id: int, data: dict):
        if self.table_name == "students":
            return db.update(self.table_name, f"id = {student_id}", data)
        else:
            return db.update(self.table_name, f"student_id = {student_id}", data)

    def delete(self, student_id: int):
        if self.table_name == "students":
            return db.delete(self.table_name, f"id = {student_id}")
        else:
            return db.delete(self.table_name, f"student_id = {student_id}")

    def get(
        self,
        student_id: int,
        submodule: bool = False,
        all_data: bool = False,
        all_table: bool = False,
        *rows,
    ):
        if all_data:
            if submodule:
                return db.get(
                    self.table_name, f"student_id = {student_id}", False, True, *rows
                )
            else:
                return db.get(self.table_name, f"id = {student_id}", False, True, *rows)
        elif all_table:
            return db.get(self.table_name, "", True, False, *rows)
        else:
            if submodule:
                return db.get(
                    self.table_name, f"student_id = {student_id}", False, False, *rows
                )
            else:
                return db.get(
                    self.table_name, f"id = {student_id}", False, False, *rows
                )
