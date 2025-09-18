"""
This file contains the GovernoratesTableManager class, which manages the population
and retrieval of governorates data in the database.

It handles the insertion of governorates associated with a specific country and
provides a method to retrieve this information.
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

# Imports the list of countries and governorates from the configuration file.
from config.data import countries


class GovernoratesTableManager:
    """
    Manages all database operations for the 'governorates' table.

    This class is responsible for populating the governorates table and providing
    a method to query its data. It is typically used in conjunction with a
    countries manager class.
    """

    def __init__(self, country_id: int = 0, governorates: list = []):
        """
        Initializes the class and populates the 'governorates' table with data
        for a specific country.

        Args:
            country_id (int, optional): The ID of the country the governorates belong to. Defaults to 0.
            governorates (list, optional): A list of governorate names to insert. Defaults to [].
        """
        # Assigns the name of the database table to a class variable.
        self.table_name = "governorates"
        # Defines the list of primary columns for this table.
        self.rows = ["id", "country_id", "governorate_name"]
        # Loops through each governorate name in the provided list.
        if country_id != 0 and governorates != []:
            for item in governorates:
                # Gets the ID of the last row and adds 1 to determine the new record's ID.
                last_id = db.get_last_row(self.table_name) + 1
                # Creates a dictionary of the governorate's data to be inserted.
                data_table = {
                    # Sets the new record's ID.
                    "id": last_id,
                    # Associates the governorate with its parent country.
                    "country_id": country_id,
                    # Sets the name of the governorate.
                    "governorate_name": item,
                }
                # Calls the database's 'insert' method to add the data to the table.
                db.insert(self.table_name, data_table)

    @log_and_execute_time_with
    def get(
        self,
        gov_id: int = 0,
        country: bool = False,
        country_id: int = 0,
        all_table: bool = False,
    ):
        """
        Retrieves governorate data from the 'governorates' table.

        Args:
            gov_id (int, optional): The ID of the governorate to retrieve. Defaults to 0.
            all_table (bool, optional): A flag to retrieve all governorates. Defaults to False.

        Returns:
            any: The query results, which can be a single governorate's data or a list of all governorates.
        """
        # Initializes the results variable to None before the database query.
        results = None
        data_governorates = None
        # Checks if the 'all_table' flag is set to True.
        if all_table:
            # If True, calls the database's get method to fetch all records from the table.
            results = db.get(self.table_name, "", True, True, *self.rows)
            return results
        elif country:
            return db.get(
                self.table_name, f"country_id = {country_id}", False, True, *self.rows
            )
        # If 'all_table' is False, this block handles retrieving a specific governorate by ID.
        else:
            # Calls the database's get method to fetch the record with the matching ID.
            results = db.get(
                self.table_name, f"id = {gov_id}", False, False, *self.rows
            )
        data_governorates = {
            "id": results[0][0],
            "country_id": results[0][1],
            "governorate_name": results[0][2],
        }
        # Returns the final results of the database query.
        return data_governorates

