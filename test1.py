from test import payment_method, counties, governorate_master, e_wallets, bank_account
from random import randint, choice, choices, random
from modules.employees.teacher_courses_table_manager import TeacherCoursesTableManager
from faker import Faker
from services.students_manager import StudentsManager
from modules.database_manager import db

courses = TeacherCoursesTableManager().get(0, False, True)


def generate_country_and_governorate():
    index_country = randint(0, len(counties) - 1)
    country_id, country_name = counties[index_country]
    governorate_id, country_governorate, governorate_name = None, None, None
    for i in governorate_master:
        if country_id == i[1]:
            governorate_id, country_governorate, governorate_name = i
            break
    return (country_id, governorate_id)


def generate_course():
    index_course = randint(0, len(courses) - 1)
    course_id = courses[index_course][0]
    return course_id


def generate_payment():
    index_payment = randint(0, len(payment_method) - 1)
    payment_id, payment_name = payment_method[index_payment]
    return (payment_id, payment_name)


def generate_info():
    country = generate_country_and_governorate()
    payment_method = generate_payment()
    f = Faker("en_US")
    students = {
        "full_name": f.name(),  # The full name of the student.
        "national_id": str(
            f.random_number(25)
        ),  # The national ID of the student, must be unique.
        "birthday": f.date_of_birth(
            minimum_age=20, maximum_age=30
        ),  # The student's date of birth.
        "gender": choices(["male", "female"])[
            0
        ],  # The gender, must be 'male' or 'female'.
        "id_photo": f.file_path(
            category="images", extension="jpg"
        ),  # Path to the student's ID photo.
        "photo": f.file_path(
            category="images", extension="jpg"
        ),  # Path to the student's personal photo.
    }
    student_details = {
        "address": f.address(),  # The student's residential address.
        "nationality_id": country[0],  # The ID of the student's nationality.
        "governorate_id": country[1],  # The ID of the student's governorate.
        "email": f.email(),  # The student's email address, must be unique.
        "phone_number": str(
            f.phone_number()
        ),  # The student's phone number, must be unique.
        "fees": randint(500, 5000),  # The student's fees.
    }

    student_courses = {
        "teacher_course_id": generate_course(),  # The ID of the specific course schedule.
        "join_date": f.date(),  # The date the student joined the course.
    }
    payment_preferences = {
        "source_type": "Student",  # The type of person ('employee' or 'student').
        "payment_method_id": payment_method[0],  # The ID of the payment method.
        "created_at": f.date(),  # The date and time the preference was set.
    }
    e_wallets_student = {}
    bank_accounts = {}
    if payment_method[1] in e_wallets:
        e_wallets_student = {
            "payment_methods": payment_method[
                0
            ],  # The ID linking to the payment preference.
            "source_id": "INTEGER NOT NULL",  # The ID of the wallet owner.
            "source_type": "TEXT NOT NULL",  # The type of wallet owner ('employee' or 'student').
            "number": str(
                f.random_number(25)
            ),  # The unique phone number associated with the wallet.
            "holder_name": f.name(),  # The name of the wallet holder, must be unique.
            "date": f.date(),  # The date the e-wallet was recorded.
        }
    elif payment_method[1] in bank_account:
        bank_accounts = {
            "payment_methods": payment_method[
                0
            ],  # The ID linking to the payment preference.
            "source_id": "INTEGER NOT NULL",  # The ID of the account holder.
            "source_type": "TEXT NOT NULL",  # The type of account holder ('employee' or 'student').
            "holder_name": f.name(),  # The name of the account holder.
            "bank_name": f.name(),  # The name of the bank.
            "account_number": str(f.random_number(25)),  # The unique account number.
            "iban": str(f.random_number(25)),  # The unique IBAN number.
            "date": f.date(),  # The date the account was recorded.
        }
    return (
        students,
        student_details,
        student_courses,
        payment_preferences,
        e_wallets_student,
        bank_accounts,
        payment_method,
    )


def generate(n: int):
    last_id = db.get_last_row("students", "id") + 1
    student = StudentsManager()
    status = []
    for i in range(last_id, last_id + n):
        results_student = generate_info()
        results = student.create(
            info_master=results_student[0],
            student_details=results_student[1],
            student_course=results_student[2],
            payment_method=results_student[6][1],
            payment_info=results_student[3],
            e_wallet=results_student[4],
            bank_account=results_student[5],
        )
        status.append(results)
        print(f"Loop Index is: {i}")
    return all(status)


print(generate(1000))
