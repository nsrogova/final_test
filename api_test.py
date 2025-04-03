import requests
from urllib3 import request


def test_get_users():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    assert response.status_code == 200
    print(response.json())

    # Проверяем, что ответ содержит список пользователей
    assert isinstance(response.json(), list)

    # Проверяем, что в списке есть хотя бы один пользователь
    assert len(response.json()) > 0


def test_get_user_by_id():
    user_id = 1
    response = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
    assert response.status_code == 200
    print(response.json())

    # Проверяем, что полученный пользователь имеет правильный ID
    user = response.json()
    assert user['id'] == user_id, "Неверный id"

# Тест для GET-запроса с query параметрами
def test_get_users_with_query():
    params = {'name': 'Leanne Graham'}
    response = requests.get("https://jsonplaceholder.typicode.com/users", params=params)
    assert response.status_code == 200

    # Выводим ответ
    print("Ответ на test_get_users_with_query:", response.json())

    # Проверяем, что ответ содержит пользователей с заданным именем
    users = response.json()
    assert any(user['name'] == 'Leanne Graham' for user in users)


# Тест для GET-запроса с path параметрами
def test_get_user_by_id():
    user_id = 1  # Пример ID пользователя
    response = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
    assert response.status_code == 200

    # Выводим ответ
    print("Ответ на test_get_user_by_id:", response.json())
    user = response.json()
    assert user['id'] == user_id


# Тест для POST-запроса с body параметрами
def test_create_user():
    new_user = {
        'name': 'John Doe',
        'username': 'johndoe',
        'email': 'johndoe@example.com'
    }
    response = requests.post("https://jsonplaceholder.typicode.com/users", json=new_user)
    assert response.status_code == 201
    print("Ответ на test_create_user:", response.json())

    # Проверяем, что созданный пользователь имеет правильные данные
    created_user = response.json()
    assert created_user['name'] == new_user['name']
    assert created_user['username'] == new_user['username']
    assert created_user['email'] == new_user['email']

def response():
    body = {
        "name": "Alex",
        "userName": "Ron"
    }
    response = requests.get("http://ya.ru")
    assert requests.status_codes == 201
    print(response.json())

    jsonBoby = response.json()
    assert jsonBoby['name'] == body['name']
    assert jsonBoby['userName'] == body['userName']