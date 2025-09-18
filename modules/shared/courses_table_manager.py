# The 'os' module provides functions for interacting with the operating system.
import os

# The 'sys' module provides access to system-specific parameters and functions.
import sys

from datetime import datetime

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
from modules.database_manager import db

# Import the custom decorator 'log_and_execute_time_with' from the logging utilities module.
from core.log_utils import log_and_execute_time_with


class CoursesTableManager(BaseTemplates):
    def __init__(self):
        super().__init__("courses")
        self.rows = ["id", "course_name", "course_code", "create_at"]

    @log_and_execute_time_with
    def create(self, id, data):
        data_table = data
        date_now = datetime.now().strftime("%d-%m-%Y,%I:%M:%S.%f %p")
        data_table.update({"create_at": date_now})
        return super().create(id, data, False, 0, False, 0)

    @log_and_execute_time_with
    def update(self, emp_id, data):
        return super().update(emp_id, data, False, False)

    @log_and_execute_time_with
    def delete(self, emp_id):
        return super().delete(emp_id, False, False)

    @log_and_execute_time_with
    def get(self, emp_id, all_table: bool = False):
        if all_table:
            results = db.get(self.table_name, "", True, False, *self.rows)
            return results
        else:
            results = super().get(emp_id, False, False, *self.rows)
            if results:
                data_table = {
                    "id": results[0][0],
                    "course_name": results[0][1],
                    "course_code": results[0][2],
                    "create_at": results[0][3],
                }
                return data_table
            else:
                return None


# c = CoursesTableManager()


# all_courses = [
#     {
#         "course_name": "Anatomy - علم التشريح",
#         "course_code": "MED-101",
#         "create_at": "2025-01-15 10:00:00",
#     },
#     {
#         "course_name": "Physiology - علم وظائف الأعضاء",
#         "course_code": "MED-102",
#         "create_at": "2025-01-15 10:05:00",
#     },
#     {
#         "course_name": "Biochemistry - الكيمياء الحيوية",
#         "course_code": "MED-103",
#         "create_at": "2025-01-15 10:10:00",
#     },
#     {
#         "course_name": "Pharmacology - علم الأدوية",
#         "course_code": "MED-104",
#         "create_at": "2025-01-15 10:15:00",
#     },
#     {
#         "course_name": "Pathology - علم الأمراض",
#         "course_code": "MED-105",
#         "create_at": "2025-01-15 10:20:00",
#     },
#     {
#         "course_name": "Medical Ethics - الأخلاقيات الطبية",
#         "course_code": "MED-106",
#         "create_at": "2025-01-15 10:25:00",
#     },
#     {
#         "course_name": "Pharmaceutical Chemistry - الكيمياء الصيدلانية",
#         "course_code": "PHM-201",
#         "create_at": "2025-01-15 10:30:00",
#     },
#     {
#         "course_name": "Pharmaceutics - الصيدلانيات",
#         "course_code": "PHM-202",
#         "create_at": "2025-01-15 10:35:00",
#     },
#     {
#         "course_name": "Clinical Pharmacy - الصيدلة السريرية",
#         "course_code": "PHM-203",
#         "create_at": "2025-01-15 10:40:00",
#     },
#     {
#         "course_name": "Pharmacognosy - علم العقاقير",
#         "course_code": "PHM-204",
#         "create_at": "2025-01-15 10:45:00",
#     },
#     {
#         "course_name": "Drug Discovery - اكتشاف الدواء",
#         "course_code": "PHM-205",
#         "create_at": "2025-01-15 10:50:00",
#     },
# ]

# for i in range(1, len(all_courses) + 1):
#     print(c.create(i, all_courses[i - 1]))
