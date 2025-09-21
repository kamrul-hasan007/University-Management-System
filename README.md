# University-Management-System

1. Base Class Person
    
  - Attributes: name, age
  - Methods: introduce() → "Hi, I am {name}, {age} years old."
    
2. Derived Classes
   
  - Student (inherits from Person)
  - Extra attribute: student_id, course_list (list of enrolled courses)
  - Methods: enroll_course(course), show_courses().
  - Teacher (inherits from Person)
  - Extra attribute: employee_id, subject
  - Override introduce() → "I am Professor {name}, teaching {subject}."
            
3. Polymorphism
   
  - Create a function display_role(person) that behaves differently if input is a Student or Teacher.
        
4. Encapsulation
   
  - In Student, make __gpa private.
  - Provide getter & setter (property) for GPA. GPA must be between 0 and 4.0.
        
5. Class Variables / Methods
    
  - Count how many Person objects have been created using a class variable.
  - Add a class method get_total_people().
 
6. Static Method
    
  - Add a static method in Student → is_valid_id(student_id) (valid if starts with "S-").
 
7. Inheritance Type

  - Add GraduateStudent class that extends Student and adds thesis_title.

    

    - Add GraduateStudent class that extends Student and adds thesis_title.
