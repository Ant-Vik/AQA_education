

# Робота з числами
# Задача 1

# a = int(input('Введите первое число '))
# b = int(input('Введите второе число '))
# f = 2 * (a + b) ** 3 + 25 * b ** 2 - 68 * a - 25
#
# print(f)



# Задача 2

# a = int(input("Введите число  " ))
#
# print(f'Наступне за числом {a} число: {a + 1}')
# print(f'Попереднє перед числом {a} число: {a - 1}')



# Задача 3

# a = int(input("Введите первое число  " ))
# b = int(input("Введите второе число  " ))
# c = int(input("Введите третье число  " ))
# s = 4
#
# print(f'{a}',f'{b}',f'{c}', f'{(a+b+c) * s}', sep='\n')


# Задача 4

# a = int(input('Введите первое число '))
# b = int(input('Введите второе число '))
#
# print(f'{a} + {b} = {a+b} ', f'{a} - {b} = {a-b} ', f'{a} * {b} = {a*b} ', sep='\n')








# Умовний оператор if/else
# Задача 1


a = int(input('Укажите свой возраст '))

# if a <= 16:
#     print('Юность')
# elif a >= 17 and a <= 35:
#     print('Молодость')
# elif a >= 36 and a <= 59:
#     print('Зрелость')
# else:
#     print('Старость')



# if a <= 16:
#     print('Юность')
# elif 17 <= a <= 35:
#     print('Молодость')
# elif 36 <= a <= 59:
#     print('Зрелость')
# else:
#     print('Старость')





# Задача 2


# a = int(input('Введите первую цифру '))
# b = int(input('Введите вторую цифру '))
# c = int(input('Введите третью цифру '))
# x = 0
# y = 0
# z = 0
#
# if a <= 0:
#     x = a
# elif b <= 0:
#     y = b
# elif c <= 0:
#     z = c
# else:
#     print(f'{a+b+c}')

# elif a <= 0 and b <= 0 and c > 0:
#     print(f'{c}')
# elif a <= 0 and b > 0 and c <= 0:
#     print(f'{b}')
# elif a > 0 and b <= 0 and c <= 0:
#     print(f'{a}')

# a = int(input('Введите первую цифру '))
# b = int(input('Введите вторую цифру '))
# c = int(input('Введите третью цифру '))
# d = 0
#
# if a >= 0 and b >= 0 and c >= 0:
#     print(f'{a + b + c}')
# elif a >= 0 and b >= 0:
#     print(f'{a + b}')
# elif a >= 0 and c >= 0:
#     print(f'{a + c}')
# elif b >= 0 and c >= 0:
#     print(f'{b + c}')
# elif a <= 0 and b <= 0 and c > 0:
#     print(f'{c}')
# elif a <= 0 and b > 0 and c <= 0:
#     print(f'{b}')
# elif a > 0 and b <= 0 and c <= 0:
#     print(f'{a}')
# else:
#     print(d)














# elif a <= 0 and b <= 0 and c <= 0:   Можно и так просто через else короче
#     print(f'{d}')





#  Задача 3


# num1 = int(input('Введите первую цифру  '))
# num2 = int(input('Введите вторую цифру  '))
# num3 = int(input('Введите третью цифру  '))
# num4 = int(input('Введите третью цифру  '))
#
#
# if num1 < num2:
#     a = num1
# else:
#     a = num2
# if num3 < num4:
#     b = num3
# else:
#     b = num4
# if a < b:
#     print(a)
# else:
#     print(b)

