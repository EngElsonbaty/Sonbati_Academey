from config.tables import tables

from modules.database_manager import db
from modules.shared.countries_table_manager import CountriesTableManager
from modules.shared.payment_methods_table_manager import PaymentMethodsTableManager
from modules.shared.roles_table_manager import RolesTableManager

from faker import Faker
import random
from datetime import date

for table in tables:
    print(db.create_table(table[0], table[1]))

c = CountriesTableManager()
p = PaymentMethodsTableManager()
r = RolesTableManager()

from modules.employees_manager import EmployeesManager


# def create_fake_employee_data(number_of_records: int):
#     """
#     Creates a specified number of fake employee, details, and user records.

#     Args:
#         number_of_records (int): The number of records to generate.

#     Returns:
#         tuple: A tuple containing three lists of dictionaries:
#                (employees_data, details_data, users_data)
#     """
#     fake = Faker("en_US")  # Using 'en_US' for generic data.
#     status = []
#     e = EmployeesManager()
#     # This loop generates the specified number of fake records.
#     for i in range(1, number_of_records + 1):
#         # 1. Generate data for the 'employees' table
#         employee_record = {
#             "full_name": fake.name(),
#             # Simulating a unique 14-digit national ID.
#             "national_id": fake.unique.random_number(digits=14),
#             # Generating a birthday for an adult employee.
#             "birthday": fake.date_of_birth(minimum_age=18, maximum_age=60),
#             # Randomly selecting 'male' or 'female' to match the CHECK constraint.
#             "gender": random.choice(["male", "female"]),
#             # Generating a placeholder path for an ID photo.
#             "id_photo": f"media/photos/id/{fake.uuid4()}.jpg",
#             # Generating a placeholder path for a personal photo.
#             "photo": f"media/photos/employee/{fake.uuid4()}.jpg",
#         }

#         # 2. Generate data for the 'employee_details' table
#         details_record = {
#             "address": fake.address(),
#             # Simulating a foreign key for a nationality ID.
#             "nationality_id": random.randint(1, 20),
#             # Simulating a foreign key for a governorate ID (assuming 27 governorates in Egypt).
#             "governorate_id": random.randint(1, 27),
#             # Generating a unique email address.
#             "email": fake.unique.email(),
#             # Generating a unique phone number.
#             "phone_number": fake.unique.phone_number(),
#             # Generating a random job title as a qualification.
#             "qualification": fake.job(),
#             # Generating a placeholder path for documents.
#             "documents": f"media/documents/{fake.uuid4()}.pdf",
#             # Generating a realistic salary amount.
#             "salary": fake.random_int(min=5000, max=50000),
#         }

#         # 3. Generate data for the 'users' table
#         users_record = {
#             # Generating a unique username.
#             "username": fake.unique.user_name(),
#             # Generating a unique password (Note: In a real app, this should be a hashed value).
#             "password": fake.unique.password(),
#         }
#         status.append(
#             e.create("admin", 1, employee_record, details_record, users_record)
#         )
#         print(f"Loop is: {i}")

#     return status


# print(create_fake_employee_data(1000000))
