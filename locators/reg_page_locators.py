from selenium.webdriver.common.by import By


class RegPageLocators:
    # форма регистрации
    TEXT_BUTTON_LOGIN = (By.LINK_TEXT, "Войти")  # текст-кнопка "Войти"
    CREATED_NAME = (By.XPATH, "(//input[@name='name'])[1]")  # поле ввода "Имя" для регистрации
    CREATED_EMAIL = (By.XPATH, "(//input[@name='name'])[2]")  # поле ввода "Email" для регистрации
    CREATED_PASSWORD = (By.XPATH, "//input[@name='Пароль']")  # поле ввода "Пароль" для регистрации
    BUTTON_REG_ACCOUNT = (By.XPATH, "//button[text()='Зарегистрироваться']")  # кнопка "Зарегистрироваться"
    ERROR_INCORRECT_PASSWORD = (By.CSS_SELECTOR, "p.input__error.text_type_main-default") # ошибка "Некорректный пароль"