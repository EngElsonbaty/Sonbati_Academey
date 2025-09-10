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


class PermissionsTableManager(BaseTemplates):
    def __init__(self):
        self.rows = [
            "id",
            "role_id",
            "addition",
            "edition",
            "deletion",
            "view",
            "print",
            "customize",
        ]
        super().__init__("permissions")

    def create(self, id, data, role_id: int = 0):
        return super().create(id, data, False, 0, True, role_id)

    def update(self, emp_id, data):
        return super().update(emp_id, data, False, True)

    def delete(self, emp_id):
        return super().delete(emp_id, False, True)

    def get(self, emp_id):
        results = super().get(emp_id, False, True, *self.rows)
        data_permissions = None
        if results:
            data_permissions = {
                "id": results[0][0],
                "role_id": results[0][1],
                "addition": results[0][2],
                "edition": results[0][3],
                "deletion": results[0][4],
                "view": results[0][5],
                "print": results[0][6],
                "customize": results[0][7],
            }
        return data_permissions


p = PermissionsTableManager()

data_table = {
    "addition": True,
    "edition": False,
    "deletion": False,
    "view": True,
    "print": True,
    "customize": True,
}

print(p.get(2))
