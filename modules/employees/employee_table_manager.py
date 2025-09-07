import os
import sys

root_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(root_path)
from base_tamplates import BaseTemplates
from core.log_utils import log_and_execute_time_with


class EmployeeTableManager(BaseTemplates):
    def __init__(self):
        super().__init__("employees")

    @log_and_execute_time_with
    def create(self, emp_id, data):
        return super().create(emp_id, data)

    @log_and_execute_time_with
    def update(self, emp_id, data):
        return super().update(emp_id, data)

    @log_and_execute_time_with
    def delete(self, emp_id):
        return super().delete(emp_id)

    @log_and_execute_time_with
    def get(self, emp_id, *rows):
        results = super().get(emp_id, *rows)
        data_employee = None
        if results is not None:
            data_employee = {
                "id": results[0][0],
                "full_name": results[0][1],
                "national_id": results[0][2],
                "birthday": results[0][3],
                "gender": results[0][4],
                "id_photo": results[0][5],
                "photo": results[0][6],
            }
        return data_employee
