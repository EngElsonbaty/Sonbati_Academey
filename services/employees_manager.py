from datetime import datetime
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
        status.append(self.employee_payment.create(last_id, payment_preferences))
        if payment_type in self.bank_account:
            if employee_bank_accounts != {}:
                status.append(self.employee_account_bank.create(employee_bank_accounts))
        elif payment_type in self.e_wallets:
            if employee_wallets != {}:
                status.append(self.employee_e_wallets.create(employee_wallets))
        return all(status)
