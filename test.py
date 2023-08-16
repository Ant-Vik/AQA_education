from bs4 import BeautifulSoup


# for i in range(1, 6):
#     for j in range(1, i + 1):
#
#         print(j, end=' ')
#     print()


# for i in range(5, 1 - 1, -1):
#     for j in range(5, i - 1, -1):
#
#         print(j, end=' ')
#     print()

# for i in range(1, 5 + 1):
#     for j in range(5, i - 1, -1):
#
#         print(j, end=' ')
#     print()


# n = int(input())
# for i in range(1, 10 + 1):
#     for j in range(n):
#         k = i * n
#     print(k)


# lst = [10, 20, 30, 40, 50]
#
# for lst in range(50, 0, -10):
#     print(lst)


# for i in range(-10, -1 + 1):
#     print(i)


# for i in range(0, 5):
#     for j in range(0, i):
#         print('*', end=' ')
#     print('*')
# for l in range(5, -1, - 1):
#     for k in range(l, 0, -1):
#         print('*', end=' ')
#     print('*')


# aLsit = [100, 200, 300, 400, 500]
# aLsit.reverse()
# print(aLsit)


# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# list3 = list1[0] + list2[0], list1[1] + list2[1], list1[2] + list2[2], list1[3] + list2[3]
#
# print(list3)

# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# for i, j in zip(list1, list2):
#     print(i + j, end=' ')


# aList = [1, 2, 3, 4, 5, 6, 7]
# for i in aList:
#     n = i ** 2
#     print(n)


# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# list3 = list1[0] + list2[0], list1[0] + list2[1], list1[1] + list2[0], list1[1] + list2[1]
# print(list3)


# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]
# total = 0
# for i in list1:
#     for j in list2:
#         total = j
#     print(i, total)
#     list2.pop()

# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# a = 7000
# list1[2][2].insert(2, a)
# print(list1)


# data = dict(
#     id=101010,
#     petId=1,
#     quantity=0,
#     shipDate="2023-07-24T08:55:37.775Z",
#     status='placed',
#     complete=True
# )
#
# url = 'https://petstore.swagger.io/#/store/order'
#
# response = requests.post(url)


# url = 'https://api.github.com/get'
#
# payload = {'key1': 'value1', 'key2': 'value2'}
#
# response = requests.get(url, params=payload)
# print(response.url)

# num1 = int(input())
# num2 = int(input())
#
#
# def sum_nam(num_1, num_2):
#     print(num_1 + num_2)
#
#
# sum_nam()


# def factorial(n):
#     """Функция для вычисления факториала числа (рекурсивный подход)."""
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
#
# print(factorial(5)) # Вызов функции для вычисления факториала числа 5
# # print(result)


# multiply = lambda x, y: x * y  # lambda ключевое слово
# result = multiply(5, 3)  # Вызов анонимной функции
# print(result)


# def test_decor(test):
#     print('первое сообщение')
#     test()
#     print('второе смс')
#     print('третье смс')
#
#
# @test_decor
# def just_test():
#     print('вставка')
#
#     def second_test():
#         print('вставка 2')
#
#     return second_test()


# def print_arguments(*args, **kwargs):
#     """Функция для вывода всех переданных аргументов."""
#     print("Позиционные аргументы:", args)
#     print("Именованные аргументы:", kwargs)
#
#
# print_arguments(1, 2, 3, name="Alice", age=25)


# numbers = [1, 2, 3, 4, 5]
# squared_numbers = map(lambda x: x ** 2, numbers)


# from functools import reduce
# numbers = [1, 2, 3, 4]
# product = reduce(lambda x, y: x * y, numbers)   # Вычисляем произведение всех чисел
# print(product)


# name = ['tolik', 'lenia', 'vlad', 'ivan', 'bob']
# age = [23, 33, 41, 18, 20]
# gender = 'malet'
#
# test = map(lambda x, y, z: f'{x} {y} {z}', name, age, gender)
#
# tester = list(test)
# print(tester)

# name = [1, 2, 3, 4, 5]
# age = [23, 33, 41, 18, 20]
# gender = [6, 7, 8, 9, 10]
#
# test = map(lambda x, y, z: x + y * z, name, age, gender)
#
# tester = list(test)
# print(tester)

# num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
#
# def squares_func(test):
#     return [x ** 2 for x in range(1, len(test) + 1) if x % 2 == 0]
#
#
# print(squares_func(num))


# original_string = "This is some sample text with spaces and more spaces"
# split_parts = original_string.split(' ', maxsplit=6)  # Разделяем на 6 частей
#
# print(split_parts)








html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""


soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.prettify())
print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.title.parent.name)
print(soup.p)
print(soup.p.name)
print(soup.p.string)
print(soup.p["class"])
print(soup.a)
print(soup.find_all('a'))
print(soup.find(id='link3'))

for link in soup.find_all('a'):
    print(link['href'])
    print(link.get('href'))

print(soup.get_text())









