import csv

class Employee:
    def __init__(self):
        self.file = "employee.csv"

    def create(self):
        empid = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        salary = input("Enter Salary: ")

        with open(self.file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([empid, name, salary])

        print("Employee added successfully!")

    def read(self):
        try:
            with open(self.file, "r") as f:
                reader = csv.reader(f)

                for row in reader:
                    print(row)

        except FileNotFoundError:
            print("File not found!")

    def update(self):
        empid = input("Enter Employee ID to update: ")

        rows = []

        with open(self.file, "r") as f:
            reader = csv.reader(f)

            for row in reader:
                if row[0] == empid:
                    row[1] = input("Enter new name: ")
                    row[2] = input("Enter new salary: ")
                rows.append(row)

        with open(self.file, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(rows)

        print("Employee updated!")

    def delete(self):
        empid = input("Enter Employee ID to delete: ")

        rows = []

        with open(self.file, "r") as f:
            reader = csv.reader(f)

            for row in reader:
                if row[0] != empid:
                    rows.append(row)

        with open(self.file, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(rows)

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