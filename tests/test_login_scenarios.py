from locators import Locators
from data import Urls
from data import FixedUser
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


# test_login_scenarios.py
"""Тесты различных сценариев авторизации пользователей в системе"""

class TestLoginScenarios:
    """Класс для тестирования различных сценариев авторизации пользователя"""

    def test_login_via_main_page_login_button(self, driver):
        """
        Тест авторизации через кнопку 'Войти' на главной странице
        Шаги:
        1. Открываем главную страницу
        2. Переходим на страницу авторизации
        3. Вводим логин и пароль
        4. Нажимаем кнопку входа
        5. Проверяем успешную авторизацию по данным в ЛК
        """
        # 1. Открытие главной страницы
        driver.get(Urls.LINK)

        # 2. Переход на страницу авторизации
        driver.find_element(*Locators.PURPLE_BUTTON).click()

        # 3. Ввод учетных данных
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(FixedUser.USER_LOGIN_FIXED)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(FixedUser.USER_PASSWORD_FIXED)

        # 4. Нажатие кнопки входа
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(Locators.PURPLE_BUTTON))
        driver.find_element(*Locators.PURPLE_BUTTON).click()

        # Ожидание подтверждения авторизации
        WebDriverWait(driver, 3).until(
            expected_conditions.text_to_be_present_in_element(Locators.PURPLE_BUTTON, "Оформить заказ"))

        # 5. Проверка данных в личном кабинете
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.EMAIL_FIELD))

        # Проверка соответствия email
        assert driver.find_element(*Locators.EMAIL_FIELD).get_attribute("value") == FixedUser.USER_LOGIN_FIXED, \
            "Email в личном кабинете не соответствует ожидаемому"

    def test_login_via_account_button_in_header(self, driver):
        """
        Тест авторизации через кнопку 'Личный кабинет' в шапке сайта
        Шаги:
        1. Открываем главную страницу
        2. Переходим в личный кабинет (неавторизованный)
        3. Вводим логин и пароль
        4. Нажимаем кнопку входа
        5. Проверяем успешную авторизацию
        """
        # 1. Открытие главной страницы
        driver.get(Urls.LINK)

        # 2. Переход в личный кабинет
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()

        # 3. Ввод учетных данных
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(FixedUser.USER_LOGIN_FIXED)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(FixedUser.USER_PASSWORD_FIXED)

        # 4. Нажатие кнопки входа
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(Locators.PURPLE_BUTTON))
        driver.find_element(*Locators.PURPLE_BUTTON).click()

        # Ожидание подтверждения авторизации
        WebDriverWait(driver, 3).until(
            expected_conditions.text_to_be_present_in_element(Locators.PURPLE_BUTTON, "Оформить заказ"))

        # 5. Проверка данных в личном кабинете
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.EMAIL_FIELD))

        # Проверка соответствия email
        assert driver.find_element(*Locators.EMAIL_FIELD).get_attribute("value") == FixedUser.USER_LOGIN_FIXED, \
            "Email в личном кабинете не соответствует ожидаемому"

    def test_login_via_register_page_button(self, driver):
        """
        Тест авторизации через ссылку на странице регистрации
        Шаги:
        1. Открываем главную страницу
        2. Переходим в личный кабинет
        3. Переходим на страницу регистрации
        4. Переходим на страницу входа
        5. Вводим учетные данные
        6. Проверяем авторизацию
        """
        # 1. Открытие главной страницы
        driver.get(Urls.LINK)

        # 2. Переход в личный кабинет
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()

        # 3. Переход на страницу регистрации
        driver.find_element(*Locators.REGISTER_REFERENCE).click()

        # 4. Переход на страницу входа
        driver.find_element(*Locators.LOGIN_REFERENCE_ON_REGISTER_PAGE).click()

        # 5. Ввод учетных данных и авторизация
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(FixedUser.USER_LOGIN_FIXED)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(FixedUser.USER_PASSWORD_FIXED)
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(Locators.PURPLE_BUTTON))
        driver.find_element(*Locators.PURPLE_BUTTON).click()

        # Ожидание подтверждения авторизации
        WebDriverWait(driver, 3).until(
            expected_conditions.text_to_be_present_in_element(Locators.PURPLE_BUTTON, "Оформить заказ"))

        # 6. Проверка данных в личном кабинете
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.EMAIL_FIELD))

        # Проверка соответствия email
        assert driver.find_element(*Locators.EMAIL_FIELD).get_attribute("value") == FixedUser.USER_LOGIN_FIXED, \
            "Email в личном кабинете не соответствует ожидаемому"

    def test_login_via_password_recovery_page_button(self, driver):
        """
        Тест авторизации через ссылку на странице восстановления пароля
        Шаги:
        1. Открываем главную страницу
        2. Переходим в личный кабинет
        3. Переходим на страницу восстановления пароля
        4. Переходим на страницу входа
        5. Вводим учетные данные
        6. Проверяем авторизацию
        """
        # 1. Открытие главной страницы
        driver.get(Urls.LINK)

        # 2. Переход в личный кабинет
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()

        # 3. Переход на страницу восстановления пароля
        driver.find_element(*Locators.FORGOT_PASSWORD_REFERENCE_ON_LOGIN_PAGE).click()

        # 4. Переход на страницу входа
        driver.find_element(*Locators.LOGIN_REFERENCE_ON_REGISTER_PAGE).click()

        # 5. Ввод учетных данных и авторизация
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(FixedUser.USER_LOGIN_FIXED)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(FixedUser.USER_PASSWORD_FIXED)
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(Locators.PURPLE_BUTTON))
        driver.find_element(*Locators.PURPLE_BUTTON).click()

        # Ожидание подтверждения авторизации
        WebDriverWait(driver, 3).until(
            expected_conditions.text_to_be_present_in_element(Locators.PURPLE_BUTTON, "Оформить заказ"))

        # 6. Проверка данных в личном кабинете
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.EMAIL_FIELD))

        # Проверка соответствия email
        assert driver.find_element(*Locators.EMAIL_FIELD).get_attribute("value") == FixedUser.USER_LOGIN_FIXED, \
            "Email в личном кабинете не соответствует ожидаемому"