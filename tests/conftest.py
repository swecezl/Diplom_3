import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from register_new_user import register_new_user_return_login_pass_and_response
from data import Urls, Endpoints


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    driver = webdriver
    if request.param == 'chrome':
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    if request.param == 'firefox':
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def login(driver):
    login_pass, response = register_new_user_return_login_pass_and_response()
    yield login_pass
    access_token = response.json()["accessToken"]
    requests.delete(f'{Urls.URL_SB}{Endpoints.DELETE_USER}', headers={'Authorization': f'{access_token}'})