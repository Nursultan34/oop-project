import mysql.connector
import sys

from Patient import Patient
from Doctor import Doctor
from Nurse import Nurse
from MainDoctor import MainDoctor
from Instruction import Instruction

def main():
    url = "localhost"
    database = "hms"
    username = "root"
    password = "1234"

    try:
        connection = mysql.connector.connect(
            host=url,
            user=username,
            password=password,
            database=database
        )

        cursor = connection.cursor()
        import builtins
        scanner = builtins.input

        patient = Patient(connection, scanner)
        doctor = Doctor(connection, scanner)
        nurse = Nurse(connection, scanner)
        main_doctor = MainDoctor(connection)
        instruction = Instruction(connection, scanner)

        while True:
            print()
            print("====================================")
            print("    HOSPITAL MANAGEMENT SYSTEM")
            print("====================================")
            print()
            print("FOR STARTING THE PROGRAM, PLEASE ENTER THE TYPE OF THE ACCOUNT: ")
            print("+--------------+")
            print("| MainDoctor   |")
            print("| Doctor       |")
            print("| Nurse        |")
            print("| Patient      |")
            print("+--------------+")
            print()
            account_type = input("Enter account type: ").lower()

            if account_type == "maindoctor":
                main_doctor.main_doctor_logging()  # Исправлено
                while True:
                    print("====================================")
                    print("    HOSPITAL MANAGEMENT SYSTEM")
                    print("====================================")
                    print("Greetings, dear, MainDoctor! ")
                    print("Please dial the menu number to work with the program,")
                    print("if finished, then dial 4:")
                    print("+--------------+")
                    print("| 1-Doctors    |")
                    print("| 2-Patients   |")
                    print("| 3-Nurses     |")
                    print("| 4-Exit       |")
                    print("+--------------+")
                    num = int(input("Select an Option: "))
                    print(" ")

                    if num == 1:
                        print("+------------------------+")
                        print("| 1. Add Doctor           |")
                        print("| 2. Delete Doctor        |")
                        print("| 3. View Doctors         |")
                        print("| 4. Best Doctor          |")
                        print("| 5. New Doctor           |")
                        print("| 6. Doctor's Schedule    |")
                        print("+------------------------+")
                        choice = int(input("Choose one: "))
                        print(" ")
                        if choice == 1:
                            doctor.add_doctor()
                        elif choice == 2:
                            doctor.delete_doctor()
                        elif choice == 3:
                            doctor.view_doctors()
                        elif choice == 4:
                            doctor.best_doctor()
                        elif choice == 5:
                            doctor.new_doctor()
                        elif choice == 6:
                            doctor.doctors_schedule()

                    elif num == 2:
                        print("+----------------------+")
                        print("| 1. Add Patient       |")
                        print("| 2. Delete Patient    |")
                        print("| 3. View Patients     |")
                        print("+----------------------+")
                        choice = int(input("Choose one: "))
                        print(" ")
                        if choice == 1:
                            patient.add_patient()
                        elif choice == 2:
                            patient.delete_patient()
                        elif choice == 3:
                            patient.view_patients()

                    elif num == 3:
                        print("+------------------------------------------+")
                        print("| 1. Add Nurse    | 4.Add Instruction      |")
                        print("| 2. Delete Nurse | 5.Delete Instruction   |")
                        print("| 3. View Nurses  | 6.View Instructions    |")
                        print("+------------------------------------------+")
                        choice = int(input("Choose one: "))
                        print(" ")
                        if choice == 1:
                            nurse.add_nurse()
                        elif choice == 2:
                            nurse.delete_nurse()
                        elif choice == 3:
                            nurse.view_nurses()
                        elif choice == 4:
                            instruction.add_instruction()
                        elif choice == 5:
                            instruction.delete_instruction()
                        elif choice == 6:
                            instruction.view_instructions()

                    elif num == 4:
                        sys.exit()
                    else:
                        print("invalid option")

            elif account_type == "doctor":
                doctor.doctor_logging()
                while True:
                    print("====================================")
                    print("    HOSPITAL MANAGEMENT SYSTEM")
                    print("====================================")
                    print("Greetings, dear, Doctor! ")
                    print("Please dial the menu number to work with the program,")
                    print("if finished, then dial 3:")
                    print("+---------------+")
                    print("| 1-Patients    |")
                    print("| 2-Nurses      |")
                    print("| 3-Exit        |")
                    print("+---------------+")
                    num = int(input("Select an Option: "))
                    print(" ")

                    if num == 1:
                        print("+----------------------+")
                        print("| 1. Add Patient       |")
                        print("| 2. Delete Patient    |")
                        print("| 3. View Patients     |")
                        print("+----------------------+")
                        choice = int(input("Choose one: "))
                        print(" ")
                        if choice == 1:
                            patient.add_patient()
                        elif choice == 2:
                            patient.delete_patient()
                        elif choice == 3:
                            patient.view_patients()

                    elif num == 2:
                        print("+------------------------------------------+")
                        print("| 1. Add Nurse    | 4.Add Instruction      |")
                        print("| 2. Delete Nurse | 5.Delete Instruction   |")
                        print("| 3. View Nurses  | 6.View Instructions    |")
                        print("+------------------------------------------+")
                        choice = int(input("Choose one: "))
                        print(" ")
                        if choice == 1:
                            nurse.add_nurse()
                        elif choice == 2:
                            nurse.delete_nurse()
                        elif choice == 3:
                            nurse.view_nurses()
                        elif choice == 4:
                            instruction.add_instruction()
                        elif choice == 5:
                            instruction.delete_instruction()
                        elif choice == 6:
                            instruction.view_instructions()

                    elif num == 3:
                        sys.exit()
                    else:
                        print("invalid option")

            elif account_type == "nurse":
                nurse.nurse_logging()
                while True:
                    print("====================================")
                    print("    HOSPITAL MANAGEMENT SYSTEM")
                    print("====================================")
                    print("Greetings, dear, Nurse! ")
                    print("Please dial the menu number to work with the program,")
                    print("if finished, then dial 4:")
                    print("+-------------------------+")
                    print("| 1. View Patients        |")
                    print("| 2. View Instructions    |")
                    print("| 3. Find Patient(by ID)  |")
                    print("| 4. Exit                 |")
                    print("+-------------------------+")
                    choice = int(input("Choose one: "))
                    print(" ")
                    if choice == 1:
                        patient.view_patients()
                    elif choice == 2:
                        instruction.view_instructions()
                    elif choice == 3:
                        id = int(input("Enter patient ID: "))
                        found = patient.get_patient_by_id(id)
                        print("Patient found: " + str(found))
                    elif choice == 4:
                        sys.exit()

            elif account_type == "patient":
                patient.patient_logging()
                while True:
                    print("====================================")
                    print("    HOSPITAL MANAGEMENT SYSTEM")
                    print("====================================")
                    print("Greetings, dear, Patient! ")
                    print("Please dial the menu number to work with the program,")
                    print("if finished, then dial 3:")
                    print("+-----------------------+")
                    print("| 1. My Information     |")
                    print("| 2. Doctor's Schedule  |")
                    print("| 3. Exit               |")
                    print("+-----------------------+")
                    choice = int(input("Choose one: "))
                    print(" ")
                    if choice == 1:
                        id = int(input("Enter your ID: "))
                        patient.patient_information(id)
                    elif choice == 2:
                        doctor.doctors_schedule()
                    elif choice == 3:
                        sys.exit()

            else:
                print("invalid account type")

    except mysql.connector.Error as e:
        print(f"Database connection error: {e}")

if __name__ == "__main__":
    main()
