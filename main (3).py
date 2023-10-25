class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

# Create a list of student objects
students = [
    Student("Alice", "A001", 3.7),
    Student("Bob", "B002", 3.5),
    Student("Charlie", "C003", 3.9),
    Student("David", "D004", 3.6),
]

# Sort the list of students by CGPA
sorted_students = sort_students(students)

# Print the sorted list of students
for student in sorted_students:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")