# Define sets for students enrolled in different exams
cet_students = {"Alice", "Bob", "Charlie", "David"}
jee_students = {"Eve", "Frank", "Charlie", "David"}
neet_students = {"George", "Hannah", "Alice", "Frank"}

# Display the sets
print("CET Students:", cet_students)
print("JEE Students:", jee_students)
print("NEET Students:", neet_students)

# Perform union operation (students appearing in any of the exams)
all_students = cet_students.union(jee_students, neet_students)
print("\nStudents appearing in any of the exams (Union):", all_students)

# Perform intersection operation (students appearing in all exams)
common_students = cet_students.intersection(jee_students, neet_students)
print("Students appearing in all exams (Intersection):", common_students)

# Perform difference operation (students appearing in CET but not in JEE)
cet_not_jee = cet_students.difference(jee_students)
print("Students appearing in CET but not in JEE (Difference):", cet_not_jee)

# Perform difference operation (students appearing in JEE but not in NEET)
jee_not_neet = jee_students.difference(neet_students)
print("Students appearing in JEE but not in NEET (Difference):", jee_not_neet)

# Perform difference operation (students appearing in NEET but not in CET)
neet_not_cet = neet_students.difference(cet_students)
print("Students appearing in NEET but not in CET (Difference):", neet_not_cet)