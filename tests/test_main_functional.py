import allure
import pytest
from data import Urls
from pages.main_page import MainPage
from pages.login_page import LoginPage
from locators.main_page_locators import MainPageLocators


class TestMainFunctional:

    @allure.title('Проверка перехода по клику на «Конструктор»')
    def test_go_to_constructor_by_click_constructor_button(self, driver, login):
        main_page = MainPage(driver)
        main_page.open(Urls.URL_SB)
        main_page.click_on_login_in_account_button()
        login_page = LoginPage(driver)
        login_page.login_user(login[0], login[1])
        main_page = MainPage(driver)
        main_page.click_on_constructor_button()
        main_page.check_title_assemble_burger_is_displayed()

    @allure.title('Проверка перехода по клику на «Лента заказов»')
    def test_go_to_orders_line_by_click_orders_line_button(self, driver, login):
        main_page = MainPage(driver)
        main_page.open(Urls.URL_SB)
        main_page.click_on_login_in_account_button()
        login_page = LoginPage(driver)
        login_page.login_user(login[0], login[1])
        main_page = MainPage(driver)
        main_page.click_on_orders_line_button()
        main_page.check_title_orders_line_is_displayed()

    @allure.title('Проверка, если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_click_on_ingredient_pop_up_window_appear_with_details(self, driver, login):
        main_page = MainPage(driver)
        main_page.open(Urls.URL_SB)
        main_page.click_on_login_in_account_button()
        login_page = LoginPage(driver)
        login_page.login_user(login[0], login[1])
        main_page = MainPage(driver)
        main_page.click_on_burger_ingredient()
        main_page.check_ingredient_pop_up_window_is_displayed()

    @allure.title('Проверка, всплывающее окно с деталями закрывается кликом по крестику')
    def test_ingredient_pop_up_window_closed_on_click_close_button(self, driver, login):
        main_page = MainPage(driver)
        main_page.open(Urls.URL_SB)
        main_page.click_on_login_in_account_button()
        login_page = LoginPage(driver)
        login_page.login_user(login[0], login[1])
        main_page = MainPage(driver)
        main_page.click_on_burger_ingredient()
        main_page.click_on_close_button_ingredient_pop_up_window()
        main_page.check_ingredient_pop_up_window_is_enabled()

    @allure.title('Проверка, при добавлении ингредиента в заказ счётчик этого ингредиента увеличивается')
    def test_add_ingredient_to_order_counter_for_ingredient_increases(self, driver, login):
        main_page = MainPage(driver)
        main_page.open(Urls.URL_SB)
        main_page.click_on_login_in_account_button()
        login_page = LoginPage(driver)
        login_page.login_user(login[0], login[1])
        main_page = MainPage(driver)
        main_page.drag_ingredient_to_order(MainPageLocators.BURGER_INGREDIENT_CUTLET)
        main_page.check_ingredient_counter_increases()

    @pytest.mark.parametrize('ingredient_1, ingredient_2',
                             [[MainPageLocators.BURGER_INGREDIENT_BUNS, MainPageLocators.BURGER_INGREDIENT_CUTLET]])
    @allure.title('Проверка, залогиненный пользователь может оформить заказ')
    def test_login_user_can_place_order(self, driver, login, ingredient_1, ingredient_2):
        main_page = MainPage(driver)
        main_page.open(Urls.URL_SB)
        main_page.click_on_login_in_account_button()
        login_page = LoginPage(driver)
        login_page.login_user(login[0], login[1])
        main_page = MainPage(driver)
        main_page.drag_ingredient_to_order(ingredient_1)
        main_page.drag_ingredient_to_order(ingredient_2)
        main_page.click_on_checkout_button()
        main_page.check_checkout_pop_up_window_is_displayed()