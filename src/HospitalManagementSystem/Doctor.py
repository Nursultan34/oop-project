import mysql.connector

class Doctor:
    def __init__(self, connection, scanner):
        self.connection = connection
        self.scanner = scanner

    def doctor_logging(self):
        login = input("Please enter the login of the Doctor: ")
        password = input(f"Please enter the password of {login}: ")

        cursor = self.connection.cursor()
        cursor.execute("SELECT login, password FROM doctor WHERE login = %s", (login,))
        row = cursor.fetchone()

        if row and row[1] == password:
            print("+-------------------------+")
            print("| Login successful.       |")
            print("+-------------------------+")
        else:
            print("+------------------------------------------+")
            print("| Wrong password or login, please try again |")
            print("+------------------------------------------+")
            self.doctor_logging()

    def add_doctor(self):
        name = input("Enter Doctor Name: ")
        specialization = input("Enter Doctor Specialization: ")
        salary = input("Enter Doctor Salary: ")
        started_day = input("Enter Doctor's started day (YYYY-MM-DD): ")

        cursor = self.connection.cursor()
        cursor.execute(
            "INSERT INTO doctors (name, specialization, salary, started_day) VALUES (%s, %s, %s, %s)",
            (name, specialization, salary, started_day)
        )
        self.connection.commit()

        print("Doctor added successfully.")

    def delete_doctor(self):
        try:
            doctor_id = int(input("Enter the ID of the doctor who will be deleted: "))

            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM doctors WHERE id = %s", (doctor_id,))
            self.connection.commit()

            print(f"Doctor with ID {doctor_id} deleted successfully.")
        except ValueError:
            print("Invalid ID format.")

    def view_doctors(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM doctors")
        result = cursor.fetchall()

        if not result:
            print("No doctors available.")
        else:
            print("+------------+--------------------+------------------+---------------+--------------+")
            print("| Doctor id  | Name               | Specialization   | Salary$$$     | Date_started |")
            print("+------------+--------------------+------------------+---------------+--------------+")
            for row in result:
                print(f"| {row[0]:<10} | {row[1]:<18} | {row[2]:<16} | {row[3]:<13} | {row[4]:<12} |")
            print("+------------+--------------------+------------------+---------------+--------------+")

    def best_doctor(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM doctors ORDER BY salary DESC LIMIT 1")
        result = cursor.fetchone()

        if result:
            print(f"Best Doctor: {result[1]}, Specialization: {result[2]}, Salary: {result[3]}")
        else:
            print("No doctors available.")

    def new_doctor(self):
        # Логика для добавления нового доктора, если необходимо
        pass

    def doctors_schedule(self):
        # Логика для отображения расписания докторов, если необходимо
        pass
