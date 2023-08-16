
#
# n = int(input('ввод числа'))
#
#
# print(n + 1, n + 2, n + 3, sep='\n')


# a = int(input('ввод числ'))
# # v = a ** 3
# # s = 6 * a ** 2
#
# print(f'{a ** 3}', f'{6*a**2}')



# answer = input('Ввести пароль')
# answer2 = input('Ввести пароль2')
# if  answer == answer2:
#     print('Пароли совпадают')
# else:
#     print('Пароли не совпадают')



# answer = int(input('Ввести число'))
# if  answer % 2 == 0:
#     print('Число парное')
# else:
#     print('Число не парное')

#
# num1 = int(input('Ввести число 1'))
# num2 = int(input('Ввести число 2'))
# num3 = int(input('Ввести число 3'))
# num4 = int(input('Ввести число 4'))
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
#













a = int(input("Число  "))
operator = input('введите знак  ')
b = int(input("Число  "))
result = 0

if  operator == '+':
    result = a + b
elif operator == '-':
    result = a - b
elif  operator == '/':
    result = a / b
elif  operator == '*':
    result = a * b
elif  operator == '%':
    result = a % b
elif operator == '**':
    result = a ** b
print(f'{a} {operator} {b} = {result}')















