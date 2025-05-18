import mysql.connector  # для подключения к базе данных
from mysql.connector import Error

class Appointments:
    def __init__(self, connection):
        self.connection = connection

    def view_appointments(self):
        query = "SELECT * FROM appointments"
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            result_set = cursor.fetchall()
            print("Appointments: ")
            print("+----+------------+-----------+------------------+")
            print("| id | patient_id | doctor_id | appointment_date |")
            print("+----+------------+-----------+------------------+")
            for row in result_set:
                id, patient_id, doctor_id, appointment_date = row
                print(f"|{id:<4}|{patient_id:<12}|{doctor_id:<11}|{appointment_date:<18}|")
                print("+----+------------+-----------+------------------+")
        except Error as e:
            print(f"Error: {e}")
