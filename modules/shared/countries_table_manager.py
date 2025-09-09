"""
This file contains the CountriesTableManager class, which manages the population
and retrieval of countries data in the database.

It handles inserting countries and their associated governorates from a data source
and provides a method to retrieve this information.
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
from governorates_table_manager import GovernoratesTableManager

# Import the custom decorator 'log_and_execute_time_with' from the logging utilities module.
# Imports a custom decorator used for logging function execution time.
from core.log_utils import log_and_execute_time_with, log_and_execute_time_without

# Imports the database connection object.
from modules.database_manager import db

# Imports the list of countries and governorates from the configuration file.
from config.data import countries


class CountriesTableManager:
    """
    Manages all database operations for the 'countries' table.

    This class is responsible for populating the countries table and providing
    methods to query its data.
    """

    # @log_and_execute_time_without
    def __init__(self):
        """
        Initializes the class and populates the 'countries' and 'governorates'
        tables if they are currently empty.

        This constructor checks if the 'countries' table is empty and, if so,
        iterates through a list of countries to insert each one. It also calls
        the GovernoratesTableManager to handle inserting the sub-data for each country.
        """
        # Assigns the name of the database table to a class variable.
        self.table_name = "countries"
        # Defines the list of primary columns for this table.
        self.rows = ["id", "country_name"]
        # Checks if the 'countries' table is empty by getting the last row's ID.
        if db.get_last_row(self.table_name, self.rows[0]) == 0:
            # If the table is empty, it starts a loop to insert data from the 'countries' list.
            for item in countries:
                # Gets the ID of the last row and adds 1 to determine the new record's ID.
                last_id = db.get_last_row(self.table_name, self.rows[0]) + 1
                # Creates a dictionary of the country's data to be inserted.
                data_country = {"id": last_id, "country_name": item[0]}
                # This line is a user-defined print statement that likely intends to print the result of the database insertion.
                db.insert(self.table_name, data_country)
                # Creates a new instance of the governorates manager, passing the new country's ID and its list of governorates.
                GovernoratesTableManager(last_id, item[1])

    # @log_and_execute_time_with
    def get(self, country_id: int = 0, all_countries: bool = False):
        """
        Retrieves country data from the 'countries' table.

        Args:
            country_id (int, optional): The ID of the country to retrieve. Defaults to 0.
            all_countries (bool, optional): A flag to retrieve all countries from the table. Defaults to False.

        Returns:
            any: The query results, which can be a single country's data or a list of all countries.
        """
        # Initializes the results variable to None before the database query.
        results = None
        data_country = None
        # Checks if the 'all_countries' flag is set to True.
        if all_countries:
            # If True, calls the database get method to fetch all records from the table.
            results = db.get(self.table_name, "", True, True, *self.rows)
            return results
        # If 'all_countries' is False, this block handles retrieving a specific country by ID.
        else:
            # Calls the database get method to fetch the record with the matching country ID.
            results = db.get(
                self.table_name, f"id = {country_id}", False, False, *self.rows
            )
        data_country = {"id": results[0][0], "country_name": results[0][1]}
        # Returns the final results of the database query.
        return data_country

