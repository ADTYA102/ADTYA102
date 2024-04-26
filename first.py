class Student:
    def __init__(self, name, roll_no, marks={}):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def add_marks(self, subject, mark):
        self.marks[subject] = mark

    def display_details(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Marks:")
        for subject, mark in self.marks.items():
            print(f"{subject}: {mark}")

class MonitoringSystem:
    def __init__(self, file_name):
        self.file_name = file_name

    def add_student(self, student):
        with open(self.file_name, 'a') as file:
            file.write(f"{student.name},{student.roll_no},")
            for subject, mark in student.marks.items():
                file.write(f"{subject}:{mark},")
            file.write("\n")

    def get_students(self):
        students = []
        with open(self.file_name, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                if len(data) < 3:  # Ensure there are at least three elements (name, roll_no, marks)
                    continue
                name = data[0]
                roll_no = data[1]
                marks_data = data[2:]
                marks = {}
                for mark_data in marks_data:
                    mark_info = mark_data.split(':')
                    if len(mark_info) != 2:  # Ensure each mark data has two parts (subject, mark)
                        continue
                    subject, mark = mark_info
                    marks[subject] = int(mark)
                student = Student(name, roll_no, marks)
                students.append(student)
        return students


# Example usage:
monitoring_system = MonitoringSystem("student_data.txt")

# Adding a new student
new_student = Student("John Doe", "101")
new_student.add_marks("Maths", 90)
new_student.add_marks("Science", 85)
monitoring_system.add_student(new_student)

# Displaying all students
all_students = monitoring_system.get_students()
for student in all_students:
    student.display_details()
    print()
