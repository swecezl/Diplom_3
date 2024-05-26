import allure
from locators.main_page_locators import MainPageLocators
from locators.account_page_locators import AccountPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    locators = MainPageLocators()

    @allure.step('Клик по кнопке: ')
    def click_on_button(self, locator):
        self.element_is_visible(locator).click()

    @allure.step('Клик по кнопке "Личный Кабинет"')
    def click_on_personal_account_button(self):
        self.element_is_visible(self.locators.BUTTON_PERSONAL_ACCOUNT).click()

    @allure.step('Клик по кнопке "Войти в аккаунт"')
    def click_on_login_in_account_button(self):
        self.element_is_visible(self.locators.BUTTON_ACCOUNT).click()

    @allure.step('Клик по кнопке "Конструктор"')
    def click_on_constructor_button(self):
        self.element_is_clickable(self.locators.BUTTON_CONSTRUCTOR).click()

    @allure.step('Проверка, что заголовок "Соберите бургер" появился на экране')
    def check_title_assemble_burger_is_displayed(self):
        assert self.element_is_visible(self.locators.TITLE_ASSEMBLE_BURGER).is_displayed()

    @allure.step('Клик по кнопке "Лента заказов"')
    def click_on_orders_line_button(self):
        self.element_is_clickable(self.locators.BUTTON_ORDERS_LINE).click()

    @allure.step('Проверка, что заголовок "Лента заказов" появился на экране')
    def check_title_orders_line_is_displayed(self):
        assert self.element_is_visible(self.locators.TITLE_ORDERS_LINE).is_displayed()

    @allure.step('Клик по ингредиенту для бургера')
    def click_on_burger_ingredient(self):
        self.element_is_visible(self.locators.BURGER_INGREDIENT).click()

    @allure.step('Проверка, что появилось всплывающее окно с "Детали ингредиента"')
    def check_ingredient_pop_up_window_is_displayed(self):
        assert self.element_is_visible(self.locators.POP_UP_WINDOW_INGR_DETAILS).is_displayed()

    @allure.step('Клик по кнопке "крестик" во всплывающем окне с "Детали ингредиента"')
    def click_on_close_button_ingredient_pop_up_window(self):
        self.element_is_visible(self.locators.CLOSE_BUTTON_POP_UP_WINDOW_INGR_DETAILS).click()

    @allure.step('Проверка, что появилось всплывающее окно с "Детали ингредиента"')
    def check_ingredient_pop_up_window_is_enabled(self):
        assert self.element_is_visible(self.locators.POP_UP_WINDOW_INGR_DETAILS).is_enabled()

    @allure.step('Перетащить ингредиент в заказ')
    def drag_ingredient_to_order(self, draggable_locator):
        self.drag_and_drop_on_to_element(draggable_locator, self.locators.BURGER_CONSTRUCTOR_BASKET)

    @allure.step('Проверка, что счётчик ингредиента увеличивается')
    def check_ingredient_counter_increases(self):
        assert self.element_is_visible(self.locators.BURGER_COUNTER_INGREDIENT).text == '1'

    @allure.step('Клик по кнопке "Оформить заказ"')
    def click_on_checkout_button(self):
        self.element_is_visible(self.locators.BUTTON_CHECKOUT).click()

    @allure.step('Проверка, что появилось всплывающее окно с идентификатором заказа')
    def check_checkout_pop_up_window_is_displayed(self):
        assert self.element_is_visible(self.locators.POP_UP_ORDER_WINDOW).is_displayed()

    @allure.step('Клик по карточке заказа')
    def click_on_order_card(self):
        self.element_is_visible(self.locators.ORDER).click()

    @allure.step('Проверка, что появилось всплывающее окно с деталями по заказу')
    def check_order_pop_up_window_is_displayed(self):
        assert self.element_is_visible(self.locators.POP_UP_DETAILS_ORDER_WINDOW).is_displayed()

    @allure.step('Клик по кнопке "крестик" во всплывающем окне с "Заказ оформлен"')
    def click_on_close_button_order_pop_up_window(self):
        self.element_is_visible(self.locators.CLOSE_BUTTON_POP_UP_WINDOW_DETAILS_ORDER).click()

    @allure.step('Проверка, номера заказа в ленте заказов')
    def check_number_orders_is_in_orders_line(self):
        num_order_history = self.element_is_visible(AccountPageLocators.NUMBER_ORDER).text
        self.click_on_orders_line_button()
        num_order_line = self.element_is_visible(AccountPageLocators.NUMBER_ORDER).text
        assert num_order_history == num_order_line

    @allure.step('Получить количество текущих заказов')
    def get_counter_order_completed(self, counter_locator):
        count_orders = int(self.element_is_visible(counter_locator).text)
        return count_orders

    @allure.step('Получить номер текущего заказа во всплывающем окне')
    def get_number_order_pop_up_window(self):
        number_order = int(self.element_is_visible(self.locators.NUMBER_ORDER_POP_UP).text)
        return number_order

    @allure.step('Получить номер текущего заказа "в работе"')
    def get_number_order_in_progress(self):
        number_order = int(self.element_is_visible(self.locators.NUMBER_ORDER_IN_PROGRESS).text)
        return number_order