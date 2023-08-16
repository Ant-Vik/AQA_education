import requests
from bs4 import BeautifulSoup

'''
Task 1 
На основі існуючого класу WebSite: Створити підклас. В цьому підкласі мають бути методи, що парсять 
сторінку, а далі забирають значення із тегів. Написати три методи на три різні теги (наприклад пошук по тегу h, a, 
title, дивлячись що у вас за сайти) Використати: from bs4 import BeautifulSoup. Після чого, створити 2 об’єкти (2 
сайти), в яких викликати методи підкласу, що шукають теги.
'''


# class WebSite:
#
#     def __init__(self, name, url):
#         self.name = name
#         self.url = url
#
#     def __str__(self):
#         return f"This is site: {self.name}. Url = {self.url}"
#
#
# class CasinoX(WebSite):
#     def __init__(self, name, url):
#         super().__init__(name, url)
#
#     def parsing_h(self):
#         response = requests.get(self.url)
#         if response.status_code == 200:
#             html = response.text
#             soup = BeautifulSoup(html, 'html.parser')
#             headers = []
#             for h in range(1, 7):
#                 headers_h = soup.find_all(f'h{h}')
#                 for tag in headers_h:
#                     headers.append(tag.get_text())
#             return headers
#         else:
#             print(f'Not ok {response.status_code}')
#
#     def parsing_a(self):
#         response = requests.get(self.url)
#         if response.status_code == 200:
#             html = response.text
#             soup = BeautifulSoup(html, 'html.parser')
#             links = soup.find_all('a')
#             for link in links:
#                 print(link['href'])
#         else:
#             print(f'Not ok {response.status_code}')
#
#     def parsing_title(self):
#         response = requests.get(self.url)
#         if response.status_code == 200:
#             html = response.text
#             soup = BeautifulSoup(html, 'html.parser')
#             titles = soup.find('title')
#             if titles:
#                 title_text = titles.text
#                 print(f"Title: {title_text}")
#         else:
#             print(f'Not ok {response.status_code}')
#
#     def result(self):
#         headers = self.parsing_h()
#         for header in headers:
#             print(header)
#
#
# slot = CasinoX('site', 'https://casino-x.live/')
# print(slot)
# print(slot.result())
# print(slot.parsing_a())
# print(slot.parsing_title())

'''
Task 2
Напишіть код по схемі: (тематика класу, логіка функцій будь-яка)
'''
#
#
# class Book:
#
#     def __init__(self, title4, author1):
#         self.title4 = title4
#         self.author1 = author1
#
#
# class SubClass1(Book):
#
#     def method_2(self, famous2):
#         print(f'{self.author1} = {famous2} из 5')
#
#
# class SubClass2(Book):
#
#     def method_3(self, price3):
#         print(f'{self.title4} = {price3}$')
#
#
# sub_class1 = SubClass1('Dream Catcher', 'King')
# sub_class2 = SubClass2('Dream Catcher', 'King')
# sub_class1.method_2(5)
# sub_class2.method_3(500)
