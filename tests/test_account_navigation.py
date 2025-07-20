from locators import Locators
from data import Urls
from data import FixedUser
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


# test_account_navigation.py
"""Тесты навигации из личного кабинета (переходы через конструктор и логотип)"""

class TestNavigationFromAccountPage:
    """Группа тестов для проверки навигации из личного кабинета пользователя"""

    def test_redirect_to_constructor_from_account(self, driver):
        """
        Проверка перехода на главную страницу через кнопку 'Конструктор' из ЛК
        Шаги:
        1. Авторизация пользователя
        2. Переход в личный кабинет
        3. Клик по кнопке 'Конструктор'
        4. Проверка возврата на главную страницу
        """
        # 1. Авторизация
        driver.get(Urls.LINK)
        driver.find_element(*Locators.PURPLE_BUTTON).click()
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(FixedUser.USER_LOGIN_FIXED)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(FixedUser.USER_PASSWORD_FIXED)
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(Locators.PURPLE_BUTTON))
        driver.find_element(*Locators.PURPLE_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.text_to_be_present_in_element(Locators.PURPLE_BUTTON, "Оформить заказ"))

        # 2. Переход в ЛК
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.EMAIL_FIELD))

        # 3. Клик по конструктору
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()

        # 4. Проверка редиректа
        assert driver.current_url == Urls.LINK, \
            f'Ожидался переход на главную страницу. Текущий URL: {driver.current_url}'

    def test_redirect_to_main_via_logo_from_account(self, driver):
        """
        Проверка перехода на главную страницу через логотип из ЛК
        Шаги:
        1. Авторизация пользователя
        2. Переход в личный кабинет
        3. Клик по логотипу
        4. Проверка возврата на главную страницу
        """
        # 1. Авторизация
        driver.get(Urls.LINK)
        driver.find_element(*Locators.PURPLE_BUTTON).click()
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(FixedUser.USER_LOGIN_FIXED)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(FixedUser.USER_PASSWORD_FIXED)
        WebDriverWait(driver, 3).until(
            expected_conditions.element_to_be_clickable(Locators.PURPLE_BUTTON))
        driver.find_element(*Locators.PURPLE_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.text_to_be_present_in_element(Locators.PURPLE_BUTTON, "Оформить заказ"))

        # 2. Переход в ЛК
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(Locators.EMAIL_FIELD))

        # 3. Клик по логотипу
        driver.find_element(*Locators.HEADER_LOGO).click()

        # 4. Проверка редиректа
        assert driver.current_url == Urls.LINK, \
            f'Ожидался переход на главную страницу. Текущий URL: {driver.current_url}'