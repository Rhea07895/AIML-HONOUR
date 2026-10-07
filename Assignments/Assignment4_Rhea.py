import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="MySQL@12345",
    database="company"
)

cur = con.cursor()

while True:

    print("\n1. Insert Employee")
    print("2. Display Employees")
    print("3. Update Employee")
    print("4. Delete Employee")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        empid = int(input("Enter Employee ID: "))
        name = input("Enter Name: ")
        salary = float(input("Enter Salary: "))

        query = "INSERT INTO employee VALUES (%s, %s, %s)"
        cur.execute(query, (empid, name, salary))

        con.commit()

        print("Employee inserted successfully!")

    elif choice == "2":

        cur.execute("SELECT * FROM employee")

        for row in cur.fetchall():
            print(row)

    elif choice == "3":

        empid = int(input("Enter Employee ID: "))
        name = input("Enter new name: ")
        salary = float(input("Enter new salary: "))

        query = "UPDATE employee SET name=%s, salary=%s WHERE empid=%s"

        cur.execute(query, (name, salary, empid))

        con.commit()

        print("Employee updated successfully!")

    elif choice == "4":

        empid = int(input("Enter Employee ID: "))

        query = "DELETE FROM employee WHERE empid=%s"

        cur.execute(query, (empid,))

        con.commit()

        print("Employee deleted successfully!")

    elif choice == "5":
        break

    else:
        print("Invalid choice")
