# =======================================================================================================================

# 1) Створіть клас Студент, в ньому обявіть дві змінні імя де збережети імя студента, та список його оцінок.
# створіть два метода в цьому класі,
# перший метод який буде вітатись і при вітання використовувати імя студента.
# другий метод буде виводити оцінки. Методи виводять результат через прінти.
#
# Створіть два екземпляра цього класу, в другому екземплярі змніть імя на своє(не міняючи нічого в класі).
# Вивідіть дві функції цих екземплярів,
# що б кожен студент привітався та сказав свої оцінки.


class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def greeting(self):
        print(f"Привіт, я {self.name}!")

    def student_grades(self):
        print(f"Мої оцінки {self.grades} \n")


student1 = Student(name="Олександр", grades=[12, 10, 11, 10])
student2 = Student(name="Федот", grades=[7, 8, 5, 3])

student1.greeting()
student1.student_grades()

student2.greeting()
student2.student_grades()
