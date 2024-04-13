import allure
import pytest
import requests

@allure.title("Тест на удаление пользователя")
def test_delete_user():
    url = "https://reqres.in/api/users/2"
    with allure.step("Отправка DELETE-запроса для удаления пользователя"):
        response = requests.delete(url)
    
    with allure.step("Проверка статус-кода ответа"):
        assert response.status_code == 204  # Проверка успешного удаления пользователя

if __name__ == "__main__":
    pytest.main()