import pytest
from selenium import webdriver
from helpers import *
from locators.account_page_locators import AccountPageLocators
from locators.header_locators import HeaderLocators
from pages.main_page import MainPage
from pages.account_page import AccountPage
import requests
from data import Urls


@pytest.fixture(params=['chrome'])
def driver(request):
    if request.param == 'chrome':
        driver = webdriver.Chrome()
        driver.set_window_size(1920, 1080)
    driver.get(Urls.BASE_PAGE)
    yield driver
    driver.quit()


@pytest.fixture
def create_and_delete_user():

    name = generate_random_string(10)
    email = generate_random_string(10)+'@yandex.ru'
    password = generate_random_string(10)

    payload = {
        "name": name,
        "email": email,
        "password": password
    }

    login_data = payload.copy()
    del login_data["name"]
    response = requests.post(Urls.REGISTER_USER, data=payload)
    access_token = response.json()["accessToken"]
    yield login_data, access_token
    requests.delete(Urls.DELETE_USER, headers={'Authorization': access_token})


@pytest.fixture
def login(driver, create_and_delete_user):
    main_page = MainPage(driver)
    main_page.click_on_enter_btn()
    main_page.click_to_element(HeaderLocators.PERSONAL_ACCOUNT_BUTTON)
    personal_account_page = AccountPage(driver)
    personal_account_page.set_text_to_element(AccountPageLocators.INPUT_EMAIL, create_and_delete_user[0]['email'])
    personal_account_page.set_text_to_element(AccountPageLocators.INPUT_PASSWORD, create_and_delete_user[0]['password'])
    personal_account_page.click_to_visible_element(AccountPageLocators.ENTER_BUTTON)