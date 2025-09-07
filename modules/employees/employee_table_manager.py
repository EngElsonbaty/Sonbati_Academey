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


class EmployeeTableManager(BaseTemplates):
    """
    Manages all database operations related to the 'employees' table.

    This class inherits from the generic BaseTemplates to provide specific
    CRUD (Create, Read, Update, Delete) functionality for employee data.
    """

    # The __init__ method is the constructor for the class.
    def __init__(self):
        # Call the constructor of the parent class (BaseTemplates)
        # and pass the specific table name "employees".
        super().__init__("employees")
        self.row = [
            "id",
            "full_name",
            "national_id",
            "birthday",
            "gender",
            "id_photo",
            "photo",
        ]

    # The decorator logs and times the execution of the 'create' method.
    @log_and_execute_time_with
    # The 'create' method inserts a new employee record.
    def create(self, emp_id, data):
        # Call the 'create' method of the parent class (BaseTemplates)
        # to handle the actual database insertion.
        return super().create(emp_id, data)

    # The decorator logs and times the execution of the 'update' method.
    @log_and_execute_time_with
    # The 'update' method modifies an existing employee record.
    def update(self, emp_id, data):
        # Call the 'update' method of the parent class to modify the record.
        return super().update(emp_id, data)

    # The decorator logs and times the execution of the 'delete' method.
    @log_and_execute_time_with
    # The 'delete' method removes an employee record.
    def delete(self, emp_id):
        # Call the 'delete' method of the parent class to remove the record.
        return super().delete(emp_id)

    # The decorator logs and times the execution of the 'get' method.
    @log_and_execute_time_with
    # The 'get' method retrieves an employee record and formats the result.
    def get(self, emp_id):
        # Call the 'get' method of the parent class to fetch the raw data.
        results = super().get(emp_id, *self.row)
        # Initialize a variable to hold the formatted employee data.
        data_employee = None
        # Check if any results were returned from the database.
        if results is not None:
            # If results exist, create a new dictionary to hold the data.
            data_employee = {
                # Map the first column from the result to the 'id' key.
                "id": results[0][0],
                # Map the second column from the result to the 'full_name' key.
                "full_name": results[0][1],
                # Map the third column from the result to the 'national_id' key.
                "national_id": results[0][2],
                # Map the fourth column from the result to the 'birthday' key.
                "birthday": results[0][3],
                # Map the fifth column from the result to the 'gender' key.
                "gender": results[0][4],
                # Map the sixth column from the result to the 'id_photo' key.
                "id_photo": results[0][5],
                # Map the seventh column from the result to the 'photo' key.
                "photo": results[0][6],
            }
        # Return the formatted dictionary if results were found, otherwise return None.
        return data_employee
