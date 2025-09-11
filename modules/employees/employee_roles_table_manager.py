"""
This file contains the EmployeeRolesTableManager class for managing employee roles data in the database.

It provides methods to create, update, delete, and retrieve employee roles, inheriting
generic database management logic from a base class.
"""

# The 'os' module provides functions for interacting with the operating system.
import os

# The 'sys' module provides access to system-specific parameters and functions.
import sys

# Get the absolute path of the directory containing the current file.
# The 'os.path.dirname' function is called three times to navigate up
# the directory tree to the project's root folder.
# This code block determines the absolute path to the project's root directory.
root_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
# Add the project's root directory to the Python path.
# This allows for direct imports from any location within the project.
# Adds the project's root path to the Python system path for module imports.
sys.path.append(root_path)
# Import the custom BaseTemplates class from the base_templates module.
# This class provides the generic database management logic.
# Imports the base class for table management, providing core database functionalities.
from modules.base_tamplates import BaseTemplates

# Import the custom decorator 'log_and_execute_time_with' from the logging utilities module.
# Imports a custom decorator used for logging function execution time.
from core.log_utils import log_and_execute_time_with


class EmployeeRolesTableManager(BaseTemplates):
    """
    Manages all database operations for the 'employee_roles' table.

    This class provides a clear and consistent interface for creating, updating,
    deleting, and retrieving employee role records. It inherits its core
    database logic from the BaseTemplates class.
    """

    def __init__(self):
        """
        Initializes the class by setting the primary table name.

        This constructor calls the parent class's initializer and defines the
        list of primary columns for this specific table.
        """
        # Calls the parent class's initializer, passing the table name 'employee_roles'.
        super().__init__("employee_roles")
        # Defines a list of the primary columns that this class will work with.
        self.rows = [
            "id",
            "emp_id",
            "role_id",
        ]

    def create(self, id, data, emp_id=0):
        """
        Creates a new record in the 'employee_roles' table.

        Args:
            id (int): The unique identifier for the new record.
            data (dict): A dictionary containing the role data to be added.
            subtable (bool, optional): An optional flag indicating if this is a subtable. Defaults to False.
            emp_id (int, optional): The employee's unique identifier. Defaults to 0.

        Returns:
            any: The result of the create operation from the parent class.
        """
        # Returns the result of calling the parent's create method with the prepared data.
        return super().create(id, data, True, emp_id)

    def update(self, emp_id, data):
        """
        Updates an existing record in the 'employee_roles' table.

        Args:
            emp_id (int): The ID of the employee whose role data will be updated.
            data (dict): A dictionary containing the data to be updated.

        Returns:
            any: The result of the update operation from the parent class.
        """
        # Returns the result of calling the parent's update method with the employee ID and new data.
        return super().update(emp_id, data, True)

    def delete(self, emp_id):
        """
        Deletes a record from the 'employee_roles' table.

        Args:
            emp_id (int): The ID of the employee whose role record will be deleted.

        Returns:
            any: The result of the delete operation from the parent class.
        """
        # Returns the result of calling the parent's delete method with the employee ID.
        return super().delete(emp_id, True)

    def get(self, emp_id):
        """
        Retrieves an employee's role data from the database.

        Args:
            emp_id (int): The ID of the employee to retrieve.

        Returns:
            dict or None: A dictionary containing the role data if found, otherwise None.
        """
        # Initializes a variable to hold the role data, defaulting to None.
        data_roles = None
        # Calls the parent's get method to fetch data from the specified columns based on employee ID.
        results = super().get(emp_id, True, False, *self.rows)
        # Checks if the database query returned any results.
        if results is not None:
            # Creates a dictionary from the fetched tuple for easier data access by name.
            data_roles = {
                "id": results[0][0],
                "emp_id": results[0][1],
                "role_id": results[0][2],
            }
        # Returns the final dictionary of role data or None.
        return data_roles
