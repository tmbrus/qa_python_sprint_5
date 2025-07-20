# qa_python_sprint_5
___
### Stellar Burgers autotests:
```test_account_access.py```
+ **test_redirect_to_login_for_unauthorized_user** - Проверка перенаправления неавторизованного пользователя на страницу входа при клике на кнопку 'Личный кабинет'  
+ **test_redirect_to_account_for_authorized_user** - Проверка перехода авторизованного пользователя в личный кабинет при клике на кнопку 'Личный кабинет'  

```test_account_logout.py```
+ **test_user_redirected_to_login_after_logout** - Проверка перенаправления на страницу входа после выхода из аккаунта

```test_account_navigation.py```
+ **test_redirect_to_constructor_from_account** - Проверка перехода на главную страницу через кнопку 'Конструктор' из ЛК
+ **test_redirect_to_main_via_logo_from_account** - Проверка перехода на главную страницу через логотип из ЛК

```test_constructor_navigation.py```
+ **test_switch_to_sauces_tab** - Проверка перехода на таб 'Соусы'
+ **test_switch_to_fillings_tab** - Проверка перехода на таб 'Начинки'
+ **test_switch_to_buns_tab** - Проверка перехода на таб 'Булки'

```test_login_scenarios```
+ **test_login_via_main_page_login_button** - Тест авторизации через кнопку 'Войти' на главной странице странице
+ **test_login_via_account_button_in_header** - Тест авторизации через кнопку 'Личный кабинет' в шапке сайта
+ **test_login_via_register_page_button** - Тест авторизации через ссылку на странице регистрации
+ **test_login_via_password_recovery_page_button** - Тест авторизации через ссылку на странице восстановления пароля

```test_registration.py```
+ **test_successful_registration_with_valid_password** - Проверка успешной регистрации с корректным паролем
+ **test_registration_fails_with_short_password** - Проверка неудачной регистрации с коротким паролем