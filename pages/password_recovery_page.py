from faker import Faker
import allure
from locators.password_recovery_page_locators import RecoveryPasswordPageLocators
from pages.base_page import BasePage

faker = Faker()


class RecoveryPasswordPage(BasePage):
    locators = RecoveryPasswordPageLocators()

    @allure.step('Ввод email в поле "email"')
    def input_email_in_email_field(self):
        self.element_is_visible(self.locators.EMAIL).send_keys(faker.free_email())

    @allure.step('Клик по кнопке "Восстановить"')
    def click_on_restore_button(self):
        self.element_is_visible(self.locators.BUTTON_RESTORE).click()

    @allure.step('Клик по кнопке "показать/скрыть пароль"')
    def click_on_show_or_hide_password_button(self):
        self.element_is_visible(self.locators.BUTTON_SHOW_OR_HIDE_PASSWORD).click()

    @allure.step('Проверка активации кнопки "показать/скрыть пароль"')
    def check_show_or_hide_password_button_is_active(self):
        assert self.element_is_presence(self.locators.PASSWORD_FIELD_ACTIVE)

    @allure.step('Проверка, что кнопка "Восстановить" появилась на экране')
    def check_restore_button_is_displayed(self):
        assert self.element_is_visible(self.locators.BUTTON_RESTORE).is_displayed()

    @allure.step('Проверка, что кнопка "Сохранить" появилась на экране')
    def check_save_button_is_displayed(self):
        assert self.element_is_visible(self.locators.BUTTON_SAVE).is_displayed()