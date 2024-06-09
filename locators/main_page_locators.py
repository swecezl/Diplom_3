from random import randint
from selenium.webdriver.common.by import By


class MainPageLocators:
    # главная страница
    BUTTON_PERSONAL_ACCOUNT = (By.LINK_TEXT, "Личный Кабинет")  # кнопка "Личный Кабинет"
    BUTTON_ACCOUNT = (By.XPATH, "//button[text()='Войти в аккаунт']")  # кнопка "Войти в аккаунт"
    BUTTON_CONSTRUCTOR = (By.XPATH, "//p[text()='Конструктор']")  # кнопка "Конструктор"
    BUTTON_ORDERS_LINE = (By.XPATH, "//p[text()='Лента Заказов']")  # кнопка "Лента заказов"
    LOGO = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']")  # логотип "Stellar Burgers"
    TITLE_ASSEMBLE_BURGER = (By.XPATH, "//h1[text()='Соберите бургер']")  # заголовок "Собери бургер"
    TITLE_ORDERS_LINE = (By.XPATH, "//h1[text()='Лента заказов']")  # заголовок "Лента заказов"
    BURGER_INGREDIENT = (By.XPATH, f"(//a[contains(@class, 'BurgerIngredient_ingredient')])[{randint(1,15)}]")
    BURGER_INGREDIENT_BUNS = (By.XPATH, "(//a[contains(@class, 'BurgerIngredient_ingredient')])[1]")  # заголовок "Лента заказов"
    BURGER_INGREDIENT_CUTLET = (By.XPATH, "(//a[contains(@class, 'BurgerIngredient_ingredient')])[7]")
    BURGER_COUNTER_INGREDIENT = (By.XPATH, "(//p[contains(@class, 'counter__num')])[7]")
    POP_UP_WINDOW_INGR_DETAILS = (By.XPATH, "//div[contains(@class, 'Modal_modal__container')]")  # Всплывающее окно с "деталями ингредиента"
    CLOSE_BUTTON_POP_UP_WINDOW_INGR_DETAILS = (By.XPATH, "(//button[@type='button'])[1]")   # кнопка "закрыть" всплывающее окно с "деталями ингредиента"
    BURGER_CONSTRUCTOR_BASKET = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket')]") # корзина заказов
    BUTTON_CHECKOUT = (By.XPATH, "//button[text()='Оформить заказ']")  # кнопка "Оформить заказ"
    POP_UP_ORDER_WINDOW = (By.XPATH, "//div[@class='Modal_modal__container__Wo2l_']")# Всплывающее окно с "заказ оформлен"
    ORDER = (By.XPATH, "//li[contains(@class, 'OrderHistory_listItem')]") # заказ
    POP_UP_DETAILS_ORDER_WINDOW = (By.XPATH, "(//div[contains(@class,'Modal_modal__contentBox')])[2]")# Всплывающее окно "детали заказа"
    CLOSE_BUTTON_POP_UP_WINDOW_DETAILS_ORDER = (By.XPATH, "//button[contains(@class, 'Modal_modal__close_modified')]")
    COUNT_ORDERS_ALL_TIME = (By.XPATH, '(//p[contains(@class, "OrderFeed_number")])[1]')
    COUNT_ORDERS_TODAY = (By.XPATH, '(//p[contains(@class, "OrderFeed_number")])[2]')
    NUMBER_ORDER_POP_UP = (By.XPATH, '//h2[contains(@class, "Modal_modal__title_shadow")]')
    NUMBER_ORDER_IN_PROGRESS = (By.XPATH, '//ul[contains(@class,"OrderFeed_orderListReady")]/li[contains(@class, "text_type_digits")]')