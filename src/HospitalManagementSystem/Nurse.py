import mysql.connector 
from mysql.connector import (Error)

class Nurse:
    nurse_password = "321"
    nurse_login = "Nur"

    def __init__(self, connection, scanner):
        self.connection = connection
        self.scanner = scanner

    def add_nurse(self):
        name = input("Enter Nurse Name: ")
        salary = int(input("Enter Nurse Salary: "))
        date_started = input("Enter Nurse's started day: ")
        try:
            query = "INSERT INTO nurses (name, salary, date_started) VALUES (%s, %s, %s)"
            cursor = self.connection.cursor()
            cursor.execute(query, (name, salary, date_started))
            self.connection.commit()
            print("Nurse added successfully!")
        except Error as e:
            print(f"Error: {e}")

    def delete_nurse(self):
        id = int(input("Enter the ID of the nurse who will be deleted: "))
        query = "DELETE FROM nurses WHERE id = %s"
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, (id,))
            self.connection.commit()
            if cursor.rowcount > 0:
                print("Nurse deleted successfully!")
            else:
                print("Failed to delete nurse!")
        except Error as e:
            print(f"Error: {e}")

    def view_nurses(self):
        query = "SELECT * FROM nurses"
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            result_set = cursor.fetchall()
            print("Nurses: ")
            print("+------------+--------------------+---------------+--------------+")
            print("| Nurse id  | Name               | Salary$$$     | Date_started |")
            print("+------------+--------------------+---------------+--------------+")
            for row in result_set:
                id, name, salary, date_started = row
                print(f"|{id:<12}|{name:<20}|{salary:<15}|{date_started:<14}|")
                print("+------------+--------------------+---------------+--------------+")
        except Error as e:
            print(f"Error: {e}")

    @staticmethod
    def nurse_logging(scanner):
        log = True
        while log:
            login = input("Please enter the login of the nurse: ")
            password = input(f"Please enter the password of the {login}: ")

            if Nurse.nurse_password == password and Nurse.nurse_login == login:
                print()
                print("+------------------------------------------+")
                print(f"|     Greetings, dear {login}!              |")
                print("+------------------------------------------+")
                log = False
            else:
                print("+------------------------------------------+")
                print("|Wrong password or login, please try again |")
                print("+------------------------------------------+")
        print()
