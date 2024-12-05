'''PYCODE | @_py.code'''

# ? 7. Student Management System
# ? Features: Add, view, update, and delete student records.

# * Source Code
def display_menu():
    print("\n--- Student Manager ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

def add_student(students):
    student_id = input("Enter Student ID: ")
    if student_id in students:
        print("Student ID already exists!")
        return
    name = input("Enter Student Name: ")
    age = input("Enter Student Age: ")
    grade = input("Enter Student Grade: ")
    students[student_id] = {"Name": name, "Age": age, "Grade": grade}
    print(f"Student {name} added successfully!")

def view_students(students):
    if not students:
        print("No student records found.")
        return
    print("\n--- Student Records ---")
    for student_id, details in students.items():
        print(f"ID: {student_id}, Name: {details['Name']}, Age: {details['Age']}, Grade: {details['Grade']}")

def update_student(students):
    student_id = input("Enter Student ID to update: ")
    if student_id not in students:
        print("Student ID not found!")
        return
    print(f"Updating record for Student ID: {student_id}")
    name = input("Enter new name (leave blank to keep current): ") or students[student_id]['Name']
    age = input("Enter new age (leave blank to keep current): ") or students[student_id]['Age']
    grade = input("Enter new grade (leave blank to keep current): ") or students[student_id]['Grade']
    students[student_id] = {"Name": name, "Age": age, "Grade": grade}
    print("Student record updated successfully!")

def delete_student(students):
    student_id = input("Enter Student ID to delete: ")
    if student_id not in students:
        print("Student ID not found!")
        return
    confirm = input(f"Are you sure you want to delete Student ID: {student_id}? (yes/no): ")
    if confirm.lower() == 'yes':
        del students[student_id]
        print("Student record deleted successfully!")
    else:
        print("Deletion canceled.")

def main():
    students = {}
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_student(students)
        elif choice == '2':
            view_students(students)
        elif choice == '3':
            update_student(students)
        elif choice == '4':
            delete_student(students)
        elif choice == '5':
            print("Exiting Student Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
