login_button = ".//button[text()='Войти в аккаунт']" #кнопка Войти в аккаунт
header_input = "//h2[text()='Вход']" #заголовок Вход
input_button = ".//button[text()='Войти']" #кнопка Войти
input_button_registration = "//a[text()='Войти']" #кнопка Войти в панели регистрации
recovery_password_button = "//a[text()='Восстановить пароль']" #кнопка Восстановить пароль
exit_button = "//button[text()='Выход']" #кнопка Выход

register_button_string = ".//a[text()='Зарегистрироваться']" #строка-кнопка Зарегистрироваться
register_button = ".//button[text()='Зарегистрироваться']" #кнопка Зарегистрироваться

string_name = "//label[text()='Имя']/following::input[1]" #строка имя
string_email = "//label[text()='Имя']/following::input[2]" #строка Email
string_password = "//label[text()='Пароль']/following::input" #строка Пароль

string_email_area_local = "//input[@type='text']" #строка Еmail в личном кабинете
string_password_area_local = "//input[@type='password']" #строка Пароль в личном кабинете

local_area_button = "//p[text()='Личный Кабинет']" #кнопка Личный Кабинет
constructor_button = "//p[text()='Конструктор']" #кнопка Конструктор
profile_button = "//a[text()='Профиль']" #кнопка Профиль

error_line_incorrect_password = "//p[text()='Некорректный пароль']" #строка ошибки Некорректный пароль

button_place_an_order = "//button[text()='Оформить заказ']" #кнопка Оформить заказ

logo = "[xmlns='http://www.w3.org/2000/svg'][width='290']" #логотип STELLAR BURGER

sauces_section = "//span[text()='Соусы']/parent::div" #раздел Соусы
tab_sauces_section = "[class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']" #раздел Соусы выбранный

fillings_section = "//span[text()='Начинки']/parent::div" #раздел Начинки
tab_fillings_section = "[class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']" #раздел Начинки выбранный

buns_section = "//span[text()='Булки']/parent::div" #раздел Булки
tab_buns_section = "[class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']" #раздел Булки выбранный