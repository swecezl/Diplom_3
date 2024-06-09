import allure
from selenium.webdriver.common.keys import Keys
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    locators = LoginPageLocators()

    @allure.step('Клик по кнопке "Восстановить пароль"')
    def click_on_password_restore_button(self):
        self.element_is_visible(self.locators.TEXT_BUTTON_RESTORE_PASSWORD).click()

    @allure.step('Авторизоваться')
    def login_user(self, email, password):
        self.element_is_clickable(self.locators.EMAIL).send_keys(email)
        self.element_is_clickable(self.locators.PASSWORD).send_keys(password)
        self.element_is_clickable(self.locators.BUTTON_LOGIN).send_keys(Keys.RETURN)

    @allure.step('Заполнить поле "Email"')
    def fill_email_field(self, email):
        self.element_is_clickable(self.locators.EMAIL).send_keys(email)

    @allure.step('Заполнить поле "Пароль"')
    def fill_password_field(self, password):
        self.element_is_clickable(self.locators.PASSWORD).send_keys(password)

    @allure.step('Клик по кнопке "Войти"')
    def click_on_login_button(self):
        self.element_is_clickable(self.locators.BUTTON_LOGIN).send_keys(Keys.RETURN)

    @allure.step('Проверка, что кнопка "Войти" появилась на экране')
    def check_login_button_is_displayed(self):
        assert self.element_is_clickable(self.locators.BUTTON_LOGIN).is_displayed()