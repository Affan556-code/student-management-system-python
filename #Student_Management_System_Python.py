# student_manegement.py
import json
import statistics
import os

# -------------------------------
# Student Management System
# -------------------------------

# Admin credentials
admins = {
    "affan": "affan",
    "rehan": "rehan",
    "atharva": "atharva"
}


DATA_FILE = "students.json"


def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


# Load students when program starts
students = load_data()


def add_student():
    name = input("Enter new student name: ")
    if name in students:
        print("⚠️ Student already exists!")
    else:
        students[name] = []
        save_data(students)
        print(f"✅ Student {name} added successfully.")


def add_grade():
    name = input("Enter student name: ")
    if name not in students:
        print("❌ Student not found.")
        return
    else:
        grade = int(input("Enter grade to add: "))
        students[name].append(grade)
        save_data(students)
        print("✅ Added grade {grade} to {name}")



def remove_student():
    name = input("Enter student name to remove: ")
    if name in students:
        del students[name]
        save_data(students)
        print("🗑️ Student {name} removed successfully.")
    else:
        print("❌ Student not found.")


def show_average():
    if not students:
        print("⚠️ No student data available.")
        return

    for student, grades in students.items():
        if grades:
            avg = statistics.mean(grades)
            print(f"📊 {student} has an average grade of {avg:.2f}")
        else:
            print(f"📊 {student} has no grades recorded.")


def view_students():
    if not students:
        print("⚠️ No students in the system.")
        return

    print("\n📖 Student Records:")
    for student, grades in students.items():
        print(f"👤 {student} -> {grades if grades else 'No grades yet'}")


def update_student():
    name = input("Enter student name to update: ")
    if name not in students:
        print("❌ Student not found.")
        return

    print("\n1️⃣ Rename Student\n2️⃣ Clear All Grades")
    choice = input("Choose an option: ")

    if choice == "1":
        new_name = input("Enter new name: ")
        students[new_name] = students.pop(name)
        save_data(students)
        print(f"✏️ Student {name} renamed to {new_name}")
    elif choice == "2":
        students[name] = []
        save_data(students)
        print(f"✏️ All grades cleared for {name}")
    else:
        print("❌ Invalid choice.")


def menu():
    """Main menu for student management system"""
    while True:
        print("\n📚 Student Management System")
        print("1️⃣ Add New Student")
        print("2️⃣ Add Grades")
        print("3️⃣ Remove Student")
        print("4️⃣ Show Student Averages")
        print("5️⃣ View All Students")
        print("6️⃣ Update Student Info")
        print("7️⃣ Exit")

        choice = input("Choose an option (1-7): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            add_grade()
        elif choice == "3":
            remove_student()
        elif choice == "4":
            show_average()
        elif choice == "5":
            view_students()
        elif choice == "6":
            update_student()
        elif choice == "7":
            print("👋 Exiting... Have a nice day!")
            break
        else:
            print("❌ Invalid choice. Please enter 1-7.")


def login():
    """Admin login system"""
    username = input("👤 Username: ")
    password = input("🔑 Password: ")

    if username in admins and admins[username] == password:
        print(f"✅ Welcome, {username}!")
        menu()
    else:
        print("❌ Invalid username or password.")


# -------------------------------
# Run Program
# -------------------------------
if __name__ == "__main__":
    print("🔐 Student Management System Login")
    login()
