import allure
from conftest import *
from pages.header_page import HeaderPage
from data import Urls


class TestHeaderPage:
    @allure.title('Проверка перехода в "Конструктор" по клику')
    def test_redirect_to_constructor(self, driver):
        header_page = HeaderPage(driver)
        header_page.click_orders_list_btn()
        header_page.click_constructor_btn()
        current_url = header_page.get_current_url()
        assert current_url == Urls.BASE_PAGE


    @allure.title('Проверка перехода в Ленту заказов по клику')
    def test_redirect_to_order_list(self, driver):
        header_page = HeaderPage(driver)
        header_page.click_orders_list_btn()
        current_url = header_page.get_current_url()
        assert current_url == Urls.FEED