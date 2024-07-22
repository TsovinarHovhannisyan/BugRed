import pytest
import requests

BASE_URL = "http://users.bugred.ru/tasks/rest"

@pytest.fixture(scope="module")
def user_data():
    return {
        "email": "syuzi1@gmail.com",
        "name": "syuzi1",
        "password": "12345678"
    }

@pytest.fixture(scope="module")
def updated_user_data():
    return {
        "name": "Syzu1",
        "email": "syuzi1@gmail.com",
        "birthday": "12.01.97",
        "gender": "f",
        "date_start": "1.11.2021",
        "hobby": "Test_AGBU",
        "name1": "Test_AGBU",
        "surname1": "Test",
        "fathername1": "Testi",
        "cat": "x",
        "dog": "Smokey",
        "parrot": "Lola",
        "cavy": "Bubba",
        "hamster": "George",
        "squirrel": "Ollie",
        "phone": "055555555",
        "adres": "Komitas 1/2",
        "inn": "123456789101"
    }

def test_register_user(user_data):
    url = f"{BASE_URL}/doregister"
    response = requests.post(url, json=user_data)
    assert response.status_code == 200

def test_get_user(user_data):
    url = f"{BASE_URL}/magicsearch"
    response = requests.post(url, json={"query": user_data["email"]})
    assert response.status_code == 231

def test_update_user_data(updated_user_data):
    url = f"{BASE_URL}/fullupdateuser"
    response = requests.put(url, json=updated_user_data)
    assert response.status_code == 200

def test_add_avatar(user_data):
    url = f"{BASE_URL}/addavatar/?email={user_data['email']}"
    files = {'avatar': open('images.jpg', 'rb')}
    response = requests.post(url, files=files)
    assert response.status_code == 200

def test_delete_avatar(user_data):
    url = f"{BASE_URL}/deleteavatar/?email={user_data['email']}"
    response = requests.delete(url)
    assert response.status_code == 200

def test_delete_user(user_data):
    url = f"{BASE_URL}/deleteuser/?email={user_data['email']}"
    response = requests.delete(url)
    assert response.status_code == 200