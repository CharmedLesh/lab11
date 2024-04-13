import allure
import pytest
import requests

@allure.title("Тест на обновление информации о пользователе")
def test_update_user():
    url = "https://reqres.in/api/users/2"
    data = {
        "name": "morpheus",
        "job": "zion resident"
    }
    with allure.step("Отправка PUT-запроса для обновления информации о пользователе"):
        response = requests.put(url, json=data)
    
    with allure.step("Проверка статус-кода ответа"):
        assert response.status_code == 200
    
    with allure.step("Проверка заголовка Content-Type"):
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8'
    
    with allure.step("Проверка данных пользователя в ответе"):
        user_data = response.json()
        assert "name" in user_data
        assert "job" in user_data
        assert "updatedAt" in user_data
        assert user_data["job"] == "zion resident"  # Проверка обновленного значения должности пользователя

if __name__ == "__main__":
    pytest.main()
