import mysql.connector

class Instruction:
    def __init__(self, connection, scanner):
        self.connection = connection
        self.scanner = scanner

    def add_instruction(self):
        instruction = input("Enter Instruction: ")
        try:
            query = "INSERT INTO Instructions(instruction) VALUES (%s)"
            cursor = self.connection.cursor()
            cursor.execute(query, (instruction,))
            self.connection.commit()
            if cursor.rowcount > 0:
                print("Instruction added successfully!")
            else:
                print("Failed to add Instruction!")
        except mysql.connector.Error as e:
            print(f"Error: {e}")

    def delete_instruction(self):
        id = int(input("Enter the ID of the instruction which will be deleted: "))
        query = "DELETE FROM instruction WHERE id = %s"
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, (id,))
            self.connection.commit()
            if cursor.rowcount > 0:
                print("Instruction deleted successfully!")
            else:
                print("Failed to delete instruction!")
        except mysql.connector.Error as e:
            print(f"Error: {e}")

    def view_instructions(self):
        query = "SELECT * FROM Instructions"
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            result_set = cursor.fetchall()
            print("Instructions: ")
            print("+----------------+-----------------------------------------------------+")
            print("| Instruction id |                   Instructions                      |")
            print("+----------------+-----------------------------------------------------+")
            for row in result_set:
                id, instruction = row
                print(f"|{str(id).ljust(16)}|{instruction.ljust(53)}|")
                print("+----------------+-----------------------------------------------------+")
        except mysql.connector.Error as e:
            print(f"Error: {e}")
