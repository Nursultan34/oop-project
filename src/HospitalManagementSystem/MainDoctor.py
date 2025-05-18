import sys 
import mysql.connector

class MainDoctor:
    main_doctor_password = "321"
    main_doctor_login = "Main"

    def __init__(self, connection):
        self.connection = connection  

    def main_doctor_logging(self):
        log = True
        while log:
            login = input("Please enter the login of the mainDoctor: ")
            password = input(f"Please enter the password of {login}: ")

            if self.main_doctor_password == password and self.main_doctor_login == login:
                print()
                print("+------------------------------------------+")
                print(f"|     Greetings, dear {login}!{' ' * (22 - len(login))}|")
                print("+------------------------------------------+")
                log = False
            else:
                print("+------------------------------------------+")
                print("|Wrong password or login, please try again |")
                print("+------------------------------------------+")
        print()

# Пример подключения к базе данных
if __name__ == "__main__":
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password",  # Укажи свой пароль
            database="hms"
        )

        # Создание экземпляра класса и вызов метода
        main_doctor = MainDoctor(connection)
        main_doctor.main_doctor_logging()

        connection.close()

    except mysql.connector.Error as err:
        print(f"Database connection error: {err}")
        sys.exit(1)
