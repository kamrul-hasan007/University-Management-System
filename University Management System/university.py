# Base Class Person
class Person:
    total_people = 0   # class variable to count created objects

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.total_people += 1

    def introduce(self):
        return f"Hi, I am {self.name}, {self.age} years old."

    @classmethod
    def get_total_people(cls):
        return f"Total people created: {cls.total_people}"


# Derived Class: Student
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        self.course_list = []
        self.__gpa = 0.0  # private attribute

    def enroll_course(self, course):
        self.course_list.append(course)

    def show_courses(self):
        return f"{self.name}'s Courses: {', '.join(self.course_list)}"

    # Getter & Setter for GPA (Encapsulation)
    @property
    def gpa(self):
        return self.__gpa

    @gpa.setter
    def gpa(self, value):
        if 0.0 <= value <= 4.0:
            self.__gpa = value
        else:
            raise ValueError("GPA must be between 0.0 and 4.0")

    # Static method
    @staticmethod
    def is_valid_id(student_id):
        return student_id.startswith("S-")


# Derived Class: Teacher
class Teacher(Person):
    def __init__(self, name, age, employee_id, subject):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.subject = subject

    def introduce(self):  # method overriding
        return f"I am Professor {self.name}, teaching {self.subject}."


# GraduateStudent (extends Student)
class GraduateStudent(Student):
    def __init__(self, name, age, student_id, thesis_title):
        super().__init__(name, age, student_id)
        self.thesis_title = thesis_title

    def show_thesis(self):
        return f"Thesis Title: {self.thesis_title}"


# Polymorphism function
def display_role(person):
    if isinstance(person, Student):
        return f"{person.name} is a Student."
    elif isinstance(person, Teacher):
        return f"{person.name} is a Teacher."
    else:
        return f"{person.name}'s role is undefined."


# ----------- Testing the System -----------

# Create objects
p1 = Person("Alice", 30)
s1 = Student("Bob", 20, "S-123")
t1 = Teacher("Dr. Smith", 45, "T-101", "Computer Science")
g1 = GraduateStudent("Charlie", 25, "S-456", "AI in Healthcare")

# Student actions
s1.enroll_course("Math")
s1.enroll_course("Physics")
s1.gpa = 3.8

# Display Information
print(p1.introduce())
print(s1.introduce())
print(s1.show_courses())
print(f"GPA: {s1.gpa}")
print(t1.introduce())
print(display_role(s1))
print(display_role(t1))
print(g1.show_thesis())
print(Person.get_total_people())

# Static Method Test
print("Valid ID?", Student.is_valid_id("S-789"))
print("Valid ID?", Student.is_valid_id("123"))
