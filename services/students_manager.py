import os
import sys
import time

path_root = os.path.dirname(os.path.dirname(__file__))
sys.path.append(path_root)

from modules.students.students_table_manager import StudentsTableManager
from modules.students.student_details_table_manager import StudentDetailsTableManager
from modules.students.attendance_student_table_manager import (
    AttendanceStudentTableManager,
)
from modules.students.evaluation_student_table_manager import (
    EvaluationStudentTableManager,
)
from modules.students.student_courses_table_manager import StudentCoursesTableManager
from modules.students.homework_student_table_manager import HomeworkStudentTableManager
from modules.students.exam_student_table_manager import ExamStudentTableManager
from modules.financial.payment_preferences_table_manager import (
    PaymentPreferencesTableManager,
)
from modules.financial.bank_accounts_table_manager import BankAccountsTableManager
from modules.financial.bank_checks_table_manager import BankChecksTableManager
from modules.financial.e_wallets_table_manager import EWalletsTableManager
from modules.financial.revenues_table_manager import RevenuesTableManager
from core.log_utils import log_and_execute_time_with
from modules.database_manager import db


class StudentsManager:
    def __init__(self) -> None:
        self.student_info_master = StudentsTableManager()
        self.student_details = StudentDetailsTableManager()
        self.student_attendance = AttendanceStudentTableManager()
        self.student_evaluation = EvaluationStudentTableManager()
        self.student_course = StudentCoursesTableManager()
        self.student_homework = HomeworkStudentTableManager()
        self.student_exams = ExamStudentTableManager()
        self.payment_preferences = PaymentPreferencesTableManager()
        self.student_bank_account = BankAccountsTableManager()
        self.student_bank_checks = BankChecksTableManager()
        self.student_e_wallets = EWalletsTableManager()
        self.student_fees = RevenuesTableManager()
        self.e_wallets = [
            # Mobile Wallets & Digital Payment Apps
            "InstaPay",
            "Vodafone Cash",
            "e& money",
            "Orange Money",
            "We Pay",
            "CIB Smart Wallet",
            "QNB Al Ahli E-Wallet",
            "BM Wallet",
            "Easycash",
            "EBank Wallet (Gebe)",
        ]
        self.bank_account = [
            "Bank Transfer",
            "Credit Cards",
            "Debit Cards",
            "Meeza Cards",
            "Point of Sale (POS)",
        ]

    @log_and_execute_time_with
    def create(
        self,
        info_master: dict,
        student_details: dict,
        student_course: dict,
        payment_method: str,
        payment_info: dict,
        e_wallet: dict = {},
        bank_account: dict = {},
    ):
        last_id = db.get_last_row("students", "id") + 1
        status = []
        status.append(self.student_info_master.create(last_id, info_master))
        status.append(self.student_details.create(last_id, student_details))
        status.append(self.student_course.create(last_id, student_course))
        status.append(self.payment_preferences.create(last_id, payment_info))
        if payment_method in self.e_wallets:
            if e_wallet != {}:
                e_wallet["source_id"] = last_id
                e_wallet["source_type"] = "student"
                status.append(self.student_e_wallets.create(e_wallet))
        elif payment_method in self.bank_account:
            if bank_account != {}:
                bank_account["source_id"] = last_id
                bank_account["source_type"] = "student"
                status.append(self.student_bank_account.create(bank_account))

        return all(status)

    @log_and_execute_time_with
    def update(
        self,
        student_id: int,
        info_master: dict = {},
        student_details: dict = {},
        student_course: dict = {},
        payment_method: dict = {},
        e_wallets: dict = {},
        bank_account: dict = {},
        is_info_master: bool = False,
        is_student_details: bool = False,
        is_student_course: bool = False,
        is_payment_method: bool = False,
        is_e_wallets: bool = False,
        is_bank_account: bool = False,
    ):
        status = []
        if is_info_master:
            status.append(self.student_info_master.update(student_id, info_master))
        if is_student_details:
            status.append(self.student_details.update(student_id, student_details))
        if is_student_course:
            status.append(self.student_course.update(student_id, student_course))
        if is_payment_method:
            status.append(self.payment_preferences.update(student_id, payment_method))
        if is_e_wallets:
            status.append(self.student_e_wallets.update(student_id, e_wallets))
        if is_bank_account:
            status.append(self.student_bank_account.update(student_id, bank_account))
        return all(status)

    @log_and_execute_time_with
    def delete(self, student_id: int):
        status = []
        status.append(self.student_info_master.delete(student_id))
        status.append(self.student_details.delete(student_id))
        status.append(self.student_attendance.delete(student_id))
        status.append(self.student_evaluation.delete(student_id))
        status.append(self.student_course.delete(student_id))
        status.append(self.student_homework.delete(student_id))
        status.append(self.student_exams.delete(student_id))
        return all(status)

    @log_and_execute_time_with
    def get(self, student_id: int, all_student: bool = False):
        if all_student:
            results = self.student_info_master.get(0, True)
            if results:
                
            return results
        else:
            results = self.student_info_master.get(student_id)
            return results

    @log_and_execute_time_with
    def fees(self, student_id: int, data: dict):
        pass

    @log_and_execute_time_with
    def attendance_student(self, student_id: int, data: dict):
        pass

    @log_and_execute_time_with
    def evaluation_student(self, student_id: int, data: dict):
        pass

    @log_and_execute_time_with
    def homework_student(self, student_id: int, data: dict):
        pass

    @log_and_execute_time_with
    def exam_student(self, student_id: int, data: dict):
        pass

    @log_and_execute_time_with
    def add_course(self, student_id: int, data: dict):
        pass


start_time = time.perf_counter_ns()
s = StudentsManager()

results = s.get(0, True)
for i in results:
    print(i)
end_time = time.perf_counter_ns()
execution_time = (end_time - start_time) / 1_000_000
print(f"The Execution Time: {execution_time:.2f}")
