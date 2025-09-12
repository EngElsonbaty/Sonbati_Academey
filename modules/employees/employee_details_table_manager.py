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

# Import the custom decorator 'log_and_execute_time_with' from the logging utilities module.
from core.log_utils import log_and_execute_time_with
from modules.database_manager import db


class EmployeeDetailsTableManager(BaseTemplates):
    """
    Manages all database operations for the 'employee_details' table.

    This class inherits from the generic BaseTemplates to provide specific
    CRUD (Create, Read, Update, Delete) functionality for employee detail data.
    It specializes the parent class to handle the unique structure of this table.
    """

    # The __init__ method is the constructor for the class.
    def __init__(self):
        """
        Initializes the EmployeeDetailsTableManager by calling the parent constructor
        and setting the specific table name.
        """
        # Call the constructor of the parent class (BaseTemplates)
        # and pass the specific table name "employee_details".
        super().__init__("employee_details")
        # Define a list of column names to be used for data retrieval and formatting.
        self.row = [
            "id",
            "emp_id",
            "address",
            "nationality_id",
            "governorate_id",
            "email",
            "phone_number",
            "qualification",
            "documents",
            "salary",
        ]

    # The decorator logs and times the execution of the 'create' method.
    @log_and_execute_time_with
    # The 'create' method inserts a new employee details record.
    def create(self, emp_id: int, data: dict):
        # Call the 'create' method of the parent class (BaseTemplates).
        # It handles the actual database insertion.
        # This call passes the record_id, data dictionary, a boolean 'True', and the emp_id.
        record_id = db.get_last_row(self.table_name, "id") + 1
        return super().create(record_id, data, True, emp_id, False, 0)

    # The decorator logs and times the execution of the 'update' method.
    @log_and_execute_time_with
    # The 'update' method modifies an existing employee details record.
    def update(self, emp_id, data):
        # Call the 'update' method of the parent class to modify the record.
        # It updates the record where the ID matches the provided employee ID.
        return super().update(emp_id, data, True)

    # The decorator logs and times the execution of the 'delete' method.
    @log_and_execute_time_with
    # The 'delete' method removes an employee details record.
    def delete(self, emp_id):
        # Call the 'delete' method of the parent class to remove the record.
        # It deletes the record where the ID matches the provided employee ID.
        return super().delete(emp_id, True)

    # The decorator logs and times the execution of the 'get' method.
    @log_and_execute_time_with
    # The 'get' method retrieves an employee details record and formats the result.
    def get(self, emp_id: int, all_emp: bool = False):
        # Call the 'get' method of the parent class to fetch the raw data.
        # It uses the 'self.row' list to specify the columns to be retrieved.
        results = super().get(emp_id, True, *self.row)
        # Initialize a variable to hold the formatted employee details data.
        data_employee = None
        # Check if any results were returned from the database.
        if results is not None:
            # If results exist, create a new dictionary to hold the formatted data.
            # The keys are taken from the 'self.row' list, and the values are
            # from the corresponding columns of the query result.
            data_employee = {
                "address": results[0][0],
                "nationality_id": results[0][1],
                "governorate_id": results[0][2],
                "email": results[0][3],
                "phone_number": results[0][4],
                "qualification": results[0][5],
                "documents": results[0][6],
                "salary": results[0][7],
            }
        # Return the formatted dictionary if results were found, otherwise return None.
        return data_employee
