import mysql.connector

class Employee:

    def __init__(self):
        self.con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="MySQL@12345",
            database="company"
        )
        self.cur = self.con.cursor()

    def create(self):
        empid = int(input("Enter Employee ID: "))
        name = input("Enter Name: ")
        salary = float(input("Enter Salary: "))

        query = "INSERT INTO employee VALUES (%s, %s, %s)"
        self.cur.execute(query, (empid, name, salary))

        self.con.commit()
        print("Employee added!")

    def read(self):
        self.cur.execute("SELECT * FROM employee")

        for row in self.cur.fetchall():
            print(row)

    def update(self):
        empid = int(input("Enter Employee ID: "))
        name = input("Enter new name: ")
        salary = float(input("Enter new salary: "))

        query = "UPDATE employee SET name=%s, salary=%s WHERE empid=%s"

        self.cur.execute(query, (name, salary, empid))

        self.con.commit()
        print("Employee updated!")

    def delete(self):
        empid = int(input("Enter Employee ID: "))

        query = "DELETE FROM employee WHERE empid=%s"

        self.cur.execute(query, (empid,))

        self.con.commit()
        print("Employee deleted!")


e = Employee()

while True:
    print("\n1. Create")
    print("2. Read")
    print("3. Update")
    print("4. Delete")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        e.create()
    elif choice == "2":
        e.read()
    elif choice == "3":
        e.update()
    elif choice == "4":
        e.delete()
    elif choice == "5":
        break
    else:
        print("Invalid choice")