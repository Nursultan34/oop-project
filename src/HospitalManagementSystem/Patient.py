import mysql.connector  # для подключения к базе данных
from mysql.connector import Error

class Patient:
    patient_password = "321"
    patient_login = "Pat"

    def __init__(self, connection, scanner):
        self.connection = connection
        self.scanner = scanner

    def add_patient(self):
        name = input("Enter Patient Name: ")
        age = int(input("Enter Patient Age: "))
        gender = input("Enter Patient Gender: ")
        height = int(input("Enter Patient Height: "))
        weight = float(input("Enter Patient Weight: "))
        illness = input("Enter Patient Illness: ")
        dob = input("Enter Patient Date of Birth: ")
        arrival_date = input("Enter Patient's Arrival Date: ")

        try:
            query = "INSERT INTO patients (name, age, gender, height, weight, illness, dob, arrival_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            cursor = self.connection.cursor()
            cursor.execute(query, (name, age, gender, height, weight, illness, dob, arrival_date))
            self.connection.commit()
            print("Patient added successfully!")
        except Error as e:
            print(f"Error: {e}")

    def delete_patient(self):
        id = int(input("Enter the ID of the patient who will be deleted: "))
        query = "DELETE FROM patients WHERE id = %s"
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, (id,))
            self.connection.commit()
            if cursor.rowcount > 0:
                print("Patient deleted successfully!")
            else:
                print("Failed to delete Patient!")
        except Error as e:
            print(f"Error: {e}")

    def view_patients(self):
        query = "SELECT * FROM patients"
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            result_set = cursor.fetchall()
            print("Patients: ")
            print("+------------+--------------------+------+---------+--------+--------+------------+------------+--------------+")
            print("| Patient ID | Name               | Age  | Gender  | Height | Weight | Illness    | DoB        | Arrival Date |")
            print("+------------+--------------------+------+---------+--------+--------+------------+------------+--------------+")
            for row in result_set:
                id, name, age, gender, height, weight, illness, dob, arrival_date = row
                print(f"|{id:<12}|{name:<20}|{age:<6}|{gender:<9}|{height:<8}|{weight:<8}|{illness:<12}|{dob:<12}|{arrival_date:<14}|")
                print("+------------+--------------------+------+---------+--------+--------+------------+------------+--------------+")
        except Error as e:
            print(f"Error: {e}")

    def get_patient_by_id(self, id):
        query = "SELECT * FROM patients WHERE id = %s"
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, (id,))
            result_set = cursor.fetchone()
            if result_set:
                return True
            else:
                return False
        except Error as e:
            print(f"Error: {e}")
        return False

    def patient_information(self, id):
        query = "SELECT * FROM patients WHERE id = %s"
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, (id,))
            result_set = cursor.fetchone()
            if result_set:
                print("Patient: ")
                print("+------------+--------------------+------+---------+--------+--------+------------+------------+--------------+")
                print("| Patient ID | Name               | Age  | Gender  | Height | Weight | Illness    | DoB        | Arrival Date |")
                print("+------------+--------------------+------+---------+--------+--------+------------+------------+--------------+")
                id, name, age, gender, height, weight, illness, dob, arrival_date = result_set
                print(f"|{id:<12}|{name:<20}|{age:<6}|{gender:<9}|{height:<8}|{weight:<8}|{illness:<12}|{dob:<12}|{arrival_date:<14}|")
                print("+------------+--------------------+------+---------+--------+--------+------------+------------+--------------+")
            else:
                print("Data not found.")
        except Error as e:
            print(f"Error: {e}")

    @staticmethod
    def patient_logging(scanner):
        log = True
        while log:
            login = input("Please enter the login of the patient: ")
            password = input(f"Please enter the password of the {login}: ")

            if Patient.patient_password == password and Patient.patient_login == login:
                print()
                print("+------------------------------------------+")
                print(f"|     Greetings, dear {login}!                 |")
                print("+------------------------------------------+")
                log = False
            else:
                print("+------------------------------------------+")
                print("|Wrong password or login, please try again |")
                print("+------------------------------------------+")
        print()
