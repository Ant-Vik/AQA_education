'''
Task 1. Створіть базовий клас Employee, у якому є атрибути name, salary, bonus. Потім створіть підклас “Info”,
який наслідується від класу Employee і має свої методи: def salary_details - повертає нам інформацію, що name має
запрлатню salary + бонус у розмірі bonus. def total_salary - метод, що повертає повідомлення: Загальний прибуток у
місяць працівника name дорівнює(salary+bonus)

Після створення класу та підкласу створити об’єкт, та вивести на екран його salary_details та total_salary.
Приклад виведення:
Ihor має зарплатню 1000 + бонус у розмірі: 100
Загальний прибуток у місяць працівника Ihor дорівнює: 1100
'''


# class Employee:
#
#     def __init__(self, name, salary, bonus):
#         self.name = name
#         self.salary = salary
#         self.bonus = bonus
#
#
# class Info(Employee):
#     def salary_details(self):
#         return f'{self.name} має зарплатню {self.salary} + бонус у розмірі: {self.bonus}'
#
#     def total_salary(self):
#         salary_and_bonus = self.salary + self.bonus
#         return f'Загальний прибуток у місяць працівника {self.name} дорівнює: {salary_and_bonus}'
#
#
# employee_info = Info('Tom', 1000, 200)
# print(employee_info.salary_details())
# print(employee_info.total_salary())
