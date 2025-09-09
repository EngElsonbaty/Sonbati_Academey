"""
This file contains the RolesTableManager class, which manages the population
and retrieval of user roles data in the database.

It handles the insertion of roles from a data source and provides a method
to retrieve this information.
"""

# The 'os' module provides functions for interacting with the operating system.
import os

# The 'sys' module provides access to system-specific parameters and functions.
import sys

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

# Imports the database connection object.
from modules.database_manager import db

# Imports the list of roles from the configuration file.
from config.data import roles


class RolesTableManager:
    """
    Manages all database operations for the 'roles' table.

    This class is responsible for populating the roles table with initial data
    and providing a method to query its data.
    """

    def __init__(self):
        """
        Initializes the class and populates the 'roles' table if it is empty.

        This constructor checks if the table is empty and, if so, iterates through
        a list of roles to insert each one into the database.
        """
        # Assigns the name of the database table to a class variable.
        self.table_name = "roles"
        # Defines the list of primary columns for this table.
        self.rows = ["id", "role_name"]
        # Checks if the 'roles' table is empty by getting the last row's ID.
        if db.get_last_row(self.table_name, "id") == 0:
            # If the table is empty, it starts a loop to insert data from the 'roles' list.
            for item in roles:
                # Gets the ID of the last row and adds 1 to determine the new record's ID.
                last_id = db.get_last_row(self.table_name, "id") + 1
                # Creates a dictionary of the role's data to be inserted.
                data_table = {"id": last_id, "role_name": item}
                # Calls the database's 'insert' method to add the data to the table.
                db.insert(self.table_name, data_table)

    def get(self, role_id: int = 0, all_table: bool = False):
        """
        Retrieves role data from the 'roles' table.

        Args:
            role_id (int, optional): The ID of the role to retrieve. Defaults to 0.
            all_table (bool, optional): A flag to retrieve all roles. Defaults to False.

        Returns:
            any: The query results, which can be a single role's data or a list of all roles.
        """
        # Initializes the results variable to None before the database query.
        results = None
        # Checks if the 'all_table' flag is set to True.
        if all_table:
            # If True, calls the database's get method to fetch all records from the table.
            results = db.get(self.table_name, "", True, True, *self.rows)
        # If 'all_table' is False, this block handles retrieving a specific role by ID.
        else:
            # Calls the database's get method to fetch the record with the matching ID.
            results = db.get(
                self.table_name, f"id = {role_id}", False, False, *self.rows
            )
        # Returns the final results of the database query.
        return results

