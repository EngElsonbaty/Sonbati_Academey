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
}
