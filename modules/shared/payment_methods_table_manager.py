import os
import sys
import time

root_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(root_path)

from core.log_utils import log_and_execute_time_with, log_and_execute_time_without
from modules.database_manager import db
from config.data import payment_methods


class PaymentMethodsTableManager:
    def __init__(self):
        self.table_name = "payment_methods"
        self.rows = ["id", "method_name"]
        if db.get_last_row(self.table_name, "id") == 0:
            for item in payment_methods:
                last_id = db.get_last_row(self.table_name, "id") + 1
                data_table = {"id": last_id, "method_name": item}
                db.insert(self.table_name, data_table)

    def get(self, payment_id: int = 0, all_table: bool = False):
        results = None
        if all_table:
            results = db.get(self.table_name, "", True, *self.rows)
        else:
            results = db.get(self.table_name, f"id = {payment_id}", False, *self.rows)
        return results
