import allure
from conftest import *
from data import Urls
from pages.account_page import AccountPage
from pages.header_page import HeaderPage
from data import Text


class TestAccountPage:
    @allure.title('Проверка перехода в личный кабинет')
    def test_redirect_to_account_from_header(self, driver, login):
        ap = AccountPage(driver)
        ap.click_account_btn()
        assert ap.get_current_url() == Urls.PROFILE_PAGE

    @allure.title('Переход в раздел История заказов')
    def test_redirect_to_order_history(self, driver, login):
        ap = AccountPage(driver)
        ap.click_account_btn()
        ap.click_on_order_list()
        assert ap.get_current_url() == Urls.ORDERS_HISTORY

    @allure.title('Выход из аккаунта')
    def test_logout(self, driver, login):
        ap = AccountPage(driver)
        HeaderPage(driver).click_user_account_btn()
        ap.wait_visibility_profile_button()
        ap.click_logout_btn()
        ap.wait_visibility_enter_button()
        assert ap.get_text_enter_button() == Text.BUTTON_TEXT