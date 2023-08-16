import requests

# url = 'https://api.privatbank.ua/p24api/exchange_rates?date=20.07.2023'
#
# response = requests.get(url)
# data = response.json()
# # print(data)
#
# lst = []
# str = ''
# for item in data['exchangeRate']:
#     currency = item['currency']
#     sale_rate_nb = item['saleRateNB']
#     # lst.append({'currency': currency, 'price': sale_rate_nb})
#     str += f'Валюта {currency}, Курс {sale_rate_nb}\n'
# print(str)


# url = 'https://petstore.swagger.io/v2/user/createWithArray'
#
# # response = requests.get(url)
#
# data = [
#     {
#         "id": 8948948949898989,
#         "username": "AQAtest",
#         "firstName": "testFN",
#         "lastName": "testLN",
#         "email": "test@gmail.com",
#         "password": "testpass",
#         "phone": "0997234234",
#         "userStatus": 0
#     }
# ]
#
# response = requests.post(url, json=data)
#
# if response.status_code == 200:
#     print(response.json())
# else:
#     print(response.status_code)


# url = 'https://petstore.swagger.io/v2/user/AQAtest'


# data = [
#     {
#         "id": 8948948949898989,
#         "username": "AQAtest",
#         "firstName": "testFN",
#         "lastName": "testLN",
#         "email": "test@gmail.com",
#         "password": "testpass",
#         "phone": "0997234234",
#         "userStatus": 0
#     }
# ]
#
# response = requests.get(url)
#
# if response.status_code == 200:
#     print(response.json())
# else:
#     print(response.status_code)
