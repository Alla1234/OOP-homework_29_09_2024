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


class Reviewer(Mentor): # Класс Reviewer - дочерний класс, передаем ему функции проверки от класса Mentor
    def __init__(self, name, surname):
        super().__init__(self, name, surname)
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
# Задание № 2 - Атрибуты и взаимодействие классов. 

class Lector(Mentor): # Класс Lector - дочерний класс - совет АСПИРАНТА по доработке!!!!!
    def __init__(self, name, surname, grades):
        super().__init__(self, name, surname, grades)
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {} # совет аспиранта по доработке!!!!!!Вот пример self.grades = {‘Python’:[9, 7, 10, 3, 10, 10], ‘Java’: [10,10,9]}
# Для того, чтобы заполнить эти списки с оценками, надо использовать метод, в который надо передать объект Студент( который будет оценивать), название курса и оценку.
#  В самом методе сначала надо проверить есть ли курс у самого студента( т к оценивать могут только студены этого курса) а потом в словарь self.grades
# записать дополнительную оценку в список оценок по ключу - название курса. self.grades[course] = [grade]. 
# Вернусь немного назад, для того чтобы запомнить в классе какие курсы использует студент , надо создать еще один атрибут, допустим, self.courses_in_progress,
# который должен являться списком из этих курсов
        self.courses_in_progress = []


## Reviewer оценивает студента:
class Student:
    def __init__(self, name, surname, gender, courses_in_progress, grades):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def __str__(self): # магический метод
        return f'Имя: {self.name} and Фамилия: {self.surname}'

        
class Reviewer:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f'Имя: {self.name} and Фамилия: {self.surname}'
       
student1 = Student('Имя: Ruoy', 'Фамилия: Eman', 'your_gender', 'courses_in_progress', 'grades')
student1.finished_courses += ['Git']
student1.courses_in_progress += ['Python']
student1.grades['Git'] = [10, 9, 10, 7, 10]
student1.grades['Python'] = [10, 9]

print(student1.name) 
print(student1.surname)
print(student1.finished_courses)
print(student1.courses_in_progress)
print(student1.grades)
# print(grades)

 
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
    def __init__(self, name, surname, courses_attached, courses_in_progress,):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.courses_in_progress = []
        


best_Lector = Lector('Elon', 'Musk', 'your_gender')
best_Lector.finished_courses += ['Git']
best_Lector.courses_in_progress += ['Python']
best_Lector.grades['Git'] = [9, 7, 10, 3, 10]
best_Lector.grades['Python'] = [10, 10, 9]
 
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
best_student.grades['Git'] = [9, 7, 10, 10, 10, 10]
best_student.grades['Python'] = [10, 10, 9]

average1 = sum(best_student.grades['Git']) / len(best_student.grades['Git']) # Задача 4 (вычисление средней оценки по курсу Git) 
print(average1)
average2 = sum(best_student.grades['Python']) / len(best_student.grades['Python']) # Задача 4 (вычисление средней оценки по курсу Python) 
print(average2)

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
    def __str__(self):
        return f'Средняя оценка за домашние задания Git: {average1}'
    def __str__(self):
        return f'Средняя оценка за домашние задания Python: {average2}'
        

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
