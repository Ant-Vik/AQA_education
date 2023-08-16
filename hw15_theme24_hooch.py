"""
Task 1

Напишіть функцію, яка приймає строку як аргумент і повертає рядок з його символами у зворотному порядку.
"""

# def revers_sting():
#     revers_text = ''.join(reversed(enter_str))
#     return revers_text
#
#
# enter_str = input('Введіть значення:  ')
# print(revers_sting())


'''
Task 2

Напишіть функцію, яка приймає список і елемент, а потім повертає кількість входжень цього елемента у списку.
'''


# def num_occurrences_element():
#     if element in lst:
#         count_list = lst.count(element)
#         if count_list == 1:
#             print(f'Список містить {count_list} елемент {element}')
#         elif 1 < count_list <= 4:
#             print(f'Список містить {count_list} елементи {element}')
#         else:
#             print(f'Список містить {count_list} елементів {element}')
#     else:
#         print(f'Список не містить елемента {element}')
#
#
# lst = input('Введіть значення:  ')
# element = input('Введіть значення:  ')
# num_occurrences_element()

'''
Task 3. 

Напишіть функцію, яка отримує інформацію про двох людей (ім’я, вік, стать). 
А далі напишіть одну чи дві функції (як забажаєте), яка порівнює вік цих людей, і вивести результат порівнянь.
'''

"Це перший варіант вирішення завдання"

# users_list = dict()
#
#
# def get_persons_info():
#     """Повертає словник з даними про людину"""
#
#     name = input("Введіть ім'я:  ")
#     age = int(input("Введіть вік:  "))
#     gender = input("Введіть стать:  ")
#
#     person = dict(
#         name=name,
#         age=age,
#         gender=gender
#     )
#
#     return person
#
#
# def find_older_person():
#     """Додає кожну нову людину у словник та визначає найстаршу з них"""
#
#     for person_id in range(2):
#         users_list[person_id + 1] = get_persons_info()
#
#     print(users_list)  # Залишив прінт для наочності що словник заповнюється
#     if users_list[1]['age'] > users_list[2]['age']:
#         print(f'{users_list[1]["name"]} та {users_list[2]["name"]} перша людина старша.')
#     elif users_list[1]['age'] < users_list[2]['age']:
#         print(f'{users_list[1]["name"]} та {users_list[2]["name"]} друга людина старша.')
#     else:
#         print(f'{users_list[1]["name"]} та {users_list[2]["name"]} люди однакового віку.')
#
#
# find_older_person()


'''Це другий варіант вирішення завдання'''

# users_list = dict()
# users_list_file = 'users_file.txt'
#
#
# def get_persons_info():
#     """Повертає словник з даними про людину"""
#
#     name = input("Введіть ім'я:  ")
#     age = int(input("Введіть вік:  "))
#     gender = input("Введіть стать:  ")
#
#     person = dict(
#         name=name,
#         age=age,
#         gender=gender
#     )
#     return person
#
#
# def find_older_person():
#     """Другий варіант який додає кожну нову людину у словник та визначає найстаршу з них"""
#
#     for person_id in range(2):
#         users_list[person_id + 1] = get_persons_info()
#
#     older_person = max(users_list.values(), key=lambda x: x['age'])
#     younger_person = min(users_list.values(), key=lambda x: x['age'])
#     print(f'{younger_person["name"]} та {older_person["name"]} друга людина старша.')
#
#     return users_list
#
#
# '''Додав ще одну функцію з додаванням людей у файл, в завданні цього немає просто мені здалось це якимсь логічним
# завершенням тому і додов'''
#
#
# def write_to_file():
#     """Створення та запис користувачів у файл"""
#     with open(users_list_file, 'w') as file:
#         users_info = find_older_person()
#         context = '\n'.join(str(person) for person in users_info.items())  # Для запису кожної людини з нового радка
#         context_del_brackets = context.translate(str.maketrans('', '', '(){}\''))  # Щоб прибрати зайві символи
#         file.write(context_del_brackets)
#
#
# write_to_file()
