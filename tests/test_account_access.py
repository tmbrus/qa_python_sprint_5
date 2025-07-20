from locators import Locators
from data import FixedUser
from data import Urls
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


# test_account_access.py
"""Тесты навигации при клике на кнопку 'Личный кабинет'"""

class TestAccountButtonNavigation:
    """Тестирование навигации при клике на кнопку 'Личный кабинет' для авторизованных и неавторизованных пользователей"""

    def test_redirect_to_login_for_unauthorized_user(self, driver):
        """
        Проверка перенаправления неавторизованного пользователя на страницу входа
        при клике на кнопку 'Личный кабинет'

        Шаги:
        1. Открытие главной страницы
        2. Клик по кнопке 'Личный кабинет'
        3. Проверка перехода на страницу авторизации
        """
        # 1. Открываем главную страницу
        driver.get(Urls.LINK)

        # 2. Переход на страницу авторизации через кнопку 'Личный кабинет'
        driver.find_element(*Locators.PURPLE_BUTTON).click()

        # 3. Проверяем, что мы на странице авторизации
        assert driver.current_url == Urls.LOGIN_PAGE, \
            f'Ожидался переход на страницу входа. Текущий URL: {driver.current_url}, ожидаемый: {Urls.LOGIN_PAGE}'

    def test_redirect_to_account_for_authorized_user(self, driver):
        """
        Проверка перехода авторизованного пользователя в личный кабинет
        при клике на кнопку 'Личный кабинет'

        Шаги:
        1. Открытие главной страницы
        2. Авторизация пользователя
        3. Клик по кнопке 'Личный кабинет'
        4. Проверка перехода в личный кабинет
        """
        # 1. Открываем главную страницу
        driver.get(Urls.LINK)

        # 2.1 Переход на страницу авторизации
        driver.find_element(*Locators.PURPLE_BUTTON).click()

        # 2.2 Ввод учетных данных
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(FixedUser.USER_LOGIN_FIXED)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(FixedUser.USER_PASSWORD_FIXED)

        # 2.3 Подтверждение авторизации
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(Locators.PURPLE_BUTTON))
        driver.find_element(*Locators.PURPLE_BUTTON).click()

        # Ожидание завершения авторизации
        WebDriverWait(driver, 3).until(
            expected_conditions.text_to_be_present_in_element(Locators.PURPLE_BUTTON, "Оформить заказ"))

        # 3. Переход в личный кабинет
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()

        # Ожидание загрузки страницы ЛК
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.EMAIL_FIELD))

        # 4. Проверяем, что мы на странице пользователя
        assert driver.current_url == Urls.ACCOUNT_PAGE, \
            f'Ожидался переход в личный кабинет. Текущий URL: {driver.current_url}, ожидаемый: {Urls.ACCOUNT_PAGE}'