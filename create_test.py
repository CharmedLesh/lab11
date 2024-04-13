import allure
import pytest
import requests

@allure.title("Тест на создание пользователя")
def test_create_user():
    url = "https://reqres.in/api/users"
    data = {
        "name": "morpheus",
        "job": "leader"
    }
    with allure.step("Отправка POST-запроса для создания пользователя"):
        response = requests.post(url, json=data)

    with allure.step("Проверка статус-кода ответа"):
        assert response.status_code == 201
    
    with allure.step("Проверка заголовка Content-Type"):
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8'
    
    with allure.step("Проверка данных пользователя в ответе"):
        user_data = response.json()
        assert "id" in user_data
        assert "name" in user_data
        assert "job" in user_data
        assert "createdAt" in user_data
        assert user_data["name"] == "morpheus"  # Проверка созданного имени пользователя

if __name__ == "__main__":
    pytest.main()