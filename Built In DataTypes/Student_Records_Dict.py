student_records = {}

def display_records():
    if not student_records:
        print("No student records available.")
    else:
        for student_id, details in student_records.items():
            print(f"ID: {student_id}, Name: {details['name']}, Grades: {details['grades']}, Attendance: {details['attendance']}")

def add_student():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    grades = input("Enter student grades: ")
    attendance = input("Enter student attendance: ")
    student_records[student_id] = {'name': name, 'grades': grades, 'attendance': attendance}
    print(f"Student '{name}' added.")

def update_record(field):
    student_id = input("Enter student ID: ")
    if student_id in student_records:
        new_value = input(f"Enter new {field}: ")
        student_records[student_id][field] = new_value
        print(f"{field.capitalize()} updated.")
    else:
        print("Student ID not found.")

while True:
    choice = input("\n1. Display records\n2. Add student\n3. Update grades\n4. Update attendance\n5. Exit\nChoose an option: ")

    if choice == '1':
        display_records()
    elif choice == '2':
        add_student()
    elif choice == '3':
        update_record('grades')
    elif choice == '4':
        update_record('attendance')
    elif choice == '5':
        break
    else:
        print("Invalid choice.")
