import os
import sys

path_modules = os.path.dirname(os.path.dirname(__file__))
root_path = os.path.dirname(path_modules)
sys.path.append(path_modules)
sys.path.append(root_path)

from core.log_utils import log_and_execute_time_with

from modules.database_manager import db


class BaseTemplates:
    def __init__(self, table_name: str) -> None:
        self.table_name = table_name

    @log_and_execute_time_with
    def create(self, emp_id: int, data: dict):
        employee_data = {}
        

    @log_and_execute_time_with
    def update(self, emp_id: int, data: dict):
        pass

    @log_and_execute_time_with
    def delete(self, emp_id: int):
        pass

    @log_and_execute_time_with
    def get(self, emp_id: int):
        pass
