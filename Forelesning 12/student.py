class Student:
    def __init__(self, first_name, last_name, age, student_id):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.student_id = student_id
        self.courses = []

    def get_full_name(self):
        return self.first_name + " " + self.last_name
    
    def enroll_student(self, course):
        self.courses.append(course)
        

class Course:
    def __init__(self, name, code, credit):
        self.name = name
        self.code = code
        self.credits = credit


programmering1 = Course("Programmering 1", "ITF123", 10)
webutvikling = Course("Webutvikling", "ITF124", 10)

linus = Student("Linus", "Torvalds", 25, "060504")
tesla = Student("Nikola", "Tesla", 33, "888888")

linus.enroll_student(programmering1)
linus.enroll_student(webutvikling)

print(f"{linus.get_full_name()} takes:")
for course in linus.courses:
    print(course.name)

print(f"\n{tesla.get_full_name()}")


# first_name = input("Student first name: ")
# last_name = input("Student last name: ")
#
# new_student = Student(first_name, last_name, 0, "000000")
# print(new_student.get_full_name())