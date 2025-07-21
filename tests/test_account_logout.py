from locators import Locators
from data import Urls
from data import FixedUser
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


# test_account_logout.py
"""Тесты функционала выхода из учетной записи пользователя"""

class TestLogoutFunctionality:
    """Класс для тестирования сценариев выхода из аккаунта"""

    def test_user_redirected_to_login_after_logout(self, driver):
        """
        Проверка перенаправления на страницу входа после выхода из аккаунта
        Шаги:
        1. Авторизация пользователя
        2. Переход в личный кабинет
        3. Выход из аккаунта
        4. Проверка перенаправления на страницу входа
        """
        # 1. Авторизация пользователя
        # Открываем главную страницу
        driver.get(Urls.LINK)
        # Переход на страницу авторизации
        driver.find_element(*Locators.PURPLE_BUTTON).click()
        # Ввод учетных данных
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(FixedUser.USER_LOGIN_FIXED)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(FixedUser.USER_PASSWORD_FIXED)
        # Подтверждение авторизации
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(Locators.PURPLE_BUTTON))
        driver.find_element(*Locators.PURPLE_BUTTON).click()
        # Ожидание завершения авторизации
        WebDriverWait(driver, 3).until(
            expected_conditions.text_to_be_present_in_element(Locators.PURPLE_BUTTON, "Оформить заказ"))

        # 2. Переход в личный кабинет
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.EMAIL_FIELD))

        # 3. Выход из аккаунта
        driver.find_element(*Locators.EXIT_BUTTON).click()
        # Ожидание перехода на страницу входа
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.TEXT_ON_LOGIN_PAGE))

        # 4. Проверка перенаправления
        assert driver.current_url == Urls.LOGIN_PAGE, \
            f'Ожидался переход на страницу входа. Текущий URL: {driver.current_url}, ожидаемый: {Urls.LOGIN_PAGE}'