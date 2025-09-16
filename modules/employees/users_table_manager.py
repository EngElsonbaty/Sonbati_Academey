"""
This file contains the UserTableManager class, which is responsible for managing user data in the database.

It provides a clear and consistent interface for creating, updating, deleting, and retrieving
user records by inheriting from a base class.
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
# Imports the base class for table management, which provides core database functionalities.
from modules.base_tamplates import BaseTemplates
from modules.database_manager import db

# Import the custom decorator 'log_and_execute_time_with' from the logging utilities module.
# Imports a custom decorator used for logging function execution time.
from core.log_utils import log_and_execute_time_with


class UserTableManager(BaseTemplates):
    """
    Manages all database operations for the 'users' table.

    This class provides a clear and consistent interface for creating, updating,
    deleting, and retrieving user records. It inherits its core database logic
    from the BaseTemplates class to ensure consistency and reusability.
    """

    def __init__(self):
        """
        Initializes the class by setting the table name and columns.

        This constructor defines the table name and the list of columns to work with,
        then calls the parent class's initializer to complete the setup.
        """
        # Defines the name of the database table this manager will handle.
        self.table_name = "users"
        # Defines a list of the primary columns that this class will work with.
        self.rows = [
            "id",
            "emp_id",
            "username",
            "password",
        ]
        # Calls the parent class's initializer, passing the table name.
        super().__init__(self.table_name)

    @log_and_execute_time_with
    def create(self, data, emp_id=0):
        """
        Creates a new record in the 'users' table.

        Args:
            id (int): The unique identifier for the new record.
            data (dict): A dictionary containing the user data to be added.
            subtable (bool, optional): An optional flag indicating if this is a subtable. Defaults to False.
            emp_id (int, optional): The employee's unique identifier. Defaults to 0.

        Returns:
            any: The result of the create operation from the parent class.
        """
        # Initializes a dictionary to hold the record's data, starting with the ID.
        # data_table = {"id": id}
        # # Checks if a valid employee ID was provided.
        # if subtable:
        #     # Adds the employee ID to the data dictionary.
        #     data_table.update({"emp_id": emp_id})
        # # Merges the provided user data into the final data dictionary.
        # data_table.update(data)
        # Returns the result of calling the parent's create method with the prepared data.
        record_id = db.get_last_row(self.table_name, "id") + 1
        return super().create(record_id, data, True, emp_id)

    @log_and_execute_time_with
    def update(self, emp_id, data):
        """
        Updates an existing user record in the 'users' table.

        Args:
            emp_id (int): The ID of the employee whose user data will be updated.
            data (dict): A dictionary containing the data to be updated.

        Returns:
            any: The result of the update operation from the parent class.
        """
        # Returns the result of calling the parent's update method with the employee ID and new data.
        return super().update(emp_id, data, True)

    @log_and_execute_time_with
    def delete(self, emp_id):
        """
        Deletes a user record from the 'users' table.

        Args:
            emp_id (int): The ID of the employee whose user record will be deleted.

        Returns:
            any: The result of the delete operation from the parent class.
        """
        # Returns the result of calling the parent's delete method with the employee ID.
        return super().delete(emp_id, True, False)

    @log_and_execute_time_with
    def get(self, emp_id):
        """
        Retrieves a user's data from the database.

        Args:
            emp_id (int): The ID of the employee whose user data to retrieve.

        Returns:
            dict or None: A dictionary containing the user data if found, otherwise None.
        """
        # Calls the parent's get method to fetch data from the specified columns based on employee ID.
        results = super().get(emp_id, True, False, *self.rows)
        # Initializes a variable to hold the user data, defaulting to None.
        data_user = None
        # Checks if the database query returned any results.
        if results is not None:
            # Creates a dictionary from the fetched tuple for easier data access by name.
            data_user = {
                "id": results[0][0],
                "emp_id": results[0][1],
                "username": results[0][2],
                "password": results[0][3],
            }
        # Returns the final dictionary of user data or None.
        return data_user
