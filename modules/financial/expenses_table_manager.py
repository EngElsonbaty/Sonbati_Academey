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


# Import the custom decorator 'log_and_execute_time_with' from the logging utilities module.
# Imports a custom decorator used for logging function execution time.
from core.log_utils import log_and_execute_time_with

# Imports the database connection object.
from modules.database_manager import db




class ExpensesTableManager:
    def __init__(self) -> None:
        self.table_name = "expenses"
        self.rows = [
            "id",
            "expense_type",
            "amount",
            "receiver",
            "emp_id",
            "expense_date",
            "payment_method_id",
            "notes",
        ]

    @log_and_execute_time_with
    def create(self, id: int, data: dict):
        data_table = {"id ": id}
        data_table.update(data)
        return db.insert(self.table_name, data_table)

    @log_and_execute_time_with
    def update(self, id: int, data: dict):
        return db.update(self.table_name, f"id = {id}", data)

    @log_and_execute_time_with
    def delete(self, id: int):
        return db.delete(self.table_name, f"id = {id}")

    @log_and_execute_time_with
    def get(self, id: int, is_employee: bool = False, all_table: bool = False):
        if is_employee:
            return db.get(self.table_name, f"emp_id = {id}", False, True, *self.rows)
        elif all_table:
            return db.get(self.table_name, "", True, False, *self.rows)
        else:
            results = db.get(self.table_name, f"id = {id}", False, False, *self.rows)
            if results:
                data_table = {
                    "id": results[0][0],
                    "expense_type": results[0][1],
                    "amount": results[0][2],
                    "receiver": results[0][3],
                    "emp_id": results[0][4],
                    "expense_date": results[0][5],
                    "payment_method_id": results[0][6],
                    "notes": results[0][7],
                }
                return data_table
            else:
                return None
