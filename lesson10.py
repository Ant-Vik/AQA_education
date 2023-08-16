# n = int(input())
# print(list(range(1, n)))

# n = [1, 2, 3, 4, 5, 6, 7, 8]
#
# if 2 in n:
#     print('yes')


# n = [1, 2, 3, 4, 5, 6, 7, 8]
#
# if 0 not in n:
#     print('yes')

# n = [1, 2, 3, 4, 5, 6, 7, 8]
# print(n[1:3])
# print(n[2:5])


# n = [1, 2, 3, 4, 5, 6, 7, 8]
# n[2:5] = [7, 9, 0,]
# print(n)


# n = [1, 2, 3, 4, 5, 6, 7, 8]
# print(sum(n))


# n = [1, 2, 3, 4, 5, 6, 7, 8]
# print(min(n))
# print(max(n))

# n = ['a', 's', 'c']
# print(min(n))
# print(max(n))


# n = [1, 2, 3, 4, 5, 6, 7, 8]
# print(n[:6])


# Среднее аррифметическое
# n = [1, 2, 3, 4, 5, 6, 7, 8]
# x = sum(n) / len(n)
# print(x)


# n = [1, 2, 3, 4, 5, 6, 7, 8]
# n[1] = 'test'
# print(n)


# До пустого списка тоже можно добавить элемент в конец
# n = [1, 2, 3, 4, 5, 6, 7, 8]
# n.append(99)
# print(n)


# n = ['test', 'python', 'best']
# n.append('best test')
# n.extend('best test')
# print(n)


# n = [1, 2, 3, 4, 5, 6, 7, 8]
# del n[1]
# del n[3:6]
# print(n)

# n = [1, 2, 3, 4, 5, 6, 7, 8]
# del n[:2]
# print(n)


# n = []
# n[0] = 'test' # Будет ошибка
# n.append('test') # В пустой список можно вот так добавить элемент
# print(n)


# n = [1, 2, 3, 4, 5, 6, 7, 8]
# print(*n)
# print(*n, sep='\n')


# s = 'seo'
# l = list(s)
# print(l)

# s = 'Привет меня зовут Витя'
# b = s.split()
# l = '\n'.join(b)
# print(l)

# n = input()
# names = ['Roma', 'Thomas', 'Karl', 'Took']
# names.insert(0, n)
# print(names)




# names = ['Roma', 'Thomas', 'Karl', 'Took'] # Такой код работает корректно
# test = names.index('Karl')
# print(test)


# names = ['Roma', 'Thomas', 'Karl', 'Took'] # Такой код отдаст ошибку из-за того что такого индекса нет в списке
# test = names.index('Test')
# print(test)




# names = ['Roma', 'Thomas', 'Karl', 'Took'] # Чтобы избежать ошибки можно написать так
# if 'Anders' in names:
#     test = names.index('Anders')
#     print(test)
# else:
#     print('Такого имени нет')





# names = 'Roma Thomas Karl Took'
# test = names.split(' ', 2)
# print(test)

