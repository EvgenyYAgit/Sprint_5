# Проект автоматизации сервиса Stellar Burgers

## Основа для написания автотестов — фреймворк pytest.

### Селекторы для автотестов: 

.//button[text()='Войти в аккаунт'] #кнопка войти

.//a[text()='Зарегистрироваться'] #кнопка Зарегистрироваться

.//fieldset[1]//input #строка имя

.//fieldset[2]//input #строка Email

.//fieldset[3]//input #строка пароль

.//button[text()='Зарегистрироваться'] #кнопка Зарегистрироваться

//div[1]//h2 #заголовок Вход

//div[1]//fieldset[3]//p #строка ошибки Некорректный пароль

//section[2]//button #кнопка Войти в аккаунт

//div[1]//button #кнопка Войти

//div[1]//section[2]//button #кнопка Оформить заказ

[xmlns='http://www.w3.org/2000/svg'][width='290'] #логотип STELLAR BURGER

//div[1]//main/section[1]/div[2]/ul[1]/a[1]/p #элемент Флюоресцентная булка R2-D3

//div[1]/div/main/section[1]/div[2]/ul[2]/a[1]/p #элемент Соус Spicy-X

//div[1]//section[1]/div[2]/ul[3]/a[2]/p #элемент Говяжий метеорит (отбивная)
