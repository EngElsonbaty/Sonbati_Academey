import os
import sys
import time
from governorates_table_manager import GovernoratesTableManager

root_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(root_path)

from core.log_utils import log_and_execute_time_with, log_and_execute_time_without
from modules.database_manager import db
from config.data import countries


class CountriesTableManager:

    # @log_and_execute_time_without
    def __init__(self):
        start_time = time.perf_counter_ns()
        self.table_name = "countries"
        self.rows = ["id", "country_name"]
        if db.get_last_row(self.table_name, self.rows[0]) == 0:
            for item in countries:
                last_id = db.get_last_row(self.table_name, self.rows[0]) + 1
                data_country = {"id": last_id, "country_name": item[0]}
                print(f"Countries:{db.insert(self.table_name, data_country)}")
                g = GovernoratesTableManager(last_id, item[1])
        end_time = time.perf_counter_ns()
        execute_time = float((end_time - start_time) / 1_000_000)
        print(execute_time)

    # @log_and_execute_time_with
    def get(self, country_id: int = 0, all_countries: bool = False):
        results = None
        if all_countries:
            results = db.get(self.table_name, "", True, *self.rows)
        else:
            results = db.get(self.table_name, f"id = {country_id}", False, *self.rows)
        return results


c = CountriesTableManager()
