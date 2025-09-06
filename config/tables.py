countries = {
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
    "country_name": "TEXT NOT NULL UNIQUE",
}

governorates = {
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
    "governorate_name": "TEXT NOT NULL UNIQUE",
    "country_id": "INTEGER NOT NULL",
    "FOREIGN KEY": "(country_id) REFERENCES countries(id)",
}

payment_methods = {
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
    "method_name": "TEXT NOT NULL UNIQUE",
}

class_rooms = {
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
    "classroom_name": "TEXT NOT NULL UNIQUE",
    "classroom_code": "TEXT NOT NULL UNIQUE",
}

courses = {
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
    "course_name": "TEXT NOT NULL UNIQUE",
    "course_code": "TEXT NOT NULL UNIQUE",
}

roles = {
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
    "role_name": "TEXT NOT NULL UNIQUE",
}

employees = {
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
    "full_name": "TEXT NOT NULL",
    "national_id": "TEXT NOT NULL UNIQUE",
    "birthday": "DATE NOT NULL",
    "gender": "TEXT NOT NULL CHECK(gender IN ('male', 'female'))",
    "id_photo": "TEXT NOT NULL",
    "photo": "TEXT NOT NULL",
}

employee_details = {
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
    "emp_id": "INTEGER NOT NULL UNIQUE",
    "address": "TEXT NOT NULL",
    "nationality_id": "INTEGER NOT NULL",
    "governorate_id": "INTEGER NOT NULL",
    "email": "TEXT NOT NULL UNIQUE",
    "phone_number": "TEXT NOT NULL UNIQUE",
    "qualification": "TEXT NOT NULL",
    "documents": "TEXT",
    "salary": "REAL NOT NULL",
    "FOREIGN KEY": "(emp_id) REFERENCES employees(id)",
    "FOREIGN KEY": "(nationality_id) REFERENCES countries(id)",
    "FOREIGN KEY": "(governorate_id) REFERENCES governorates(id)",
}

employee_roles = {
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
    "emp_id": "INTEGER NOT NULL UNIQUE",
    "role_id": "INTEGER NOT NULL",
    "FOREIGN KEY": "(emp_id) REFERENCES employees(id)",
    "FOREIGN KEY": "(role_id) REFERENCES roles(id)",
}

permissions = {
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
    "role_id": "INTEGER NOT NULL UNIQUE",
    "add": "BOOLEAN NOT NULL DEFAULT 0 CHECK(add IN (0, 1))",
    "edit": "BOOLEAN NOT NULL DEFAULT 0 CHECK(edit IN (0, 1))",
    "delete": "BOOLEAN NOT NULL DEFAULT 0 CHECK(delete IN (0, 1))",
    "view": "BOOLEAN NOT NULL DEFAULT 0 CHECK(view IN (0, 1))",
    "print": "BOOLEAN NOT NULL DEFAULT 0 CHECK(print IN (0, 1))",
    "customize": "BOOLEAN NOT NULL DEFAULT 0 CHECK(customize IN (0, 1))",
    "FOREIGN KEY": "(role_id) REFERENCES employee_roles(id)",
}

expenses = {
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
    "expense_type": "TEXT NOT NULL",
    "amount": "REAL NOT NULL",
    "receiver": "TEXT NOT NULL",
    "emp_id": "INTEGER NOT NULL",
    "expense_date": "DATETIME NOT NULL",
    "payment_method_id": "INTEGER NOT NULL",
    "notes": "TEXT",
    "FOREIGN KEY": "(emp_id) REFERENCES employees(id)",
}

revenues = {
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
    "income_type": "TEXT NOT NULL",
    "amount": "REAL NOT NULL",
    "source_id": "INTEGER NOT NULL",
    "emp_id": "INTEGER NOT NULL",
    "transaction_date": "DATETIME NOT NULL",
    "payment_method_id": "INTEGER NOT NULL",
    "notes": "TEXT",
    "FOREIGN KEY": "(source_id) REFERENCES students(id)",
    "FOREIGN KEY": "(emp_id) REFERENCES employees(id)",
}

salaries = {
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
    "emp_id": "INTEGER NOT NULL",
    "payment_methods": "INTEGER NOT NULL",
    "salary": "REAL NOT NULL",
    "amount": "REAL NOT NULL",
    "discounts": "REAL NOT NULL",
    "date": "DATETIME NOT NULL",
    "FOREIGN KEY": "(emp_id) REFERENCES employees(id)",
}

# edit

users = {
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
    "emp_id": "INTEGER NOT NULL UNIQUE",
    "username": "TEXT NOT NULL UNIQUE",
    "password": "TEXT NOT NULL UNIQUE",
    "FOREIGN KEY": "(emp_id) REFERENCES employees(id)",
}

teacher_courses = {
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
    "teacher_id": "INTEGER NOT NULL",
    "course_id": "INTEGER NOT NULL",
    "class_room_id": "INTEGER NOT NULL",
    "day_of_week": "TEXT NOT NULL",
    "start_time": "TIME NOT NULL",
    "end_time": "TIME NOT NULL",
    "FOREIGN KEY": "(teacher_id) REFERENCES employees(id)",
    "FOREIGN KEY": "(course_id) REFERENCES courses(id)",
    "FOREIGN KEY": "(class_room_id) REFERENCES class_rooms(id)",
}

exams = {
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
    "course_id": "INTEGER NOT NULL",
    "teacher_id": "INTEGER NOT NULL",
    "class_rooms_id": "INTEGER NOT NULL",
    "finally_grade": "REAL NOT NULL",
    "full_time": "TIME NOT NULL",
    "start_time": "TIME NOT NULL",
    "end_time": "TIME NOT NULL",
    "date": "DATE NOT NULL",
    "FOREIGN KEY": "(teacher_id) REFERENCES employees(id)",
    "FOREIGN KEY": "(course_id) REFERENCES courses(id)",
    "FOREIGN KEY": "(class_rooms_id) REFERENCES class_rooms(id)",
}

homework = {
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
    "teacher_id": "INTEGER NOT NULL",
    "course_id": "INTEGER NOT NULL",
    "class_room_id": "INTEGER NOT NULL",
    "date": "DATETIME NOT NULL",
    "FOREIGN KEY": "(student_id) REFERENCES students(id)",
    "FOREIGN KEY": "(nationality_id) REFERENCES countries(id)",
    "FOREIGN KEY": "(governorate_id) REFERENCES governorates(id)",
}

students = {
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
    "full_name": "TEXT NOT NULL",
    "national_id": "TEXT NOT NULL UNIQUE",
    "birthday": "DATE NOT NULL",
    "gender": "TEXT NOT NULL CHECK(gender IN ('male', 'female'))",
    "id_photo": "TEXT NOT NULL",
    "photo": "TEXT NOT NULL",
}

student_details = {
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
    "student_id": "INTEGER NOT NULL UNIQUE",
    "address": "TEXT NOT NULL",
    "nationality_id": "INTEGER NOT NULL",
    "governorate_id": "INTEGER NOT NULL",
    "email": "TEXT NOT NULL UNIQUE",
    "phone_number": "TEXT NOT NULL UNIQUE",
    "fees": "REAL NOT NULL",
    "FOREIGN KEY": "(student_id) REFERENCES students(id)",
    "FOREIGN KEY": "(nationality_id) REFERENCES countries(id)",
    "FOREIGN KEY": "(governorate_id) REFERENCES governorates(id)",
}

user_operation = {
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
    "emp_id": "INTEGER NOT NULL",
    "operation_type": "TEXT NOT NULL",
    "date": "DATETIME NOT NULL",
    "FOREIGN KEY": "(emp_id) REFERENCES employees(id)",
}
