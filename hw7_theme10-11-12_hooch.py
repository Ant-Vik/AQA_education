import math

'''
                                        Homework 10
'''

'''
Task 1

На вхід подається натуральне число. Напишіть програму, яка змінює порядок поданих цифр числа на зворотний.
'''

# num = int(input('Введіть число:  '))
#
# while num != 0:
#     inverse = num % 10
#     num //= 10
#     print(inverse, end='')


'''
Task 2

Дано натуральне число. Напишіть програму, яка обчислює:

суму його цифр;
кількість цифр у ньому;
добуток його цифр;
середнє арифметичне його цифр;
його першу цифру;
суму його першої та останньої цифри
'''

# num = int(input('Введіть число:  '))
# sum_dig = 0
# total_dig = 0
# prod_num = 1
# arithmetic_num = 0
# first_dig = 0
# last_dig = num % 10
# first_last = 0
#
# while num != 0:
#     total_count = num % 10
#     sum_dig += total_count
#     prod_num *= total_count
#     total_dig += 1
#     arithmetic_num = sum_dig / total_dig
#     first_dig = num
#     first_last = num % 10 + last_dig
#     num = num // 10
#
# print(sum_dig, total_dig, prod_num, arithmetic_num, first_dig, first_last, sep='\n')


'''
Task 3
 Дано натуральне число n,(n≥10). Напишіть програму, яка визначає його максимальну та мінімальну цифри.
'''

# num = int(input('Введіть число:  '))
# total_max = 0
# total_min = 10
#
# while num >= 10:
#     count = num % 10
#     if count >= total_max:
#         total_max = count
#     if count <= total_min:
#         total_min = count
#     num = num // 10
#
# while num != total_max:
#     if total_max <= num:
#         total_max = num
#     if num <= total_min:
#         total_min = num
#     num = num // 10
#     break
#
# print('Максимальна цифра', total_max)
# print('Мінімальна цифра', total_min)


'''
Task 4

Дано натуральне число. Напишіть програму, яка визначає, чи складаєтсья число із однакових цифр.
'''

# num = int(input('Введіть число:  '))
# boo = True
# total = 0
# last = num % 10
#
# if last != 0:
#     total = last
#
# while num != 0:
#     last_digit = num % 10
#     if total != last_digit:
#         boo = False
#         break
#     elif total == last_digit:
#         boo = True
#         total = last_digit
#     num //= 10
#
# if total == 0:
#     print('NO')
# elif boo == True:
#     print('Yes')
# else:
#     print('No')


# num = int(input('Введіть число:  '))
# boo = False
# total = 0
# last = num % 10
#
# if last != 0:
#     total = last
#
# for i in range(1, num + 1):
#     last_digit = num % 10
#     if num == 0:
#         continue
#     if total != last_digit:
#         boo = False
#         break
#     elif total == last_digit:
#         boo = True
#         total = last_digit
#     num //= 10
# # if total == 0:
# #     print('NO')
# if boo == True:
#     print('Yes')
# else:
#     print('No')


'''
                                            Homework 11
'''

'''
Task 1.

На вхід до програми подається число n > 1. Напишіть програму, яка виводить його найменший відмінний від 1 дільник. 
Використовуйте оператор break, коли знайшли дільник.
'''

# n = int(input('Введіть число:  '))
# flag = True
# for i in range(2, n + 1):
#     if n % i == 0:
#         flag = True
#         break
#
# if flag == True:
#     print(i)


'''
Task 2.
На вхід до програми подається натуральне число n. Напишіть програму, яка виводить числа від 1 до n включно, за винятком:

- чисел від 5 до 9 включно;
- чисел від 17 до 37 включно;
- чисел від 78 до 87 включно.
'''

# n = int(input('Введіть число:  '))
#
# for i in range(1, n + 1):
#     if 5 <= i <= 9 or 17 <= i <= 37 or 78 <= i <= 87:
#         continue
#     print(i)


'''
                                            Homework 12
'''

'''
4. Дано натуральне число n (n<=9). Напишіть програму, яка зчитує таблицю розміром   n x 3 і складається із даного числа.
'''

# n = int(input('Введіть число:  '))
#
# if n <= 9:
#     for i in range(n):
#         for j in range(3):
#             print(n, end=' ')
#         print()
# else:
#     print('Не вірно введене число')


'''
5. Дано натуральне число n (n <= 9). Напишіть програму, яка виводить таблицю додавання для всіх чисел від 1 до n.
'''

# n = int(input('Введіть число:  '))
#
# if n <= 9:
#     for i in range(1, n + 1):
#         for j in range(1, n + 1):
#             total = i + j
#             print(f'{i} + {j} = {total}')
# else:
#     print('Не вірно введене число')





'''Задачки с презентации 12 записал здесь чтобы не создавать новый файл'''

# for hourse in range(24):
#     for minutes in range(60):
#         for seconds in range(60):
#             print(hourse, ':', minutes, ':', seconds)
# h = hourse * minutes * seconds
# print(h)


# for i in range(8):
#     for j in range(6):
#         print('*', end=' ')
#     print()


# for i in range(8):
#     for j in range(i +1):
#         print('*', end=' ')
#     print()

# for i in range(1, 4):
#     for j in range(3, 6):
#         print(i, j)

# for i in range(1, 4):
#     for j in range(3, 5):
#         print(i + j, end='')

# counter = 0
# for i in range(99, 102):
#     temp = i
#     while temp > 0:
#         counter += 1
#         temp //= 10
#         print(temp)
# print(counter)
