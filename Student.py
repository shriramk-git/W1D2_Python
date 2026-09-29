# Simple Student Grade Manager

name = input("Enter student name: ")
mark = float(input("Enter mark: "))

if mark >= 80:
    grade = "A"
    message = "Good job!"
elif mark >= 70:
    grade = "B"
    message = ""
elif mark >= 60:
    grade = "D"
    message = ""
elif mark >= 50:
    grade = "E"
    message = ""
else:
    grade = "Fail"
    message = "Study well."

print("\n--- Student Result ---")
print("Student Name:", name)
print("Mark:", mark)
print("Grade:", grade)

if message:
    print(message)
