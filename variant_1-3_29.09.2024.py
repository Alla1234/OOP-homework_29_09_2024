# Задание № 1 : Наследование
class Mentor: # Класс Mentor - родительский класс
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
mentor = Mentor("Stewe","Jobs")
    

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
        return f"Имя: {self.name} and Фамилия: {self.surname}"
    
        
class Reviewer:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f"Имя: {self.name} and Фамилия: {self.surname}"
       
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

 
cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
print(cool_reviewer.courses_attached)
print(cool_reviewer.name)
print(cool_reviewer.surname)

   
  
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
 
print(best_student.finished_courses)
print(best_student.courses_in_progress)
print(best_student.grades)
 
cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
print(cool_mentor.courses_attached)

# Нахождение средней оценки
