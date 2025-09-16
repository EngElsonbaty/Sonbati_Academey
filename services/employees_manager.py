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
from modules.database_manager import db
from core.log_utils import log_and_execute_time_with


class EmployeesManager:
    def __init__(self):
        self.e1 = EmployeeTableManager()  # data1
        self.e2 = EmployeeDetailsTableManager()  # data2
        self.e3 = EmployeeRolesTableManager()  # data3
        self.e4 = PermissionsTableManager()  # data4
        self.e5 = UserTableManager()  # data3
        self.e6 = AttendanceEmployeeTableManager()  # data 6
        self.e7 = EvaluationEmployeeTableManager()  # data 7
        self.date_now = datetime.now().date().strftime("%d-%m-%Y")
        self.time_now = datetime.now().time().strftime("%I:%M:%S.%f %p")

    @log_and_execute_time_with
    def create(
        self,
        role_name: str,
        role_id: int,
        employee_base_info: dict,
        employee_details: dict,
        user_info: dict = {},
    ):
        status = []
        last_id = db.get_last_row("employees", "id") + 1
        status.append(self.e1.create(last_id, employee_base_info))
        status.append(self.e2.create(last_id, employee_details))
        data_role = {"role_id": role_id, "create_at": self.date_now}
        status.append(self.e3.create(data_role, last_id))
        if role_name == "admin":
            permissions = {
                "addition": True,  # Permission to add data.
                "edition": True,  # Permission to edit data.
                "deletion": True,  # Permission to delete data.
                "view": True,  # Permission to view data.
                "print": True,  # Permission to print data.
                "customize": True,  # Permission to customize settings.
            }
            status.append(self.e4.create(permissions, role_id))
            status.append(self.e5.create(user_info, last_id))
        elif role_name == "teacher":
            print("teacher")
        elif role_name == "data_entry":
            permissions = {
                "addition": True,  # Permission to add data.
                "edition": False,  # Permission to edit data.
                "deletion": False,  # Permission to delete data.
                "view": True,  # Permission to view data.
                "print": False,  # Permission to print data.
                "customize": True,  # Permission to customize settings.
            }
            status.append(self.e4.create(permissions, role_id))
            self.e5.create(user_info, last_id)
        else:
            status = [False]
        return all(status)

    @log_and_execute_time_with
    def update(self, id: int, data: dict):
        pass

    @log_and_execute_time_with
    def delete(self, id: int):
        pass

    @log_and_execute_time_with
    def get(self, id: int):
        pass


e = EmployeesManager()

employees = {
    "full_name": "Mahmoud Elsonbaty",  # The full name of the employee.
    "national_id": "65464894354655465465",  # The national ID of the employee, must be unique.
    "birthday": "21-06-1999",  # The employee's date of birth.
    "gender": "male",  # The gender, must be 'male' or 'female'.
    "id_photo": "TEXT",  # Path to the employee's ID photo.
    "photo": "TEXT",  # Path to the employee's personal photo.
}

employee_details = {
    "address": "Egypt, Cairo",  # The employee's residential address.
    "nationality_id": 1,  # The ID of the employee's nationality.
    "governorate_id": 1,  # The ID of the employee's governorate.
    "email": "mahmoudelsonbaty4553@gmail.com",  # The employee's email address, must be unique.
    "phone_number": "0106448051458",  # The employee's phone number, must be unique.
    "qualification": "TEXT",  # The employee's academic qualification.
    "documents": "TEXT",  # Path to additional documents.
    "salary": 5000,  # The employee's salary.
}

users = {
    "username": "elsonbaty5",  # The unique username for login.
    "password": "1234565",  # The unique password (should be a hashed value).
}

print(e.create("admin", 1, employees, employee_details, users))
