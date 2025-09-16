"""
This file defines the database schema for the educational management system.
Each dictionary represents a table, with keys as column names and values as
SQL data types and constraints.
"""



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


# tables = [
#     # This list holds the names and schemas of all tables in the database.
#     ("countries", countries),
#     ("governorates", governorates),
#     ("payment_methods", payment_methods),
#     ("class_rooms", class_rooms),
#     ("courses", courses),
#     ("roles", roles),
#     ("employees", employees),
#     ("students", students),
#     ("employee_details", employee_details),
#     ("student_details", student_details),
#     ("employee_roles", employee_roles),
#     ("users", users),
#     ("user_operation", user_operation),
#     ("permissions", permissions),
#     ("teacher_courses", teacher_courses),
#     ("exams", exams),
#     ("homework", homework),
#     ("attendance_employee", attendance_employee),
#     ("attendance_student", attendance_student),
#     ("evaluation_employee", evaluation_employee),
#     ("evaluation_student", evaluation_student),
#     ("exam_student", exam_student),
#     ("homework_student", homework_student),
#     ("student_courses", student_courses),
#     ("expenses", expenses),
#     ("revenues", revenues),
#     ("payment_preferences", payment_preferences),
#     ("bank_accounts", bank_accounts),
#     ("bank_checks", bank_checks),
#     ("e_wallets", e_wallets),
#     ("salaries", salaries),
#     ("financial_analysis", financial_analysis),
#     ("course_analytics", course_analytics),
#     ("classroom_analytics", classroom_analytics),
#     ("attendance_analytics", attendance_analytics),
# ]
