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

from config.tables import employees


class BaseTemplates:
    """
    A generic base class for managing database tables.

    This class provides a template for common database operations such as create, update, delete,
    and get. It is designed to be inherited by other table-specific classes.
    """

    # The __init__ method is the constructor for the class.
    def __init__(self, table_name: str) -> None:
        """
        Initializes the BaseTemplates manager with a specific table name.

        Args:
            table_name (str): The name of the database table to be managed.
        """
        # Store the provided table name as an instance variable.
        self.table_name = table_name

    # The decorator logs and times the execution of the 'create' method.
    @log_and_execute_time_with
    # The 'create' method inserts a new record into the database table.
    def create(self, id: int, data: dict, subtable: bool = False, emp_id: int = 0):
        # Create a new dictionary and add the employee ID to it.
        employee_data = {"id": id}
        if subtable:
            employee_data.update({"emp_id": emp_id})
        # Update the dictionary with the provided data (e.g., name, age).
        employee_data.update(data)
        # Call the 'insert' method from the 'db' object to add the record.
        return db.insert(self.table_name, employee_data)

    # The decorator logs and times the execution of the 'update' method.
    @log_and_execute_time_with
    # The 'update' method modifies an existing record in the database.
    def update(self, emp_id: int, data: dict):
        # Call the 'update' method from the 'db' object.
        # It updates the record where the id matches the provided employee ID.
        return db.update(self.table_name, f"id = {emp_id}", data)

    # The decorator logs and times the execution of the 'delete' method.
    @log_and_execute_time_with
    # The 'delete' method removes a record from the database.
    def delete(self, emp_id: int, submodule: bool = False):
        # Call the 'delete' method from the 'db' object.
        # It deletes the record where the id matches the provided employee ID.
        if submodule:
            return db.delete(self.table_name, f"emp_id = {emp_id}")
        else:
            return db.delete(self.table_name, f"id = {emp_id}")

    # The decorator logs and times the execution of the 'get' method.
    @log_and_execute_time_with
    # The 'get' method retrieves a single record from the database.
    def get(self, emp_id: int, *rows):
        # Call the 'get' method from the 'db' object to retrieve the record.
        # 'False' indicates that we are not performing a search operation, and '*rows' allows for
        # fetching specific columns.
        results = db.get(self.table_name, f"id = {emp_id}", False, False, *rows)
        # Check if the results list is not empty.
        # If results are found, return the results; otherwise, return None.
        return results if results != [] else None
