import allure
import pytest
import requests

@allure.title("Тест на получение информации о пользователе")
def test_single_user():
    url = "https://reqres.in/api/users/2"
    with allure.step("Отправка GET-запроса для получения информации о пользователе"):
        response = requests.get(url)
    
    with allure.step("Проверка статус-кода ответа"):
        assert response.status_code == 200
    
    with allure.step("Проверка заголовка Content-Type"):
        assert response.headers['Content-Type'] == 'application/json; charset=utf-8'
    
    with allure.step("Проверка данных пользователя в ответе"):
        user_data = response.json()["data"]
        assert "id" in user_data
        assert "email" in user_data
        assert "first_name" in user_data
        assert "last_name" in user_data
        assert "avatar" in user_data
        assert len(user_data) == 5  # Проверка наличия всех ожидаемых полей

if __name__ == "__main__":
    pytest.main()
