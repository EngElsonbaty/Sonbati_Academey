countries = {
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
    "country_name": "TEXT NOT NULL UNIQUE",
}

payment_method = {
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
    "method_name": "TEXT NOT NULL UNIQUE",
}

employees = {
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
    "full_name": "TEXT NOT NULL",
    "address": "TEXT NOT NULL",
    "national_id": "TEXT NOT NULL UNIQUE",
    "birthday": "DATE NOT NULL",
    "gender": "TEXT NOT NULL CHECK(gender IN ('male', 'female'))",
    "id_photo": "TEXT NOT NULL",
    "photo": "TEXT NOT NULL",
}

employee_details = {
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
    "emp_id": "INTEGER NOT NULL",
    "nationality": "INTEGER NOT NULL",
    "email": "TEXT NOT NULL UNIQUE",
    "phone_number": "TEXT NOT NULL UNIQUE",
    "qualification": "TEXT NOT NULL",
    "documents": "TEXT",
    "salary": "REAL NOT NULL",
    "FOREIGN KEY": "(emp_id) REFERENCES employees(id)",
    "FOREIGN KEY": "(nationality) REFERENCES countries(id)",
}
