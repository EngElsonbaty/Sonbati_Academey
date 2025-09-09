"""
This file contains the UserOperationTableManager class, which is responsible for
managing user operation logs in the database.

It provides methods to create new operation logs and retrieve existing ones
for auditing and reporting purposes.
"""

# The 'os' module provides functions for interacting with the operating system.
import os

# The 'sys' module provides access to system-specific parameters and functions.
import sys

# Imports the datetime class from the datetime module to handle timestamps.
from datetime import datetime

# Gets the absolute path of the directory containing the current file.
# The 'os.path.dirname' function is called three times to navigate up
# the directory tree to the project's root folder.
# This code block determines the absolute path to the project's root directory.
root_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
# Adds the project's root directory to the Python path.
# This allows for direct imports from any location within the project.
# Adds the project's root path to the Python system path for module imports.
sys.path.append(root_path)

# Imports a custom decorator used for logging function execution time.
from core.log_utils import log_and_execute_time_with, log_and_execute_time_without

# Imports the database connection object and the DatabaseManager class.
from modules.database_manager import db, DatabaseManager

# Imports the list of roles from the configuration file.
from config.data import roles


class UserOperationTableManager:
    """
    Manages all database operations for the 'user_operation' table.

    This class is responsible for logging user actions and retrieving those logs
    for auditing or reporting purposes.
    """

    def __init__(self):
        """
        Initializes the class by setting the table name and the list of columns.
        """
        # Assigns the name of the database table to a class variable.
        self.table_name = "user_operation"
        # Defines the list of primary columns for this table.
        self.rows = [
            "id",
            "emp_id",
            "operation_type",
            "details",
            "date",
        ]

    def create(self, emp_id: int, oper_type: str, details: str):
        """
        Creates a new record (log entry) in the 'user_operation' table.

        Args:
            emp_id (int): The ID of the employee performing the operation.
            oper_type (str): The type of operation (e.g., 'login', 'update').
            details (str): A string containing specific details of the operation.

        Returns:
            any: The result of the insert operation from the database manager.
        """
        # Gets the ID of the last row and increments it to determine the new record's ID.
        last_id = db.get_last_row(self.table_name, "id") + 1
        # Gets the current date and time and formats it into a specific string.
        date_now = datetime.now().strftime("%d-%m-%Y %H:%I:%f:%p")
        # Creates a dictionary of the user operation data to be inserted.
        data_table = {
            "id": last_id,
            "emp_id": emp_id,
            "operation_type": oper_type,
            "details": details,
            "date": date_now,
        }
        # Calls the database's insert method and returns its result.
        return db.insert(self.table_name, data_table)

    def get(self, emp_id: int):
        """
        Retrieves a user's operation records from the database based on an employee ID.

        Args:
            emp_id (int): The employee's ID to search for.

        Returns:
            dict or None: A dictionary containing the user's operation data if found,
                          or None if no data is found.
        """
        # Initializes the return variable to None.
        data_user = None
        # Calls the database's get method to fetch all records for the specified employee.
        results = db.get(self.table_name, f"emp_id = {emp_id}", False, True, *self.rows)
        # Checks if the database query returned any results.
        if results is not None:
            # Creates a dictionary from the fetched tuple for easier data access.
            data_user = {
                "id": results[0][0],
                "emp_id": results[0][1],
                "operation_type": results[0][2],
                "details": results[0][3],
                "date": results[0][4],
            }
        # Returns the final dictionary of user data or None.
        return data_user
