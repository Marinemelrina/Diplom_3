import allure
from conftest import *
from data import Urls
from pages.account_page import AccountPage
from pages.forgot_password_page import ForgotPasswordPage
from pages.header_page import HeaderPage


class TestForgotPassword:
    @allure.title('Проверка перехода по клику на кнопку Восстановить пароль на странице логина')
    def test_click_password_reset_button(self, driver):
        fp = ForgotPasswordPage(driver)
        HeaderPage(driver).click_user_account_btn()
        AccountPage(driver).click_password_reset_btn()
        fp.click_reset_btn()
        assert fp.find_save_button().is_displayed()

    @allure.title('Переход по кнопке Восстановить после ввода почты')
    def test_enter_email_and_click_reset(self, driver, create_and_delete_user):
        fp = ForgotPasswordPage(driver)
        fp.open_page(Urls.FORGOT_PASSWORD_PAGE)
        fp.set_email_for_reset_password(create_and_delete_user[0]['email'])
        fp.click_reset_btn()
        assert fp.find_save_button().is_displayed()

    @allure.title('Проверка активности поля пароль после клика по иконке показать')
    def test_active_password_field(self, driver, create_and_delete_user):
        fp = ForgotPasswordPage(driver)
        fp.open_page(Urls.FORGOT_PASSWORD_PAGE)
        fp.set_email_for_reset_password(create_and_delete_user[0]['email'])
        fp.click_reset_btn()
        fp.find_save_button()
        fp.click_on_show_password_icon()
        assert fp.check_input_password_field()