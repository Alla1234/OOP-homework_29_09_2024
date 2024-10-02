# Задание № 1 : Наследование
class Mentor: # Класс Mentor - родительский класс
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
mentor = Mentor('Stewe', 'Jobs')
class Mentor: 
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return f'Name: {self.name}'

mentor = Mentor('Stewe')
print(mentor)

class Mentor:
    def __init__(self, surname):
        self.surname = surname
        
    def __str__(self):
        return f'Surname: {self.surname}'
mentor = Mentor('Jobs')
print(mentor)


class Reviewer(Mentor): # Класс Reviewer - дочерний класс
    def __init__(self, name, surname):
        super().__init__(self, name, surname)
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lector(Mentor): # Класс Lector - дочерний класс
    def __init__(self, name, surname):
        super().__init__(self, name, surname)
        self.name = name
        self.surname = surname
        self.courses_attached = []

# Задание № 2 - Атрибуты и взаимодействие классов. 
## Reviewer оценивает студента:
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def __str__(self): # метод не работает
        return f'Имя: {self.name} and Фамилия: {self.surname}'
    
        
class Reviewer:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f'Имя: {self.name} and Фамилия: {self.surname}'
       
best_student = Student('Имя: Ruoy', 'Фамилия: Eman', 'your_gender')
best_student.finished_courses += ['Git']
best_student.courses_in_progress += ['Python']
best_student.grades['Git'] = [10, 10, 10, 10, 10]
best_student.grades['Python'] = [10, 10]

print(best_student.name) 
print(best_student.surname)
print(best_student.finished_courses)
print(best_student.courses_in_progress)
print(best_student.grades)

 
cool_reviewer = Reviewer('Some', 'Buddy') # Проверяющий
cool_reviewer.courses_attached += ['Python']
print(cool_reviewer.courses_attached)
print(cool_reviewer.name)
print(cool_reviewer.surname)
class Reviewer:
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return f'Name: {self.name}'

reviewer = Reviewer('Some')
print(reviewer)
class Reviewer: 
    def __init__(self, surname):
        self.surname = surname
        
    def __str__(self):
        return f'Surname: {self.surname}'

reviewer= Reviewer('Buddy')
print(reviewer)
   
  
### Студент оценивает лектора:

class Lector: # Класс Lector, который проверяется студентами
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

 
        
class Student_evaluator:# Класс Student_evaluator, который проверяет лектора
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


best_Lector = Lector('Elon', 'Musk', 'your_gender')
best_Lector.finished_courses += ['Git']
best_Lector.courses_in_progress += ['Python']
best_Lector.grades['Git'] = [10, 10, 10, 10, 10]
best_Lector.grades['Python'] = [10, 10]
 
print(best_Lector.finished_courses)
print(best_Lector.courses_in_progress)
print(best_Lector.grades)
print(best_Lector.name)
print(best_Lector.surname)
 
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
 
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
 
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.finished_courses += ['Git']
best_student.courses_in_progress += ['Python']
best_student.grades['Git'] = [10, 10, 10, 10, 10]
best_student.grades['Python'] = [10, 10]

average = sum(best_student.grades['Git']) / len(best_student.grades['Git']) # Задача 4 (вычисление средней оценки по курсу Git) 
print(average)
average = sum(best_student.grades['Python']) / len(best_student.grades['Python']) # Задача 4 (вычисление средней оценкипо курсу Python) 
print(average)

print(best_student.finished_courses)
print(best_student.courses_in_progress)
print(best_student.grades)
 
cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
print(cool_mentor.courses_attached)

class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
    def __str__(self):
        return f'Name: {self.name}, Surname: {self.surname}'

student = Student('Ruoy', 'Eman')
print(student)

class Student:
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return f'Name: {self.name}'

student = Student('Ruoy')
print(student)
class Student: 
    def __init__(self, surname):
        self.surname = surname
        
    def __str__(self):
        return f'Surname: {self.surname}'

student = Student('Eman')
print(student)
class Student: 
    def __init__(self, grades):
        self.grades = grades
        
    def __str__(self):
        return f'Средняя оценка за домашние задания: {self.grades}'

student = Student('10')
print(student)
class Student: 
    def __init__(self, courses_in_progress):
        self.courses_in_progress = courses_in_progress
        
    def __str__(self):
        return f'Курсы в процессе изучения: {self.courses_in_progress}'

student = Student('Python, Git')
print(student)
class Student: 
    def __init__(self, finished_courses):
        self.finished_courses = finished_courses
        
    def __str__(self):
        return f'Завершенные курсы: {self.finished_courses}'

student = Student('Введение в программирование')
print(student)

# Методы сравнения (Сравниваем оценки студентов)

Student1_grade = 5
Student2_grade = 7
Student3_grade = 10

# Проверяем, меньше ли Student1_grade и Student2_grade, чем Student1_grade3
print(Student1_grade < Student2_grade < Student3_grade) 

# Проверяем, равны ли все оценки
print(Student1_grade == Student2_grade == Student3_grade)

# Проверяем, больше ли Student2_grade чем Student1_grade
print(Student1_grade < Student2_grade) 

# Проверяем, больше ли Student2_grade чем Student3_grade
print(Student2_grade > Student3_grade) 
