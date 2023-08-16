'''
                                Homework23								Робота з файлами
'''

'''
Task 1.

Написати програму, що створює текстовий файл і поміщає в нього текст:
Після чого, провести заміну у цьому текстовому файлі слово “Walk” на слово “RIDE”.
'''

# text = "When you walk through a storm Hold your head up high And don't be afraid of the dark At the end of a storm" \
#        " There's a golden sky And the sweet silver song of a lark Walk on through the wind Walk on through the rain" \
#        " For your dreams be tossed and blown Walk on, walk on With hope in your heart And you'll never walk alone"
# c_file = 'content_file.txt'
#
# with open(c_file, 'w') as file:  # Создание и добавление в файл исходный текст
#     new_file = file.write(text)
#
# with open(c_file, 'r') as file:  # Замена ключевого слова
#     content = file.read()
#     print(content)  # Оставил просто для наглядности, что файл создан с исходным текстом
#     new_content = content.replace('Walk', 'RIDE')
#
# with open(c_file, 'w') as file:  # Пересоздание файла с измененным ключевым словом
#     new_file2 = file.write(new_content)

'''
Task 2.

Написати програму, що створює текстовий файл, в який записуються речення, що вводяться з клавіатури, 
допоки користувач не введе число 0. Число нуль зупинить довільний ввід тексту. Після того, коли програма створить 
файл і запише довільний текст, вивести повідомлення: Дані були успішно записані у файл “file_name”
'''

# t_file = 'text_file.txt'
#
# with open(t_file, 'w') as file:
#     while True:
#         text = input('Введіть текст:  ')
#         if '0' in text:
#             break
#         context = file.write(text + '\n')
# print(f'Дані були успішно записані у файл {t_file}')


'''
Task 3

Написати програму, що створює новий файл, в який ми додаємо всі парні числа в діапазоні від 0 до введеного з 
клавіатури числа включно, які більше за 18 і є парними. Після завершення програма вивести повідомлення: Парні числа 
більше за 18 були успішно записані у файл “file_name.txt”. При кожному запуску програми, нові числа додаються у 
кінець файла “file_name.txt”
'''

# num_file = 'number_file.txt'
# enter = int(input('Введіть число більше за 18'))
# flag = True  # Создал flag для покрытия кейса с введением числа меньше 18
#
# with open(num_file, 'a') as file:
#     for i in range(0, enter + 1, 2):
#         if i > 18:
#             flag = True
#             transform = str(i)
#             file.write(transform + ', ')
#         elif enter < 18:
#             flag = False
#             break
#
# if flag:
#     print(f'Парні числа більше за 18 були успішно записані у файл {num_file}')
# else:
#     print('Введене число меньше за 18')
