
'''
Таsk 1.
Написати програму, в якій вказується url = “https://example.com” Далі, у програмі створити словник із
даних, взятих зі сторінки “view-source:https://example.com”, у форматі ключ/значення (як мінімум 10 пар
ключ/значення).
'''


test_dict = {
    'og:locale': 'en_US',
    'og:type': 'website',
    'og:title': 'Mr Bet Casino With a Big Bonus Today',
    'og:description': 'Read all about Mr.Bet Casino here.',
    'og:url': 'https://mrbetcanada.com/',
    'og:site_name': 'https://mrbetcanada.com/test',
    'article:modified_time': '2023-07-17T10:32:14+00:00',
    'og:image': 'https://mrbetcanada.com/wp-content/uploads/sites/36961/mrbet-logo.webp',
    'og:image:width': 2,
    'og:image:height': 1,
    'og:image:type': 'image/webp',
    'twitter:card': 'summary_large_image',
    'twitter:label1': 'Est. reading time',
}


sum_keys = []
sum_values = []
new_value = 777
sum_num = 0
second_test_dict = {}
for key, value in test_dict.items():
    sum_keys.append(key)
    sum_values.append(value)
    sum_num = len(test_dict)
    second_test_dict = test_dict.copy()
    for key in second_test_dict:
        second_test_dict[key] = new_value

uni_values = set(test_dict.values())
if len(uni_values) != len(test_dict.values()):
    print('У словнику є однакові значення!')
else:
    print('У словнику не має однакових значень!')
print(f' Список усіх key у форматі list {sum_keys}')
print(f'Список усіх value у форматі list{sum_values}')
print(f'Всього в словнику {sum_num} пари ключ/значення')
print(second_test_dict)