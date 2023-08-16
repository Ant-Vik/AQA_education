# Homework 4:

# Задача 1

# num = int(input('Введите год:  '))
#
# if not num % 4 and num % 100:
#     print("Yes")
# elif num == 0:
#     print("Год некорректен")
# else:
#     print('not yes')


# Задача 2
#
# x1 = int(input('Введите число 1:  '))
# y1 = int(input('Введите число 2:  '))
# x2 = int(input('Введите число 3:  '))
# y2 = int(input('Введите число 4:  '))
#
# if 0 < x1 < 9 and 0 < y1 < 9 and (x1 == x2 or y1 == y2) and x1 + x2 != y1 + y2:
#     print('yes')
# else:
#     print('no')

    # Второй способ решения, в этом способе я взял за основу что мы знаем расположение ладьи
    # и нам нужно сделать ход только на одну клетку в первом способе я указал диапазон от 1 до 8


# x = int(input('Введите число 1:  '))
# y = int(input('Введите число 2:  '))
# c = int(input('Введите число 3:  '))
# b = int(input('Введите число 4:  '))
#
# if x == y and c == b:
#     print('no')
# elif 4 == x or 6 and y == 4 and c == 4 and 4 == b or 5:
#     print('yes')
# elif x == 5 and 3 == y or 5 and 3 == c or 5 and 4 == b or 5:
#     print('yes')
# else:
#     print('no')


# Homework 5:


# Задача 1

# x = int(input('Введите число 1:  '))
#
# if x == 4 or x == 6 or x == 9 or x == 11:
#     print(30)
# elif x == 2:
#     print(28)
# else:
#     print(31)


# Задача 2

# color1 = input('Введите первый цвет:  ')
# color2 = input('Введите второй цвет:  ')
#
# if (color1 == 'красный' or color2 == 'красный') and (color2 == 'синий' or color1 == 'синий'):
#     print('фиолетовый')
# elif (color1 == 'красный' or color2 == 'красный') and (color2 == 'желтый' or color1 == 'желтый'):
#     print('оранжевый')
# elif (color1 == 'синий' or color2 == 'синий') and (color2 == 'желтый' or color1 == 'желтый'):
#     print('зеленый')
# elif (color1 != 'красный' and color1 != 'синий' and color1 != 'желтый') or (color2 != 'красный' and color2 != 'синий' and color2 != 'желтый'):
#     print('неправильный цвет')
# elif color1 == color2:
#     print(color1)



# Задача 3

# num = int(input('Введите число:  '))
#
# m1 = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
# m2 = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
#
# if num in m1:
#     print('Красный')
# elif num in m2:
#     print('Черный')
# elif num == 0:
#     print('Зеленый')
# else:
#     print('Ошибка ввода')



    # В этой задаче также два варианта первый написал при помощи массива мне показался самым просты вариантом.
    # Второй через остаток от деления но этот способ оч замороченый и сложный как по мне

# num = int(input('Введите число:  '))
#
# if num % 2 == 0 and 0 < num < 11:
#     print('Черный')
# elif num % 2 != 0 and 10 < num < 19:
#     print('Черный')
# elif num % 2 == 0 and 18 < num < 29:
#     print('Черный')
# elif num % 2 != 0 and 28 < num < 37:
#     print('Черный')
# elif num == 0:
#     print('Зеленый')
# elif num > 36 or num < 0:
#     print('Ошибка ввода')
# else:
#     print('Красный')