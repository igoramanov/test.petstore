#Сценарии для группы хендлеров "pet"
#POST для создания нового питомца:
import requests

base_url = 'https://petstore.swagger.io/v2'

data = {
    "id": 2112,
    "name": "dog1",
    "photoUrls": [],
    "status": "available"
}

response = requests.post(f'{base_url}/pet', json=data)

if response.status_code == 200:
    print("Питомец создан:", response.json())
else:
    print("Не удалось создать питомца. Статус-код:", response.status_code)



#GET для получения информации о питомце:
import requests

base_url = 'https://petstore.swagger.io/v2'

pet_id = 2112

response = requests.get(f'{base_url}/pet/{pet_id}')

if response.status_code == 200:
    print("Питомец найден:", response.json())
elif response.status_code == 404:
    print("Питомец не найден")
else:
    print("Неожиданный статус-код:", response.status_code)


#DELETE для удаления питомца:
import requests

base_url = 'https://petstore.swagger.io/v2'

pet_id_to_delete = 2112

response = requests.delete(f'{base_url}/pet/{pet_id_to_delete}')

if response.status_code == 200:
    print("Питомец удален")
elif response.status_code == 404:
    print("Питомец не найден")
else:
    print("Не удалось удалить питомца. Статус-код:", response.status_code)

#Сценарии для группы хендлеров "store"
#GET для получения информации о состоянии склада:
import requests

base_url = 'https://petstore.swagger.io/v2'

response = requests.get(f'{base_url}/store/inventory')

if response.status_code == 200:
    print("Информация о складе:", response.json())
else:
    print("Не удалось получить информацию о складе. Статус-код:", response.status_code)

#POST для добавления нового заказа:
import requests

base_url = 'https://petstore.swagger.io/v2'

data = {
    "id": 1200,
    "petId": 2112,
    "quantity": 1,
    "shipDate": "2023-08-21T18:25:43.511Z",
    "status": "placed",
    "complete": False
}

response = requests.post(f'{base_url}/store/order', json=data)

if response.status_code == 200:
    print("Заказ создан:", response.json())
else:
    print("Не удалось создать заказ. Статус-код:", response.status_code)
#DELETE для удаления заказа:
import requests

base_url = 'https://petstore.swagger.io/v2'

order_id_to_delete = 1

response = requests.delete(f'{base_url}/store/order/{order_id_to_delete}')

if response.status_code == 200:
    print("Заказ удален")
elif response.status_code == 404:
    print("Заказ не найден")
else:
    print("Не удалось удалить заказ. Статус-код:", response.status_code)


#Сценарии для группы хендлеров "user"
#POST для создания нового пользователя:
import requests

base_url = 'https://petstore.swagger.io/v2'

data = {
    "id": 2552,
    "username": "Igor",
    "firstName": "Igor",
    "lastName": "Amanov",
    "email": "igoramanov9@gmail.com",
    "phone": "1234567890",
    "userStatus": 1
}

response = requests.post(f'{base_url}/user', json=data)

if response.status_code == 200:
    print("Пользователь создан:", response.json())
else:
    print("Не удалось создать пользователя. Статус-код:", response.status_code)

#GET для получения информации о пользователе:
import requests

base_url = 'https://petstore.swagger.io/v2'

username = 'Igor’'

response = requests.get(f'{base_url}/user/{username}')

if response.status_code == 200:
    print("Информация о пользователе:", response.json())
elif response.status_code == 404:
    print("Пользователь не найден")
else:
    print("Не удалось получить информацию о пользователе. Статус-код:", response.status_code)

#DELETE для удаления пользователя:
import requests

base_url = 'https://petstore.swagger.io/v2'

username_to_delete = 'Igor’'

response = requests.delete(f'{base_url}/user/{username_to_delete}')

if response.status_code == 200:
    print("Пользователь удален")
elif response.status_code == 404:
    print("Пользователь не найден")
else:
    print("Не удалось удалить пользователя. Статус-код:", response.status_code)















