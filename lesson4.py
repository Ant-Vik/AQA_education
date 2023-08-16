import math

# n1 = int(input("ведите число:  "))
# n2 = int(input('ведите число:  '))
# n3 = int(input('ведите число:  '))
#
# if n3 <= n2 <= n1:
#     print(n1, n2, n3, sep='\n')
# elif n3 <= n1 <= n2:
#     print(n2, n1, n3,  sep='\n')
# elif n1 <= n2 <= n3:
#     print(n3, n2, n1,  sep='\n')
# elif n2 <= n1 <= n3:
#     print(n3, n1, n2,  sep='\n')
# elif n3 <= n3 <= n1:
#     print(n1, n3, n2,  sep='\n')
# elif n1 == n3 == n2:
#     print(n3, n2, n1,  sep='\n')

#
# n1 = input("ведите название:  ")
# n2 = input('ведите название:  ')
# n3 = input('ведите название:  ')
#
# if len(n1) > len(n2) > len(n3):
#     print(n1, n3, sep='\n')
# elif len(n2) > len(n1) > len(n3):
#     print(n2, n3, sep='\n')
# elif len(n2) > len(n3) > len(n1):
#     print(n2, n1, sep='\n')
# elif len(n1) < len(n2) < len(n3):
#     print(n3, n1, sep='\n')
# elif len(n1) == len(n2) != len(n3):
#     print(n3, n1, sep='\n')
# elif len(n1) != len(n2) == len(n3):
#     print(n3, n1, sep='\n')
# elif len(n2) != len(n1) == len(n3):
#     print(n2, n1, sep='\n')
# elif len(n2) == len(n1) == len(n3):
#     print('Все равны', n1, n2, n3, sep='\n')










# a = float(input('enter  '))
# b = float(input('enter  '))
# s = 0.5 * a * b
# print(s)


# a = float(input('enter  '))
# if a == 0:
#     print('no')
# else:
#     ob = 1 / a # a ** -1
#     print(ob)

# print(max(1, 3, -5, 6, 10))
# print(min(1, 3, -5, 6, 10))
#


# #len() считает только строки
# s1 = 'test'
# lenght1 = len(s1)
# lenght2 = len('test test')
#

# s = input('test ')
#
# if len(s) == 1 and s in 'aeiou': # совпадение из одного символа если указать 2 то совпадение из двух символов и.т.д.
#     print('yes')


# name = input('Имя ')
# # name1 = len(name)
# print(f'my name {name} has lenght {len(name)}')

# a = input('enter ')
# if 'желтый' in a:
#     print('yes')
# else:
#     print('no')


# модуль математических обчислений нужно импортировать
# num1 = math.sqrt(2)
# num2 = math.ceil(3.8)
# nam3 = math.floor(3.8)


# a = float(input('ввод'))
# s = pow(a, 2) # первый вариант
# s1 = 2 * math.pi * a # второй вариант
# print(s1)


# for i in range(5):
#     num = int(input())
#     print('квадрат числа', num * num)
# print('закончен')


# for i in range(5):
#     print(i, '---привет')


# for i in range(5):
#     print(i +1, '---привет')


# for _ in range(5):  # Если не нужна переменная можно указать нижнее подчеркивание
#     print('---привет')


# for i in range(3):
#     a = 'python - rocks'
#     print(i, a)



# for i in range(3):
#     n = int(input())
#     print('квадрат числа', n * n)


# n = int(input())
# for i in range(n+1):
#     print(f'квадрат числа {i} равно {i*i}')




# for i in range(100, 1000):
#     if i % 10 == 7:
#         print(i)


# m = int(input())
# n = int(input())
#
# for i in range(m, n+1):
#     print(i)




# m = int(input('m  '))
# n = int(input('n  '))
#
# if m < n:
#     for i in range(m, n +1):
#         print(i)
# elif m > n:
#     for i in range(m, n-1, -1):
#         print(i)
# else:
#     print('числа равны')
