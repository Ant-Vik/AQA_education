# a = int(input('test'))
#
# if 2 <= a <= 17:
#     b = 3
#     p = a*a + b*b
# else:
#     b = 5
# p = (a + b) * (a + b)
# print(p)


# x = int(input('test'))
#
# if x >= -1 and x <= 17:
#     print("Належить")
# else:
#     print("Не належить")



# x = int(input('test'))
#
# if not -3 <= x <= 7:
#     print("Належить")
# else:
#     print("Не належить")




# x = int(input('test'))
# y = int(input('test'))
#
#
# if  x > 0:
#     if y > 0:
#         print('1')
#     else:
#         print('4')
# else:
#     if y > 0:
#         print('2')
#     else:
#         print('3')

# x = int(input('test'))
# y = int(input('test'))
# c = int(input('test'))
#
#
# if  x == y == c:
#         print('равносторонний')
# elif x == y or x == c or y == c:
#         print('равнобедренный')
# elif x != y and x != c and y != c:
#         print('разносторонний')






# x = int(input('test'))
# y = int(input('test'))
# c = int(input('test'))
#
# if  x < y < c or x > y > c:
#     print(y)
# elif y < x < c or y > x > c:
#     print(x)
# else:
#     print(c)

# elif c < x < y or c > x > y
#         print(c)



# x = int(input('test'))
# y = int(input('test'))
# c = int(input('test'))
#
# if  x < y < c or x > y > c:
#     print(y)
# elif y < x < c or y > x > c:
#     print(x)
# else:
#     print(c)




x = int(input('число 1  '))
y = int(input('число 2  '))
operator = (input('оператор  '))
result = 0

if  operator == "+":
    result = x + y
elif operator == "-":
    result = x - y
elif operator == "/":
    result = x / y
elif operator == "*":
    result = x * y
print(f'{x} {operator} {y} = {result}')


# elif operator == "/" and y == 0:
#     print("на ноль днлить нельзя")