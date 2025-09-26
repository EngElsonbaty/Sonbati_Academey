import os, sys
from datetime import datetime

path_root = os.path.dirname(os.path.dirname(__file__))

sys.path.append(path_root)

from modules.employees.employee_table_manager import EmployeeTableManager
from modules.employees.employee_details_table_manager import EmployeeDetailsTableManager
from modules.employees.employee_roles_table_manager import EmployeeRolesTableManager
from modules.employees.permissions_table_manager import PermissionsTableManager
from modules.employees.users_table_manager import UserTableManager
from modules.employees.attendance_employee_table_manager import (
    AttendanceEmployeeTableManager,
)
from modules.employees.evaluation_employee_table_manager import (
    EvaluationEmployeeTableManager,
)
from modules.employees.teacher_courses_table_manager import TeacherCoursesTableManager
from modules.database_manager import db
from core.log_utils import log_and_execute_time_with
from modules.financial.payment_preferences_table_manager import (
    PaymentPreferencesTableManager,
)
from modules.financial.e_wallets_table_manager import EWalletsTableManager
from modules.financial.bank_accounts_table_manager import BankAccountsTableManager
from modules.financial.bank_checks_table_manager import BankChecksTableManager
from modules.financial.salaries_table_manager import SalariesTableManager
from modules.shared.countries_table_manager import CountriesTableManager
from modules.shared.governorates_table_manager import GovernoratesTableManager
from modules.shared.roles_table_manager import RolesTableManager


class EmployeesManager:
    def __init__(self):
        self.employee_info_master = EmployeeTableManager()
        self.employee_details = EmployeeDetailsTableManager()
        self.employee_roles = EmployeeRolesTableManager()
        self.employee_permissions = PermissionsTableManager()
        self.employee_user = UserTableManager()
        self.employee_course = TeacherCoursesTableManager()
        self.employee_payment = PaymentPreferencesTableManager()
        self.employee_e_wallets = EWalletsTableManager()
        self.employee_account_bank = BankAccountsTableManager()
        self.employee_check_bank = BankChecksTableManager()
        self.employee_salary = SalariesTableManager()
        self.employee_evaluation = EvaluationEmployeeTableManager()
        self.employee_attendance = AttendanceEmployeeTableManager()
        self.date_now = datetime.now().date().strftime("%d-%m-%Y")
        self.time_now = datetime.now().time().strftime("%I:%M:%S.%f %p")
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
        role_name: str,
        role_id: int,
        payment_type: str,
        employee_inf: dict,
        employee_details: dict,
        payment_preferences: dict,
        employee_wallets: dict = {},
        employee_bank_accounts: dict = {},
        employee_user: dict = {},
        employee_course: dict = {},
    ):
        status = []
        last_id = db.get_last_row("employees", "id") + 1
        status.append(self.employee_info_master.create(last_id, employee_inf))
        status.append(self.employee_details.create(last_id, employee_details))
        employee_role = {
            "emp_id": last_id,
            "role_id": role_id,
            "create_at": self.date_now,
        }
        status.append(self.employee_roles.create(employee_role, last_id))
        if (
            role_name == "Administrator"
            or role_name == "Manager"
            or role_name == "Supervisor"
        ):
            if employee_user != {}:
                permission = {
                    "role_id": role_id,  # The ID of the role, must be unique to assign one permission set per role.
                    "addition": True,  # Permission to add data.
                    "edition": True,  # Permission to edit data.
                    "deletion": True,  # Permission to delete data.
                    "view": True,  # Permission to view data.
                    "print": True,  # Permission to print data.
                    "customize": True,  # Permission to customize settings.
                }
                status.append(self.employee_permissions.create(permission, role_id))
                status.append(self.employee_user.create(employee_user, last_id))
        elif role_name == "Data Entry":
            permission = {
                "role_id": role_id,  # The ID of the role, must be unique to assign one permission set per role.
                "addition": True,  # Permission to add data.
                "edition": False,  # Permission to edit data.
                "deletion": False,  # Permission to delete data.
                "view": False,  # Permission to view data.
                "print": True,  # Permission to print data.
                "customize": True,  # Permission to customize settings.
            }
            status.append(self.employee_permissions.create(permission, role_id))
            status.append(self.employee_user.create(employee_user, last_id))
        elif role_name == "Teacher":
            status.append(self.employee_course.create(last_id, employee_course))
        payment_preferences["source_id"] = last_id
        payment_preferences["source_type"] = "employee"
        status.append(self.employee_payment.create(last_id, payment_preferences))
        if payment_type in self.bank_account:
            if employee_bank_accounts != {}:
                status.append(self.employee_account_bank.create(employee_bank_accounts))
        elif payment_type in self.e_wallets:
            if employee_wallets != {}:
                status.append(self.employee_e_wallets.create(employee_wallets))
        return all(status)

    @log_and_execute_time_with
    def update(
        self,
        emp_id: int,
        data: dict = {},
        e_wallets: dict = {},
        account_bank: dict = {},
        is_info_master: bool = False,
        is_details: bool = False,
        is_role: bool = False,
        is_payment: bool = False,
        is_info_payment: bool = False,
        is_permission: bool = False,
        is_users: bool = False,
        is_teacher: bool = False,
    ):
        status = []
        if is_info_master:
            if data != {}:
                status.append(self.employee_info_master.update(emp_id, data))
        if is_details:
            if data != {}:
                status.append(self.employee_details.update(emp_id, data))
        if is_role:
            if data != {}:
                status.append(self.employee_roles.update(emp_id, data))
        if is_payment:
            if data != {}:
                status.append(self.employee_payment.update(emp_id, data))
        if is_info_payment:
            if e_wallets != {}:
                status.append(self.employee_e_wallets.update(emp_id, e_wallets))
            elif account_bank != {}:
                status.append(self.employee_account_bank.update(emp_id, account_bank))
            else:
                status.append(False)
        if is_permission:
            if data != {}:
                status.append(self.employee_permissions.update(emp_id, data))
        if is_users:
            if data != {}:
                status.append(self.employee_user.update(emp_id, data))
        if is_teacher:
            if data != {}:
                status.append(self.employee_course.update(emp_id, data))

        else:
            return status.append(False)
        return all(status)

    @log_and_execute_time_with
    def delete(self, emp_id: int, is_teacher: bool = False, is_manager: bool = False):
        status = []
        if is_teacher and is_manager:
            status.append(self.employee_info_master.delete(emp_id))
            status.append(self.employee_details.delete(emp_id))
            status.append(self.employee_roles.delete(emp_id))
            status.append(self.employee_permissions.delete(emp_id))
            status.append(self.employee_user.delete(emp_id))
            status.append(self.employee_course.delete(emp_id))
            status.append(self.employee_payment.delete(emp_id))
            status.append(self.employee_e_wallets.delete(emp_id))
            status.append(self.employee_account_bank.delete(emp_id))
            status.append(self.employee_check_bank.delete(emp_id))
            status.append(self.employee_salary.delete(emp_id))
            status.append(self.employee_evaluation.delete(emp_id))
            status.append(self.employee_attendance.delete(emp_id))
        elif is_teacher:
            status.append(self.employee_info_master.delete(emp_id))
            status.append(self.employee_details.delete(emp_id))
            status.append(self.employee_course.delete(emp_id))
            status.append(self.employee_payment.delete(emp_id))
            status.append(self.employee_e_wallets.delete(emp_id))
            status.append(self.employee_account_bank.delete(emp_id))
            status.append(self.employee_check_bank.delete(emp_id))
            status.append(self.employee_salary.delete(emp_id))
            status.append(self.employee_evaluation.delete(emp_id))
            status.append(self.employee_attendance.delete(emp_id))
        elif is_manager:
            status.append(self.employee_info_master.delete(emp_id))
            status.append(self.employee_details.delete(emp_id))
            status.append(self.employee_roles.delete(emp_id))
            status.append(self.employee_permissions.delete(emp_id))
            status.append(self.employee_user.delete(emp_id))
            status.append(self.employee_payment.delete(emp_id))
            status.append(self.employee_e_wallets.delete(emp_id))
            status.append(self.employee_account_bank.delete(emp_id))
            status.append(self.employee_check_bank.delete(emp_id))
            status.append(self.employee_salary.delete(emp_id))
            status.append(self.employee_evaluation.delete(emp_id))
            status.append(self.employee_attendance.delete(emp_id))
        else:
            status.append(False)
        return all(status)

    @log_and_execute_time_with
    def get(self, emp_id: int = 0, all_employee: bool = False):
        results = None
        employee = []
        country = CountriesTableManager()
        if all_employee:
            employee = self.employee_info_master.get(0, True)
            if employee:
                for i in employee:
                    employee_info = {
                        "id": i[0],
                        "full_name": i[1],
                        "gender": i[4],
                        "photo": i[6],
                    }
                    employee.append(employee_info)
                employee = None
                for i in employee:
                    employee = self.employee_details.get(i["id"])
                    i["nationality"] = employee["nationality_id"]
                    i["governorate"] = employee["governorate_id"]
                    employee = self.employee_roles.get(i["id"])
                    i["role"] = employee["role_id"]
                    employee = self.employee_evaluation.get(i["id"])
                    i["rating"] = employee["rating"] if employee else None
                    employee = self.employee_payment.get(i["id"])
                    i["payment_method"] = employee["payment_method_id"]
                    i["governorate"] = GovernoratesTableManager().get(i["governorate"])[
                        "governorate_name"
                    ]
                    i["nationality"] = country.get(i["nationality"])["country_name"]
                    i["role"] = RolesTableManager().get(i["role"])[0][1]
                return employee
            else:
                return None

        else:
            employee = self.employee_info_master.get(emp_id, False)
            if employee:
                results = self.employee_details.get(employee["id"])
                employee.update(results)
                results = self.employee_roles.get(employee["id"])
                employee.update(results)
                results = self.employee_payment.get(employee["id"])["payment_method_id"]
                employee.update({"payment_method_id": results})
                results = self.employee_e_wallets.get(employee["id"])
                if results:
                    results.pop("id")
                    results.pop("payment_methods")
                    results.pop("source_id")
                    results.pop("source_type")
                    results.pop("date")
                    employee.update(results)
                results = self.employee_account_bank.get(employee["id"])
                if results:
                    employee.update(results)
                results = self.employee_check_bank.get(employee["id"])
                if results:
                    employee.update(results)
                results = self.employee_permissions.get(employee["id"])
                if results:
                    employee.update(results)
                results = self.employee_user.get(employee["id"])
                if results:
                    employee.update(results)
                results = self.employee_course.get(employee["id"], True)
                if results:
                    employee.update(results)
                results = self.employee_salary.get(employee["id"], True)
                if results:
                    employee.update({"salaries": results})
                results = self.employee_evaluation.get(employee["id"], True)
                if results:
                    employee.update({"evaluation": results})
                results = self.employee_attendance.get(employee["id"], True)
                if results:
                    employee.update({"attendance": results})
                return employee
            else:
                return None

    @log_and_execute_time_with
    def attendance_employee(self, emp_id: int, data: dict):
        return self.employee_attendance.create(emp_id, data)

    @log_and_execute_time_with
    def evaluation_employee(self, emp_id: int, data: dict):
        return self.employee_evaluation.create(emp_id, data)

    @log_and_execute_time_with
    def salary_employee(self, emp_id: int, data: dict):
        return self.employee_salary.create(emp_id, data)
