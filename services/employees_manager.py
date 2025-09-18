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


class EmployeesManager:
    def __init__(self):
        self.employee_info_master = EmployeeTableManager()  # data1
        self.employee_details = EmployeeDetailsTableManager()  # data2
        self.employee_roles = EmployeeRolesTableManager()  # data3
        self.employee_permissions = PermissionsTableManager()  # data4
        self.employee_user = UserTableManager()  # data3
        self.employee_attendance = AttendanceEmployeeTableManager()  # data 6
        self.employee_evaluation = EvaluationEmployeeTableManager()  # data 7
        self.employee_course = TeacherCoursesTableManager()
        self.date_now = datetime.now().date().strftime("%d-%m-%Y")
        self.time_now = datetime.now().time().strftime("%I:%M:%S.%f %p")

    @log_and_execute_time_with
    def create(
        self,
        role_name: str,
        role_id: int,
        employee_base_info: dict,
        employee_details: dict,
        user_info:dict,
        course_info:dict,
    ):
        status = []
        last_id = db.get_last_row("employees", "id") + 1
        status.append(self.employee_info_master.create(last_id, employee_base_info))
        status.append(self.employee_details.create(last_id, employee_details))
        data_role = {"role_id": role_id, "create_at": self.date_now}
        status.append(self.employee_roles.create(data_role, last_id))
        if (
            role_name == "Administrator"
            or role_name == "Manager"
            or role_name == "Supervisor"
        ):
            if user_info != {}:
                permissions = {
                    "addition": True,  # Permission to add data.
                    "edition": True,  # Permission to edit data.
                    "deletion": True,  # Permission to delete data.
                    "view": True,  # Permission to view data.
                    "print": True,  # Permission to print data.
                    "customize": True,  # Permission to customize settings.
                }
                status.append(self.employee_permissions.create(permissions, role_id))
                status.append(self.employee_user.create(user_info, last_id))
        elif role_name == "Teacher":
            if course_info != {}:
                last_id = db.get_last_row("teacher_courses", "id") + 1
                status.append(self.employee_course.create(last_id, course_info))
        elif role_name == "Data Entry":
            if user_info != {}:
                permissions = {
                    "addition": True,  # Permission to add data.
                    "edition": False,  # Permission to edit data.
                    "deletion": False,  # Permission to delete data.
                    "view": True,  # Permission to view data.
                    "print": False,  # Permission to print data.
                    "customize": True,  # Permission to customize settings.
                }
                status.append(self.employee_permissions.create(permissions, role_id))
                status.append(self.employee_user.create(user_info, last_id))
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
