import requests
from bs4 import BeautifulSoup

"""
Task 1 Створіть клас BankAccount, який має атрибути owner (власник рахунку) та balance
(баланс рахунку). Додайте методи для додавання коштів на рахунок та зняття коштів з рахунку. Також додайте метод
для виведення інформації про рахунок.
"""

# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance
#
#     def dodavanya(self, suma_dodavanya):
#         self.balance += suma_dodavanya
#         return f'Счет пополнено на {suma_dodavanya} сейчас на балансе {self.balance}'
#
#     def vidnimanya(self, suma_vidnimanya):
#         if self.balance >= suma_vidnimanya:
#             self.balance -= suma_vidnimanya
#             return f'С счета снято {suma_vidnimanya} на балансе {self.balance}'
#         else:
#             return f'На балансе {self.balance} а вы пытаетесь снять {suma_vidnimanya}'
#
#     def info(self):
#         return f'На счету {self.owner} сейчас на балансе {self.balance}'
#
#
# account1 = BankAccount('Maks', 0)
#
# print(account1.info())
# print(account1.dodavanya(120))
# print(account1.vidnimanya(30))
# print(account1.info())
# print(account1.vidnimanya(100))


"""
Task 2 Створіть клас Book, який представляє книгу з атрибутами title (назва книги), author (автор книги) та
price (ціна книги). Створіть ще один клас Bookstore, який містить список книг у вигляді об'єктів класу Book.
Додайте методи до класу Bookstore для додавання нових книг, видалення книг, підрахунку загальної вартості усіх книг
та виведення списку доступних книг.
"""

# class Book:
#
#     def __init__(self, title, author, price):
#         self.title = title
#         self.author = author
#         self.price = price
#
#     def __str__(self):
#         return f'title - {self.title}, author - {self.author}, price - {self.price}'
#
#
# class BookStore:
#     def __init__(self):
#         self.books = []
#
#     def add_books(self, book):
#         self.books.append(book)
#         return f'{book} успешно добавлена'
#
#     def del_books(self, book):
#         if book in self.books:
#             self.books.remove(book)
#             return f'{book} успешно удалена'
#         else:
#             return f'Книги {book} не найдено'
#
#     def total_price(self):
#         pass
#
#     def lst_books(self):
#         book_list = []
#         for book in self.books:
#             book_list.append(str(book))
#         result = '\n '.join(book_list)
#         return result
#
#
# book1 = Book('book-1', 'Poma', 230)
# book2 = Book('book-2', 'Tom', 33)
# book3 = Book('book-3', 'Jack', 99)
#
# print(book1)
# book_store = BookStore()
# print(book_store.add_books(book1))
# print(book_store.add_books(book2))
# print(book_store.lst_books())
# print(book_store.del_books(book2))
# print(book_store.lst_books())
# print(book_store.del_books(book3))


"""
Створіть клас Task, який має атрибути title (назва завдання) та priority (пріоритет завдання). Створіть клас
TaskManager, який зберігатиме список об'єктів класу Task. Додайте методи до класу TaskManager для додавання нових
завдань, видалення завдань за назвою, виведення списку завдань відсортованих за пріоритетом та виведення загального
числа завдань.
"""


# class Task:
#     def __init__(self, title, priority=3):
#         self.title = title
#         self.priority = priority
#
#     def __str__(self):
#         return f'Task {self.title}, priority {self.priority}'
#
#
# class TaskManager:
#     def __init__(self):
#         self.tasks = []
#
#     def add_task(self, task):
#         self.tasks.append(task)
#         return f'{task} добавлено успешно'
#
#     def del_task(self, task):
#         if task in self.tasks:
#             self.tasks.remove(task)
#             return f'{task} успешно удалена'
#         else:
#             return f'Task {task} не найдено'
#
#     def sort_by_priority(self):
#         lst = sorted(self.tasks, key=lambda task: task.priority, reverse=True)
#         str1 = ', '.join(str(task) for task in lst)
#         return str1
#
#     def total_tasks(self):
#         return len(self.tasks)
#
#
# task1 = Task('Bug1', 1)
# task2 = Task('Bug2', 3)
#
# taskman = TaskManager()
#
# print(taskman.add_task(task1))
# print(taskman.add_task(task2))
# print(taskman.sort_by_priority())
# print(taskman.total_tasks())
# print(taskman.del_task(task2))
# print(taskman.total_tasks())


"""

"""


# class WebSite:
#     def __init__(self, name, url):
#         self.name = name
#         self.url = url
#
#     def __str__(self):
#         return f'This is site {self.name}'
#
#
# class Slotozilla(WebSite):
#     def __init__(self, name, url):
#         super().__init__(name, url)
#
#     def parsing_h(self):
#         try:
#             response = requests.get(self.url)
#             if response.status_code == 200:
#                 html = response.text
#                 soup = BeautifulSoup(html, 'html.parser')
#                 headers = []
#                 for h in range(1, 7):
#                     headers_h = soup.find_all(f'h{h}')
#                     for tag in headers_h:
#                         headers.append(tag.get_text())
#                 return headers
#             else:
#                 print(f'Not ok {response.status_code}')
#         except requests.exceptions.RequestException as e:
#             print(f'Error response {e}')
#         return []
#
#     def result(self):
#         headers = self.parsing_h()
#         for header in headers:
#             print(header)
#
#
# slot = Slotozilla('slota', 'https://www.slotozilla.com/')
# print(slot)
# print(slot.result())
