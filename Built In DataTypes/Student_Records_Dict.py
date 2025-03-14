# Initialize an empty dictionary for student records
student_records = {}

def display_records():
    if not student_records:
        print("No student records available.")
    else:
        for student_id, details in student_records.items():
            print(f"ID: {student_id}, Name: {details['name']}, Grades: {details['grades']}, Attendance: {details['attendance']}")

def add_student(student_id, name, grades, attendance):
    student_records[student_id] = {'name': name, 'grades': grades, 'attendance': attendance}
    print(f"Student '{name}' added with ID {student_id}.")

def update_grades(student_id, new_grades):
    if student_id in student_records:
        student_records[student_id]['grades'] = new_grades
        print(f"Grades updated for student ID {student_id}.")
    else:
        print("Student ID not found.")

def update_attendance(student_id, new_attendance):
    if student_id in student_records:
        student_records[student_id]['attendance'] = new_attendance
        print(f"Attendance updated for student ID {student_id}.")
    else:
        print("Student ID not found.")

while True:
    print("\nStudent Records Management")
    print("1. Display student records")
    print("2. Add student")
    print("3. Update grades")
    print("4. Update attendance")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        display_records()
    elif choice == '2':
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        grades = input("Enter student grades: ")
        attendance = input("Enter student attendance: ")
        add_student(student_id, name, grades, attendance)
    elif choice == '3':
        student_id = input("Enter student ID to update grades: ")
        new_grades = input("Enter new grades: ")
        update_grades(student_id, new_grades)
    elif choice == '4':
        student_id = input("Enter student ID to update attendance: ")
        new_attendance = input("Enter new attendance: ")
        update_attendance(student_id, new_attendance)
    elif choice == '5':
        print("Exiting Student Records Management.")
        break
    else:
        print("Invalid choice. Please try again.")