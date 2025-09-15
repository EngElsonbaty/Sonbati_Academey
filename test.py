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
    "create_at": "DATETIME NOT NULL",
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
employee_roles = {
    # The 'employee_roles' table links employees to their roles.
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",  # Unique identifier for the role assignment.
    "emp_id": "INTEGER NOT NULL UNIQUE",  # The ID of the employee, must be unique to assign one role per employee.
    "role_id": "INTEGER NOT NULL",  # The ID of the assigned role.
    "create_at": "DATE NOT NULL",
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
    "role_id": "INTEGER NOT NULL",  # The ID of the role, must be unique to assign one permission set per role.
    "addition": "BOOLEAN NOT NULL DEFAULT 0 CHECK(addition IN (0, 1))",  # Permission to add data.
    "edition": "BOOLEAN NOT NULL DEFAULT 0 CHECK(edition IN (0, 1))",  # Permission to edit data.
    "deletion": "BOOLEAN NOT NULL DEFAULT 0 CHECK(deletion IN (0, 1))",  # Permission to delete data.
    "view": "BOOLEAN NOT NULL DEFAULT 0 CHECK(view IN (0, 1))",  # Permission to view data.
    "print": "BOOLEAN NOT NULL DEFAULT 0 CHECK(print IN (0, 1))",  # Permission to print data.
    "customize": "BOOLEAN NOT NULL DEFAULT 0 CHECK(customize IN (0, 1))",  # Permission to customize settings.
    "FOREIGN KEY": "(role_id) REFERENCES employee_roles(id)",  # Links to the 'employee_roles' table.
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
attendance_employee = {
    # The 'attendance_employee' table records attendance for employees.
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",  # Unique identifier for each attendance record.
    "emp_id": "INTEGER NOT NULL",  # The ID of the employee.
    "type": "TEXT NOT NULL CHECK (type IN ('in', 'out'))",  # The type of record, either 'in' or 'out'.
    "time": "TIME NOT NULL",  # The time of the attendance record.
    "created_at": "DATE NOT NULL",  # The date of the attendance record.
    "FOREIGN KEY": "(emp_id) REFERENCES employees(id)",  # Links to the 'employees' table.
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
teacher_courses = {
    # The 'teacher_courses' table links teachers to courses and classrooms.
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",  # Unique identifier for the course assignment.
    "teacher_id": "INTEGER NOT NULL",  # The ID of the teacher.
    "course_id": "INTEGER NOT NULL",  # The ID of the course.
    "class_room_id": "INTEGER NOT NULL",  # The ID of the classroom.
    "day_of_week": "TEXT NOT NULL",  # The day of the week for the class.
    "start_time": "TIME NOT NULL",  # The start time of the class.
    "end_time": "TIME NOT NULL",  # The end time of the class.
    "fees": "",
    "created_at": "DATE NOT NULL",  # The date the assignment was created.
    "FOREIGN KEY": "(teacher_id) REFERENCES employees(id)",  # Links to the 'employees' table.
    "FOREIGN KEY": "(course_id) REFERENCES courses(id)",  # Links to the 'courses' table.
    "FOREIGN KEY": "(class_room_id) REFERENCES class_rooms(id)",  # Links to the 'class_rooms' table.
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

attendance_student = {
    # The 'attendance_student' table records attendance for students.
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",  # Unique identifier for each attendance record.
    "student_id": "INTEGER NOT NULL",  # The ID of the student.
    "type": "TEXT NOT NULL CHECK (type IN ('in', 'out'))",  # The type of record, either 'in' or 'out'.
    "time": "TIME NOT NULL",  # The time of the attendance record.
    "created_at": "DATE NOT NULL",  # The date of the attendance record.
    "FOREIGN KEY": "(student_id) REFERENCES students(id)",  # Links to the 'students' table.
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
