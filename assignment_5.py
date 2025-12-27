student_marks = {
    "Rahul": 85,
    "Anita": 92,
    "Sumit": 78,
    "Priya": 88
}
name = input("Enter student name: ")

if name in student_marks:
    print("Marks:", student_marks[name])
else:
    print("Student not found")
