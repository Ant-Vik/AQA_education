import math

"""
Task 1
На вхід до програми подається натуральне число n. Напишіть програму, яка обчислює значення виразу:
"""
# n1 = 0
# n = int(input())
# for i in range(1, n + 1):
#     n1 += (1 / i)
# print(n1 - math.log(n))

"""
Task 2
На вхід до програми подається натуральне число n. Напишіть програму, яка підраховує суму тих чисел від 1 до n (включно), квадрат яких закінчується на 2,5 або 8.
"""

# n = int(input())
# total = 0
#
# for i in range(1, n + 1):
#     if i ** 2 % 10 == 2 or i ** 2 % 10 == 5 or i ** 2 % 10 == 8:
#         total = total + i
# print(total)


"""

Task 3

На вхід до програми подається натуральне число n. Напишіть програму, яка обчислює суму всіх дільників.
(приклад число 10. Сума всіх дільників буде дорівнювати 18. Тому що число 10 ділиться на 1, на 2, на 5, на 10. І їх сума буде 1 + 2 + 5 + 10 = 18)

"""

# n = int(input())
# total = 0
#
# for i in range(1, n + 1):
#     if n % i == 0:
#         total = total + i
# print(total)


"""
Task 4

Напишіть програму, яка рахує, скільки разів кількість прожитих років поміститься у столітті. 
На вхід програмі подається вік. Програма має вивести кількість таких проміжків життя у одному столітті.
"""

# n = int(input())
# total = 100 // n
# print(total)


"""
Task 5

Напишіть програму, відповідає на питання, чи можна людині отримувати водійське посвідчення, відповідно її  віку.
Якщо людині менше 18, вивести на екран “залишилось почекати (розрахунок скільки)  днів!”
Якщо рівно 18 років, вивести на екран “Вітаю, дозволено!”
Якщо людина старше 18, вивести на екран “Дозволено вже (розрахунок скільки) років”

"""

# n = int(input("Солько Вам лет?  "))
# year = 365
# if 0 < n < 18:
#     m = (18 - n) * year
#     print(f'Осталось подождать {m} дней!')
# elif n > 18:
#     m = n - 18
#     print(f"Разрешено уже {m} лет!")
# elif n == 18:
#     print("Поздравляю! Разрешено!")
# else:
#     print("Вы еще не родились)")



# n = int(input("Солько Вам лет?  "))
# b = n ** 2
# print(b)




# сity1 = input("назва")
# сity2 = input("назва")
# сity3 = input("назва")
# minCity = min(сity1, сity2, сity3, key=len)
# maxCity = max(сity1, сity2, сity3, key=len)
# print(minCity)
# print(maxCity)