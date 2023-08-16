import math

# ДЗ 6:

# Задача 1

# n = int(input('ведите возраст:  '))
# x = 10.5
# y = 4
# if 0 < n <= 2:
#     print(n * x)
# elif n > 2:
#     print(2 * x + (n - 2) * y)
# else:
#     print('Ошибка ввода')


# Задача 2

# a = float(input())
# print(a % 1)


# Задача 3

# n1 = int(input("ведите число:  "))
# n2 = int(input('ведите число:  '))
# n3 = int(input('ведите число:  '))
#
# print(max(n1, n2, n3))
# print(n1 + n2 + n3 - max(n1, n2, n3) - min(n1, n2, n3))
# print(min(n1, n2, n3))

# Задача 4

# n1 = input("ведите название города:  ")
# n2 = input('ведите название города:  ')
# n3 = input('ведите название города:  ')
#
# print(min(n1, n2, n3))
# print(max(n1, n2, n3))


# if n2 < n1 > n3:
#     print(min(n2, n3))
#     print(n1)
# elif n1 < n2 > n3:
#     print(min(n1, n3))
#     print(n2)
# elif n2 < n3 > n1:
#     print(min(n1, n2))
#     print(n3)
# elif n2 == n1 > n3:
#     print(n3, n2)
# elif n2 == n3 > n1:
#     print(n1, n2)
# elif n3 == n1 > n2:
#     print(n3, n2)

# print(max(n1, n2, n3))


# Задача 5

# n1 = input("ведите почту:  ")
#
# if "@" in n1 and "." in n1:
#     print('Yes')
# else:
#     print('No')


# Задача 6

# n = int(input("ведите число:  "))
# a = int(input("ведите число:  "))
#
# print((n * a ** 2) / (4 * math.tan(math.pi / n)))


# ДЗ 7:

# Задание 1

# for i in range(6):
#     print("AAA")
# for j in range(5):
#     print("BBBB")
# print("E")
# for k in range(9):
#     print("TTTTT")
# print("G")


# Задание 2

# m = int(input("ведите число:  "))
# n = int(input("ведите число:  "))
#
# if m % 2 == 0:
#     for i in range(m - 1, n - 1, -2):
#         print(i)
# elif m % 2 != 0:
#     for i in range(m, n - 1, -2):
#         print(i)

# Задание 3

'''Эту задачу решить не получается подскажи пожалуйста правильное ли я выбрал направление решения задачи
 и чего не хватает для ее правильного решения'''

# m = int(input("ведите название:  "))
# n = int(input("ведите название:  "))
#
# if m == n:
#     print(n)
# if m < n:
#     for i in range(m, n+1):
#         if i % 17 == 0 or i % 10 == 9 or i % 3 == 0 and i % 5 == 0:
#             print(i)


# Задание 4

# n = int(input("ведите число:  "))
#
# for i in range(1, 10+1):
#     print(f'{i} x {n}= {i * n}')










# if len(a) > len(b) > len(c):
#     print(a, c, sep='\n')
# elif len(a) > len(c) > len(b):
#     print(a, b, sep='\n')
# elif len(a) < len(b) < len(c):
#     print(a, c, sep='\n')
# elif len(a) > len(c) < len(b):
#     print(c, a, sep='\n')
# elif len(b) < len(a) < len(c):
#     print(b, c, sep='\n')


a = input('Enter 1st string: ')
b = input('Enter 2nd string: ')
c = input('Enter 3d string: ')

a_len = len(a)
b_len = len(b)
c_len = len(c)

longest = max(a_len, b_len, c_len)
shortest = min(a_len, b_len, c_len)

if a_len == shortest:
    print('Shortest word: ' + a)
elif b_len == shortest:
    print('Shortest word: ' + b)
elif c_len == shortest:
    print('Shortest word: ' + c)

if a_len == longest:
    print('Longest word: ' + a)
elif b_len == longest:
    print('Longest word: ' + b)
elif c_len == longest:
    print('Longest word: ' + c)


