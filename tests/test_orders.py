import allure
import pytest
from data import Urls
from locators.main_page_locators import MainPageLocators
from pages.account_page import AccountPage
from pages.main_page import MainPage
from pages.login_page import LoginPage


class TestOrdersLine:

    @allure.title('Проверка, если кликнуть на заказ в разделе «Лента заказов», откроется всплывающее окно с деталями')
    def test_click_on_order_open_pop_up_window_with_details_order(self, driver, login):
        main_page = MainPage(driver)
        main_page.open(Urls.URL_SB)
        main_page.click_on_login_in_account_button()
        login_page = LoginPage(driver)
        login_page.login_user(login[0], login[1])
        main_page = MainPage(driver)
        main_page.click_on_orders_line_button()
        main_page.click_on_order_card()
        main_page.check_order_pop_up_window_is_displayed()

    @pytest.mark.parametrize('ingredient_1, ingredient_2',
                             [[MainPageLocators.BURGER_INGREDIENT_BUNS, MainPageLocators.BURGER_INGREDIENT_CUTLET]])
    @allure.title('Проверка, заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_user_orders_from_order_history_display_in_order_line_page(self, driver, login, ingredient_1, ingredient_2):
        main_page = MainPage(driver)
        main_page.open(Urls.URL_SB)
        main_page.click_on_login_in_account_button()
        login_page = LoginPage(driver)
        login_page.login_user(login[0], login[1])
        main_page = MainPage(driver)
        main_page.drag_ingredient_to_order(ingredient_1)
        main_page.drag_ingredient_to_order(ingredient_2)
        main_page.click_on_checkout_button()
        main_page.click_on_close_button_order_pop_up_window()
        main_page.click_on_personal_account_button()
        account_page = AccountPage(driver)
        account_page.click_on_history_orders_button()
        main_page.check_number_orders_is_in_orders_line()

    @pytest.mark.parametrize('ingredient_1, ingredient_2, counter_orders', [
        [MainPageLocators.BURGER_INGREDIENT_BUNS, MainPageLocators.BURGER_INGREDIENT_CUTLET,
         MainPageLocators.COUNT_ORDERS_ALL_TIME],
        [MainPageLocators.BURGER_INGREDIENT_BUNS, MainPageLocators.BURGER_INGREDIENT_CUTLET,
         MainPageLocators.COUNT_ORDERS_TODAY]])
    @allure.title('Проверка, при создании нового заказа счётчик увеличиваются')
    def test_when_creating_new_order_counter_increases(self, driver, login, ingredient_1, ingredient_2, counter_orders):
        main_page = MainPage(driver)
        main_page.open(Urls.URL_SB)
        main_page.click_on_login_in_account_button()
        login_page = LoginPage(driver)
        login_page.login_user(login[0], login[1])
        main_page = MainPage(driver)
        main_page.click_on_orders_line_button()
        count_orders_before = main_page.get_counter_order_completed(counter_orders)
        main_page.click_on_constructor_button()
        main_page.drag_ingredient_to_order(ingredient_1)
        main_page.drag_ingredient_to_order(ingredient_2)
        main_page.click_on_checkout_button()
        main_page.click_on_close_button_order_pop_up_window()
        main_page.click_on_orders_line_button()
        count_orders_after = main_page.get_counter_order_completed(counter_orders)
        assert count_orders_before == count_orders_after - 1

    @pytest.mark.parametrize('ingredient_1, ingredient_2',
                             [[MainPageLocators.BURGER_INGREDIENT_BUNS, MainPageLocators.BURGER_INGREDIENT_CUTLET]])
    @allure.title('Проверка, после оформления заказа его номер появляется в разделе "В работе"')
    def test_after_placing_order_number_appears_in_progress_section(self, driver, login, ingredient_1, ingredient_2):
        main_page = MainPage(driver)
        main_page.open(Urls.URL_SB)
        main_page.click_on_login_in_account_button()
        login_page = LoginPage(driver)
        login_page.login_user(login[0], login[1])
        main_page = MainPage(driver)
        main_page.drag_ingredient_to_order(ingredient_1)
        main_page.drag_ingredient_to_order(ingredient_2)
        main_page.click_on_checkout_button()
        number_order_pop_up = main_page.get_number_order_pop_up_window()
        main_page.click_on_close_button_order_pop_up_window()
        main_page.click_on_orders_line_button()
        number_order_in_progress = main_page.get_number_order_in_progress()
        assert number_order_pop_up == number_order_in_progress