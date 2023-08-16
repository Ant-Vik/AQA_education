import requests


data = dict(
    id=77777,
    category=dict(
        id=111,
        name='Luffi'
    ),
    name='doggie',
    photoUrls=[
        'url_img'
    ],
    tags=[
        dict(
            id=345,
            name='luf'
        )
    ],
    status='available'
)


''' Додаємо тварину на сервер. '''

url = 'https://petstore.swagger.io/v2/pet/'
response = requests.post(url, json=data)

if response.status_code == 200:
    print(f'Статус код = {response.status_code}\nЗапит створено. {response.json()}')
else:
    print('Помилка при виконанні запиту.\n404')

petId = data['category']['id']
print(petId)

''' Отримуємо тварину яку додали на сервер. '''

url_get_pet = 'https://petstore.swagger.io/v2/pet/77777'
response_get_pet = requests.get(url_get_pet)

if response_get_pet.status_code == 200:
    print(response_get_pet.json())
elif response_get_pet.status_code == 400:
    print('Даний ідентифікатор невірний.\n400')
else:
    print('Помилка при виконанні запиту.\n404')


''' Видаляємо додану тварину з сервера. '''

url_del_pet = 'https://petstore.swagger.io/v2/pet/77777'
response_del_pet = requests.delete(url_del_pet)

if response_del_pet.status_code == 200:
    print(f'{response_del_pet.json()} видалено')
elif response_del_pet.status_code == 400:
    print('Даний ідентифікатор невірний.\n400')
else:
    print('Помилка при виконанні запиту.\n404')


''' Перевіряємо чи видалення тварини з серверу пройшло успішно. '''

url_after_del = 'https://petstore.swagger.io/v2/pet/77777'
response_after_del = requests.get(url_after_del)

if response_after_del.status_code == 404:
    print('Не знайдено. Вірогідно запис видалено.\n404')
else:
    print(f'Тварину не видалено: {response_after_del.json()}')

