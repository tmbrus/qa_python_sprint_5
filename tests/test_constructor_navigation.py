from locators import Locators
from data import Urls
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


# test_constructor_navigation.py
"""Тесты навигации по разделам конструктора бургеров"""

class TestConstructorTabsNavigation:
    """Тесты навигации по табам конструктора"""
    def test_switch_to_sauces_tab(self, driver):
        """
                Проверка перехода на таб 'Соусы'
                1. Открываем главную страницу
                2. Кликаем на таб 'Соусы'
                3. Проверяем:
                   - Отображение раздела соусов
                   - Активное состояние таба
                """

        driver.get(Urls.LINK)

        driver.find_element(*Locators.CONSTRUCTOR_SAUCE_TAB).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.CONSTRUCTOR_MENU_TEXT_SAUCE))
        assert "tab_tab__1SPyG" in driver.find_element(
            *Locators.CONSTRUCTOR_SAUCE_TAB).get_attribute("class")

    def test_switch_to_fillings_tab(self, driver):
        """
                Проверка перехода на таб 'Начинки'
                1. Открываем главную страницу
                2. Кликаем на таб 'Начинки'
                3. Проверяем:
                   - Отображение раздела начинок
                   - Активное состояние таба
                """

        driver.get(Urls.LINK)

        driver.find_element(*Locators.CONSTRUCTOR_FILLING_TAB).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.CONSTRUCTOR_MENU_TEXT_FILLING))
        assert "tab_tab__1SPyG" in driver.find_element(
            *Locators.CONSTRUCTOR_FILLING_TAB).get_attribute("class")

    def test_switch_to_buns_tab(self, driver):
        """
                Проверка перехода на таб 'Булки'
                1. Открываем главную страницу
                2. Переходим на таб 'Начинки' (чтобы сменить активный таб)
                3. Кликаем на таб 'Булки'
                4. Проверяем:
                   - Отображение раздела булок
                   - Активное состояние таба
                """

        driver.get(Urls.LINK)

        driver.find_element(*Locators.CONSTRUCTOR_FILLING_TAB).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.CONSTRUCTOR_MENU_TEXT_FILLING))

        driver.find_element(*Locators.CONSTRUCTOR_BUN_TAB).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.CONSTRUCTOR_MENU_TEXT_BUN))
        assert "tab_tab__1SPyG" in driver.find_element(
            *Locators.CONSTRUCTOR_BUN_TAB).get_attribute("class")
