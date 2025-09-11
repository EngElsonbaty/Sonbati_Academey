"""
This file defines the database schema for the educational management system.
Each dictionary represents a table, with keys as column names and values as
SQL data types and constraints.
"""

countries = {
    # The 'countries' table stores information about different countries.
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",  # Unique identifier for each country.
    "country_name": "TEXT NOT NULL UNIQUE",  # The name of the country, must be unique.
}

governorates = {
    # The 'governorates' table stores information about governorates.
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",  # Unique identifier for each governorate.
    "country_id": "INTEGER NOT NULL",  # The ID of the country to which the governorate belongs.
    "governorate_name": "TEXT NOT NULL",  # The name of the governorate.
    "FOREIGN KEY": "(country_id) REFERENCES countries(id)",  # Defines the foreign key relationship with the 'countries' table.
}

payment_methods = {
    # The 'payment_methods' table stores the different types of payment methods.
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",  # Unique identifier for each payment method.
    "method_name": "TEXT NOT NULL UNIQUE",  # The name of the payment method, such as 'cash' or 'bank transfer'.
}

class_rooms = {
    # The 'class_rooms' table stores information about the classrooms.
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",  # Unique identifier for each classroom.
    "classroom_name": "TEXT NOT NULL UNIQUE",  # The name of the classroom.
    "classroom_code": "TEXT NOT NULL UNIQUE",  # The unique code for the classroom.
    "counter": "INTEGER NOT NULL",
}

courses = {
    # The 'courses' table stores information about the academic courses.
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",  # Unique identifier for each course.
    "course_name": "TEXT NOT NULL UNIQUE",  # The name of the course.
    "course_code": "TEXT NOT NULL UNIQUE",  # The unique code for the course.
}

roles = {
    # The 'roles' table stores the different roles of employees in the system.
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",  # Unique identifier for each role.
    "role_name": "TEXT NOT NULL UNIQUE",  # The name of the role, such as 'teacher' or 'administrator'.
}

employees = {
    # The 'employees' table stores general information about employees.
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",  # Unique identifier for each employee.
    "full_name": "TEXT NOT NULL",  # The full name of the employee.
    "national_id": "TEXT NOT NULL UNIQUE",  # The national ID of the employee, must be unique.
    "birthday": "DATE NOT NULL",  # The employee's date of birth.
    "gender": "TEXT NOT NULL CHECK(gender IN ('male', 'female'))",  # The gender, must be 'male' or 'female'.
    "id_photo": "TEXT NOT NULL",  # Path to the employee's ID photo.
    "photo": "TEXT NOT NULL",  # Path to the employee's personal photo.
}

students = {
    # The 'students' table stores general information about students.
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",  # Unique identifier for each student.
    "full_name": "TEXT NOT NULL",  # The full name of the student.
    "national_id": "TEXT NOT NULL UNIQUE",  # The national ID of the student, must be unique.
    "birthday": "DATE NOT NULL",  # The student's date of birth.
    "gender": "TEXT NOT NULL CHECK(gender IN ('male', 'female'))",  # The gender, must be 'male' or 'female'.
    "id_photo": "TEXT NOT NULL",  # Path to the student's ID photo.
    "photo": "TEXT NOT NULL",  # Path to the student's personal photo.
}

employee_details = {
    # The 'employee_details' table stores additional, detailed information about employees.
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",  # Unique identifier for the detail record.
    "emp_id": "INTEGER NOT NULL UNIQUE",  # The ID of the employee, must be unique for a one-to-one relationship.
    "address": "TEXT NOT NULL",  # The employee's residential address.
    "nationality_id": "INTEGER NOT NULL",  # The ID of the employee's nationality.
    "governorate_id": "INTEGER NOT NULL",  # The ID of the employee's governorate.
    "email": "TEXT NOT NULL UNIQUE",  # The employee's email address, must be unique.
    "phone_number": "TEXT NOT NULL UNIQUE",  # The employee's phone number, must be unique.
    "qualification": "TEXT NOT NULL",  # The employee's academic qualification.
    "documents": "TEXT",  # Path to additional documents.
    "salary": "REAL NOT NULL",  # The employee's salary.
    "FOREIGN KEY": "(emp_id) REFERENCES employees(id)",  # Links to the 'employees' table.
    "FOREIGN KEY": "(nationality_id) REFERENCES countries(id)",  # Links to the 'countries' table.
    "FOREIGN KEY": "(governorate_id) REFERENCES governorates(id)",  # Links to the 'governorates' table.
}

student_details = {
    # The 'student_details' table stores additional, detailed information about students.
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",  # Unique identifier for the detail record.
    "student_id": "INTEGER NOT NULL UNIQUE",  # The ID of the student, must be unique for a one-to-one relationship.
    "address": "TEXT NOT NULL",  # The student's residential address.
    "nationality_id": "INTEGER NOT NULL",  # The ID of the student's nationality.
    "governorate_id": "INTEGER NOT NULL",  # The ID of the student's governorate.
    "email": "TEXT NOT NULL UNIQUE",  # The student's email address, must be unique.
    "phone_number": "TEXT NOT NULL UNIQUE",  # The student's phone number, must be unique.
    "fees": "REAL NOT NULL",  # The student's fees.
    "FOREIGN KEY": "(student_id) REFERENCES students(id)",  # Links to the 'students' table.
    "FOREIGN KEY": "(nationality_id) REFERENCES countries(id)",  # Links to the 'countries' table.
    "FOREIGN KEY": "(governorate_id) REFERENCES governorates(id)",  # Links to the 'governorates' table.
}

employee_roles = {
    # The 'employee_roles' table links employees to their roles.
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",  # Unique identifier for the role assignment.
    "emp_id": "INTEGER NOT NULL UNIQUE",  # The ID of the employee, must be unique to assign one role per employee.
    "role_id": "INTEGER NOT NULL",  # The ID of the assigned role.
    "FOREIGN KEY": "(emp_id) REFERENCES employees(id)",  # Links to the 'employees' table.
    "FOREIGN KEY": "(role_id) REFERENCES roles(id)",  # Links to the 'roles' table.
}

users = {
    # The 'users' table stores login credentials for employees.
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",  # Unique identifier for the user record.
    "emp_id": "INTEGER NOT NULL UNIQUE",  # The ID of the employee, must be unique for a one-to-one relationship.
    "username": "TEXT NOT NULL UNIQUE",  # The unique username for login.
    "password": "TEXT NOT NULL UNIQUE",  # The unique password (should be a hashed value).
    "FOREIGN KEY": "(emp_id) REFERENCES employees(id)",  # Links to the 'employees' table.
}

user_operation = {
    # The 'user_operation' table logs operations performed by employees.
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",  # Unique identifier for each operation log.
    "emp_id": "INTEGER NOT NULL",  # The ID of the employee who performed the operation.
    "operation_type": "TEXT NOT NULL",  # The type of operation performed.
    "details": "TEXT",  # Optional details about the operation.
    "date": "DATETIME NOT NULL",  # The date and time of the operation.
    "FOREIGN KEY": "(emp_id) REFERENCES employees(id)",  # Links to the 'employees' table.
}

permissions = {
    # The 'permissions' table defines access rights for each role.
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",  # Unique identifier for the permission set.
    "role_id": "INTEGER NOT NULL UNIQUE",  # The ID of the role, must be unique to assign one permission set per role.
    "addition": "BOOLEAN NOT NULL DEFAULT 0 CHECK(addition IN (0, 1))",  # Permission to add data.
    "edition": "BOOLEAN NOT NULL DEFAULT 0 CHECK(edition IN (0, 1))",  # Permission to edit data.
    "deletion": "BOOLEAN NOT NULL DEFAULT 0 CHECK(deletion IN (0, 1))",  # Permission to delete data.
    "view": "BOOLEAN NOT NULL DEFAULT 0 CHECK(view IN (0, 1))",  # Permission to view data.
    "print": "BOOLEAN NOT NULL DEFAULT 0 CHECK(print IN (0, 1))",  # Permission to print data.
    "customize": "BOOLEAN NOT NULL DEFAULT 0 CHECK(customize IN (0, 1))",  # Permission to customize settings.
    "FOREIGN KEY": "(role_id) REFERENCES employee_roles(id)",  # Links to the 'employee_roles' table.
}

teacher_courses = {
    # The 'teacher_courses' table links teachers to courses and classrooms.
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",  # Unique identifier for the course assignment.
    "teacher_id": "INTEGER NOT NULL",  # The ID of the teacher.
    "course_id": "INTEGER NOT NULL",  # The ID of the course.
    "class_room_id": "INTEGER NOT NULL",  # The ID of the classroom.
    "day_of_week": "TEXT NOT NULL",  # The day of the week for the class.
    "start_time": "TIME NOT NULL",  # The start time of the class.
    "end_time": "TIME NOT NULL",  # The end time of the class.
    "created_at": "DATE NOT NULL",  # The date the assignment was created.
    "FOREIGN KEY": "(teacher_id) REFERENCES employees(id)",  # Links to the 'employees' table.
    "FOREIGN KEY": "(course_id) REFERENCES courses(id)",  # Links to the 'courses' table.
    "FOREIGN KEY": "(class_room_id) REFERENCES class_rooms(id)",  # Links to the 'class_rooms' table.
}

exams = {
    # The 'exams' table stores information about scheduled exams.
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",  # Unique identifier for the exam.
    "course_id": "INTEGER NOT NULL",  # The ID of the course the exam belongs to.
    "teacher_id": "INTEGER NOT NULL",  # The ID of the teacher who created the exam.
    "class_rooms_id": "INTEGER NOT NULL",  # The ID of the classroom where the exam takes place.
    "finally_grade": "REAL NOT NULL",  # The final grade for the exam.
    "full_time": "TIME NOT NULL",  # The total duration of the exam.
    "start_time": "TIME NOT NULL",  # The start time of the exam.
    "end_time": "TIME NOT NULL",  # The end time of the exam.
    "file_pdf": "TEXT NOT NULL",  # Path to the PDF file of the exam questions.
    "date": "DATE NOT NULL",  # The date of the exam.
    "FOREIGN KEY": "(teacher_id) REFERENCES employees(id)",  # Links to the 'employees' table.
    "FOREIGN KEY": "(course_id) REFERENCES courses(id)",  # Links to the 'courses' table.
    "FOREIGN KEY": "(class_rooms_id) REFERENCES class_rooms(id)",  # Links to the 'class_rooms' table.
}

homework = {
    # The 'homework' table stores information about assignments given.
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",  # Unique identifier for the homework.
    "teacher_id": "INTEGER NOT NULL",  # The ID of the teacher who assigned the homework.
    "course_id": "INTEGER NOT NULL",  # The ID of the course the homework belongs to.
    "class_room_id": "INTEGER NOT NULL",  # The ID of the classroom the homework is for.
    "file_pdf": "TEXT NOT NULL",  # Path to the PDF file of the homework questions.
    "finally_grade": "REAL NOT NULL",  # The final grade for the homework.
    "date": "DATETIME NOT NULL",  # The date the homework was assigned.
    "FOREIGN KEY": "(teacher_id) REFERENCES employees(id)",  # Links to the 'employees' table.
    "FOREIGN KEY": "(course_id) REFERENCES courses(id)",  # Links to the 'courses' table.
    "FOREIGN KEY": "(class_room_id) REFERENCES class_rooms(id)",  # Links to the 'class_rooms' table.
}

attendance_employee = {
    # The 'attendance_employee' table records attendance for employees.
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",  # Unique identifier for each attendance record.
    "emp_id": "INTEGER NOT NULL",  # The ID of the employee.
    "type": "TEXT NOT NULL CHECK (type IN ('in', 'out'))",  # The type of record, either 'in' or 'out'.
    "time": "TIME NOT NULL",  # The time of the attendance record.
    "created_at": "DATE NOT NULL",  # The date of the attendance record.
    "FOREIGN KEY": "(emp_id) REFERENCES employees(id)",  # Links to the 'employees' table.
}

attendance_student = {
    # The 'attendance_student' table records attendance for students.
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",  # Unique identifier for each attendance record.
    "student_id": "INTEGER NOT NULL",  # The ID of the student.
    "type": "TEXT NOT NULL CHECK (type IN ('in', 'out'))",  # The type of record, either 'in' or 'out'.
    "time": "TIME NOT NULL",  # The time of the attendance record.
    "created_at": "DATE NOT NULL",  # The date of the attendance record.
    "FOREIGN KEY": "(student_id) REFERENCES students(id)",  # Links to the 'students' table.
}

evaluation_employee = {
    # The 'evaluation_employee' table stores employee evaluation records.
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",  # Unique identifier for each evaluation record.
    "emp_id": "INTEGER NOT NULL",  # The ID of the employee being evaluated.
    "evaluation_type": "TEXT NOT NULL",  # The type of evaluation (e.g., 'performance').
    "rating": "REAL NOT NULL",  # The numerical rating of the evaluation.
    "created_at": "DATETIME NOT NULL",  # The date and time the evaluation was created.
    "FOREIGN KEY": "(emp_id) REFERENCES employees(id)",  # Links to the 'employees' table.
}

evaluation_student = {
    # The 'evaluation_student' table stores student evaluation records.
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",  # Unique identifier for each evaluation record.
    "student_id": "INTEGER NOT NULL",  # The ID of the student being evaluated.
    "evaluation_type": "TEXT NOT NULL",  # The type of evaluation (e.g., 'behavior').
    "rating": "REAL NOT NULL",  # The numerical rating of the evaluation.
    "created_at": "DATETIME NOT NULL",  # The date and time the evaluation was created.
    "FOREIGN KEY": "(student_id) REFERENCES students(id)",  # Links to the 'students' table.
}

exam_student = {
    # The 'exam_student' table records student grades on exams.
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",  # Unique identifier for each exam grade.
    "exam_id": "INTEGER NOT NULL",  # The ID of the exam.
    "student_id": "INTEGER NOT NULL",  # The ID of the student.
    "student_grade": "REAL NOT NULL",  # The grade the student received.
    "file_pdf": "TEXT NOT NULL",  # Path to the PDF file of the student's answers.
    "date": "DATETIME NOT NULL",  # The date the grade was recorded.
    "FOREIGN KEY": "(student_id) REFERENCES students(id)",  # Links to the 'students' table.
    "FOREIGN KEY": "(exam_id) REFERENCES exams(id)",  # Links to the 'exams' table.
    "UNIQUE": "(exam_id, student_id)",  # Ensures a student can't have multiple grades for the same exam.
}

homework_student = {
    # The 'homework_student' table records student grades on homework.
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",  # Unique identifier for each homework grade.
    "homework_id": "INTEGER NOT NULL",  # The ID of the homework.
    "student_id": "INTEGER NOT NULL",  # The ID of the student.
    "student_grade": "REAL NOT NULL",  # The grade the student received.
    "date": "DATETIME NOT NULL",  # The date the grade was recorded.
    "notes": "TEXT NOT NULL",  # Notes about the student's homework.
    "FOREIGN KEY": "(homework_id) REFERENCES homework(id)",  # Links to the 'homework' table.
    "FOREIGN KEY": "(student_id) REFERENCES students(id)",  # Links to the 'students' table.
}

student_courses = {
    # The 'student_courses' table links students to specific course schedules.
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",  # Unique identifier for the course enrollment.
    "student_id": "INTEGER NOT NULL",  # The ID of the student.
    "teacher_course_id": "INTEGER NOT NULL",  # The ID of the specific course schedule.
    "join_date": "DATE NOT NULL",  # The date the student joined the course.
    "FOREIGN KEY": "(student_id) REFERENCES students(id)",  # Links to the 'students' table.
    "FOREIGN KEY": "(teacher_course_id) REFERENCES teacher_courses(id)",  # Links to the 'teacher_courses' table.
}

expenses = {
    # The 'expenses' table records all expenses.
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",  # Unique identifier for each expense.
    "expense_type": "TEXT NOT NULL",  # The type of expense (e.g., 'salaries', 'rent').
    "amount": "REAL NOT NULL",  # The amount of the expense.
    "receiver": "TEXT NOT NULL",  # The name of the receiver of the funds.
    "emp_id": "INTEGER NOT NULL",  # The ID of the employee who authorized the expense.
    "expense_date": "DATETIME NOT NULL",  # The date and time of the expense.
    "payment_method_id": "INTEGER NOT NULL",  # The ID of the payment method used.
    "notes": "TEXT",  # Optional notes about the expense.
    "FOREIGN KEY": "(emp_id) REFERENCES employees(id)",  # Links to the 'employees' table.
}

revenues = {
    # The 'revenues' table records all income.
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",  # Unique identifier for each revenue record.
    "income_type": "TEXT NOT NULL",  # The type of income (e.g., 'student fees').
    "amount": "REAL NOT NULL",  # The amount of income.
    "source_id": "INTEGER NOT NULL",  # The ID of the source of the income (e.g., a student).
    "emp_id": "INTEGER NOT NULL",  # The ID of the employee who recorded the income.
    "transaction_date": "DATETIME NOT NULL",  # The date and time of the transaction.
    "payment_method_id": "INTEGER NOT NULL",  # The ID of the payment method used.
    "notes": "TEXT",  # Optional notes about the income.
    "FOREIGN KEY": "(source_id) REFERENCES students(id)",  # Links to the 'students' table.
    "FOREIGN KEY": "(emp_id) REFERENCES employees(id)",  # Links to the 'employees' table.
}

payment_preferences = {
    # The 'payment_preferences' table links a person to their preferred payment methods.
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",  # Unique identifier for the preference record.
    "source_id": "INTEGER NOT NULL",  # The ID of the person (employee or student).
    "source_type": "TEXT NOT NULL",  # The type of person ('employee' or 'student').
    "payment_method_id": "INTEGER NOT NULL",  # The ID of the payment method.
    "created_at": "DATETIME NOT NULL",  # The date and time the preference was set.
    "FOREIGN KEY": "(payment_method_id) REFERENCES payment_methods(id)",  # Links to the 'payment_methods' table.
    "UNIQUE": "(source_id, source_type, payment_method_id)",  # Ensures a person has only one record for each payment method.
}

bank_accounts = {
    # The 'bank_accounts' table stores bank account details for individuals.
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",  # Unique identifier for each bank account.
    "payment_methods": "INTEGER NOT NULL",  # The ID linking to the payment preference.
    "source_id": "INTEGER NOT NULL",  # The ID of the account holder.
    "source_type": "TEXT NOT NULL",  # The type of account holder ('employee' or 'student').
    "holder_name": "TEXT NOT NULL",  # The name of the account holder.
    "bank_name": "TEXT NOT NULL",  # The name of the bank.
    "account_number": "TEXT NOT NULL UNIQUE",  # The unique account number.
    "iban": "TEXT NOT NULL UNIQUE",  # The unique IBAN number.
    "date": "DATETIME NOT NULL",  # The date the account was recorded.
    "UNIQUE": "(source_id, source_type, account_number, payment_methods)",  # Ensures uniqueness for this combination.
    "FOREIGN KEY": "(payment_methods) REFERENCES payment_preferences(id)",  # Links to the 'payment_preferences' table.
}

bank_checks = {
    # The 'bank_checks' table records details about bank checks.
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",  # Unique identifier for each check.
    "payment_methods": "INTEGER NOT NULL",  # The ID linking to the payment preference.
    "source_id": "INTEGER NOT NULL",  # The ID of the check source.
    "source_type": "TEXT NOT NULL",  # The type of check source ('employee' or 'student').
    "bank_name": "TEXT NOT NULL",  # The name of the bank the check is from.
    "holder_name": "TEXT NOT NULL",  # The name of the check holder.
    "check_number": "TEXT NOT NULL UNIQUE",  # The unique check number.
    "date": "DATETIME NOT NULL",  # The date the check was recorded.
    "FOREIGN KEY": "(payment_methods) REFERENCES payment_preferences(id)",  # Links to the 'payment_preferences' table.
}

e_wallets = {
    # The 'e_wallets' table stores details about electronic wallets.
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",  # Unique identifier for each e-wallet.
    "payment_methods": "INTEGER NOT NULL",  # The ID linking to the payment preference.
    "source_id": "INTEGER NOT NULL",  # The ID of the wallet owner.
    "source_type": "TEXT NOT NULL",  # The type of wallet owner ('employee' or 'student').
    "number": "TEXT NOT NULL UNIQUE",  # The unique phone number associated with the wallet.
    "holder_name": "TEXT NOT NULL UNIQUE",  # The name of the wallet holder, must be unique.
    "date": "DATETIME NOT NULL",  # The date the e-wallet was recorded.
    "UNIQUE": "(source_id, source_type, number, payment_methods)",  # Ensures uniqueness for this combination.
    "FOREIGN KEY": "(payment_methods) REFERENCES payment_preferences(id)",  # Links to the 'payment_preferences' table.
}

salaries = {
    # The 'salaries' table records salary payments.
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",  # Unique identifier for each salary payment.
    "emp_id": "INTEGER NOT NULL",  # The ID of the employee who received the salary.
    "payment_methods": "INTEGER NOT NULL",  # The ID linking to the payment preference used.
    "salary": "REAL NOT NULL",  # The base salary amount.
    "amount": "REAL NOT NULL",  # The net amount paid.
    "discounts": "REAL NOT NULL",  # Any discounts applied to the salary.
    "date": "DATETIME NOT NULL",  # The date and time of the salary payment.
    "FOREIGN KEY": "(emp_id) REFERENCES employees(id)",  # Links to the 'employees' table.
    "FOREIGN KEY": "(payment_methods) REFERENCES payment_preferences(id)",  # Links to the 'payment_preferences' table.
}

###########################

financial_analysis = {
    # The 'financial_analysis' table stores results of financial calculations.
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",  # Unique identifier for the analysis record.
    "analysis_type": "TEXT NOT NULL",  # The type of analysis (e.g., 'profit', 'revenue').
    "period": "DATE NOT NULL",  # The start date of the analysis period.
    "value": "REAL NOT NULL",  # The calculated value of the analysis.
    "start": "TIME NOT NULL",  # The start time of the analysis period.
    "end": "TIME NOT NULL",  # The end time of the analysis period.
    "generated_at": "DATETIME NOT NULL",  # The date and time the analysis was generated.
}

course_analytics = {
    # The 'course_analytics' table stores metrics about course performance.
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",  # Unique identifier for the analysis record.
    "course_id": "INTEGER NOT NULL",  # The ID of the course being analyzed.
    "metric_type": "TEXT NOT NULL",  # The type of metric (e.g., 'passing_rate').
    "value": "REAL NOT NULL",  # The value of the metric.
    "period": "DATE NOT NULL",  # The start date of the analysis period.
    "start": "TIME NOT NULL",  # The start time of the analysis period.
    "end": "TIME NOT NULL",  # The end time of the analysis period.
    "date": "DATETIME NOT NULL",  # The date and time the analysis was generated.
}

classroom_analytics = {
    # The 'classroom_analytics' table stores metrics about classroom usage.
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",  # Unique identifier for the analysis record.
    "classroom_id": "INTEGER NOT NULL",  # The ID of the classroom being analyzed.
    "utilization_rate": "REAL NOT NULL",  # The rate at which the classroom is used.
    "number_of_sessions": "INTEGER NOT NULL",  # The total number of sessions held.
    "average_capacity": "REAL NOT NULL",  # The average number of people in a session.
    "period": "DATE NOT NULL",  # The start date of the analysis period.
    "start": "TIME NOT NULL",  # The start time of the analysis period.
    "end": "TIME NOT NULL",  # The end time of the analysis period.
    "date": "DATETIME NOT NULL",  # The date and time the analysis was generated.
}

attendance_analytics = {
    # The 'attendance_analytics' table stores attendance metrics for individuals.
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",  # Unique identifier for the analysis record.
    "source_id": "INTEGER NOT NULL",  # The ID of the person (employee or student).
    "source_type": "TEXT NOT NULL",  # The type of person ('employee' or 'student').
    "attendance_rate": "REAL NOT NULL",  # The rate of attendance.
    "late_count": "INTEGER NOT NULL",  # The total number of late arrivals.
    "total_hours": "REAL NOT NULL",  # The total hours of attendance or work.
    "period": "DATE NOT NULL",  # The start date of the analysis period.
    "start": "TIME NOT NULL",  # The start time of the analysis period.
    "end": "TIME NOT NULL",  # The end time of the analysis period.
    "date": "DATETIME NOT NULL",  # The date and time the analysis was generated.
}


tables = [
    # This list holds the names and schemas of all tables in the database.
    ("countries", countries),
    ("governorates", governorates),
    ("payment_methods", payment_methods),
    ("class_rooms", class_rooms),
    ("courses", courses),
    ("roles", roles),
    ("employees", employees),
    ("students", students),
    ("employee_details", employee_details),
    ("student_details", student_details),
    ("employee_roles", employee_roles),
    ("users", users),
    ("user_operation", user_operation),
    ("permissions", permissions),
    ("teacher_courses", teacher_courses),
    ("exams", exams),
    ("homework", homework),
    ("attendance_employee", attendance_employee),
    ("attendance_student", attendance_student),
    ("evaluation_employee", evaluation_employee),
    ("evaluation_student", evaluation_student),
    ("exam_student", exam_student),
    ("homework_student", homework_student),
    ("student_courses", student_courses),
    ("expenses", expenses),
    ("revenues", revenues),
    ("payment_preferences", payment_preferences),
    ("bank_accounts", bank_accounts),
    ("bank_checks", bank_checks),
    ("e_wallets", e_wallets),
    ("salaries", salaries),
    ("financial_analysis", financial_analysis),
    ("course_analytics", course_analytics),
    ("classroom_analytics", classroom_analytics),
    ("attendance_analytics", attendance_analytics),
]
