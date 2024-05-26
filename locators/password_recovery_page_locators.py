from selenium.webdriver.common.by import By


class RecoveryPasswordPageLocators:

    EMAIL = (By.XPATH, '//input[@name="name"]')  # поле ввода "Email" для восстановления пароля
    BUTTON_RESTORE = (By.XPATH, "//button[text()='Восстановить']")  # кнопка "Восстановить"
    BUTTON_SHOW_OR_HIDE_PASSWORD = (By.XPATH, '//div[@class="input__icon input__icon-action"]') # кнопка "показать/скрыть пароль"
    PASSWORD_FIELD_DEFAULT = (By.XPATH, '//input[@type="password"]')
    PASSWORD_FIELD_ACTIVE = (By.XPATH, '//input[@type="text"]')
    BUTTON_SAVE = (By.XPATH, '//button[text()="Сохранить"]') # кнопка "Сохранить"