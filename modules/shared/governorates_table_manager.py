import os
import sys

root_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(root_path)

from core.log_utils import log_and_execute_time_with, log_and_execute_time_without
from modules.database_manager import db
from config.data import countries


class GovernoratesTableManager:

    def __init__(self, country_id: int = 0, governorates: list = []):
        self.table_name = "governorates"
        self.rows = ["id", "country_id", "governorate_name"]
        for item in governorates:
            last_id = db.get_last_row(self.table_name) + 1
            data_table = {
                "id": last_id,
                "country_id": country_id,
                "governorate_name": item,
            }
            db.insert(self.table_name, data_table)

    # Note: Test
    def get(self, gov_id: int = 0, all_table: bool = False):
        results = None
        if all_table:
            results = db.get(self.table_name, "", True, *self.rows)
        else:
            results = db.get(self.table_name, f"id = {gov_id}", False, *self.rows)
        return results
