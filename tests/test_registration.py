import pytest
from locators import Locators
from data import Urls
from data import FixedUser
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


# test_registration.py
"""Тесты функционала регистрации новых пользователей в системе"""

class TestRegistrationFunctionality:
    """Класс для тестирования сценариев регистрации пользователей"""

    def test_successful_registration_with_valid_password(self, driver, generated_user):
        """
        Проверка успешной регистрации с корректным паролем
        Шаги:
        1. Открытие формы регистрации
        2. Заполнение данных пользователя
        3. Отправка формы
        4. Авторизация под новыми данными
        5. Проверка успешности регистрации
        """
        # 1. Открытие формы регистрации
        # Открываем главную страницу
        driver.get(Urls.LINK)
        # Переход на страницу регистрации
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.REGISTER_REFERENCE).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.NAME_FIELD_ON_REG_PAGE))

        # 2. Заполнение данных пользователя
        driver.find_element(*Locators.NAME_FIELD_ON_REG_PAGE).send_keys(generated_user.user_name)
        driver.find_element(*Locators.EMAIL_FIELD_ON_REG_PAGE).send_keys(generated_user.login)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(generated_user.password)

        # 3. Отправка формы
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(Locators.PURPLE_BUTTON))
        driver.find_element(*Locators.PURPLE_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.text_to_be_present_in_element(Locators.PURPLE_BUTTON, "Войти"))

        # 4. Авторизация под новыми данными
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(generated_user.login)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(generated_user.password)
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(Locators.PURPLE_BUTTON))
        driver.find_element(*Locators.PURPLE_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.text_to_be_present_in_element(Locators.PURPLE_BUTTON, "Оформить заказ"))

        # 5. Проверка успешности регистрации
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.EMAIL_FIELD))
        assert driver.find_element(*Locators.EMAIL_FIELD).get_attribute("value") == generated_user.login, \
            "Email в личном кабинете не соответствует зарегистрированному"

    @pytest.mark.parametrize('password_length', [3, 5],
                             ids=['пароль из 3 символов', 'пароль из 5 символов'])
    def test_registration_fails_with_short_password(self, driver, generated_user, password_length):
        """
        Проверка неудачной регистрации с коротким паролем
        Шаги:
        1. Открытие формы регистрации
        2. Заполнение данных с коротким паролем
        3. Попытка регистрации
        4. Проверка сообщения об ошибке
        """
        # 1. Открытие формы регистрации
        driver.get(Urls.LINK)
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.REGISTER_REFERENCE).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.NAME_FIELD_ON_REG_PAGE))

        # 2. Заполнение данных с коротким паролем
        driver.find_element(*Locators.NAME_FIELD_ON_REG_PAGE).send_keys(generated_user.user_name)
        driver.find_element(*Locators.EMAIL_FIELD_ON_REG_PAGE).send_keys(generated_user.login)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(generated_user.password[0:password_length])

        # 3. Попытка регистрации
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(Locators.PURPLE_BUTTON))
        driver.find_element(*Locators.PURPLE_BUTTON).click()

        # 4. Проверка сообщения об ошибке
        assert driver.find_element(*Locators.ERROR_TEXT).text == "Некорректный пароль", \
            "Не отображается сообщение о некорректном пароле"