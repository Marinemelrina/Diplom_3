import allure
from locators.account_page_locators import AccountPageLocators
from locators.header_locators import HeaderLocators
from pages.base_page import BasePage


class AccountPage(BasePage):
    @allure.step('Клик по кнопке "Восстановить пароль"')
    def click_password_reset_btn(self):
        self.click_to_visible_element(AccountPageLocators.NEW_PASSWORD)

    @allure.step('Клик по кнопке Личный кабинет')
    def click_account_btn(self):
        self.move_to_element_and_click(HeaderLocators.PERSONAL_ACCOUNT_BUTTON)
        self.wait_visibility_element(AccountPageLocators.PROFILE)

    @allure.step('Клик по кнопке "Выход"')
    def click_logout_btn(self):
        self.click_to_visible_element(AccountPageLocators.EXIT)

    @allure.step('Клик по кнопке "История заказов"')
    def click_on_order_list(self):
        self.click_to_visible_element(AccountPageLocators.ORDERS_HISTORY_BUTTON)

    @allure.step('Проверьте видимость кнопки профиля')
    def wait_visibility_profile_button(self):
        return self.wait_visibility_element(AccountPageLocators.PROFILE)

    @allure.step('Проверьте текст, нажав на кнопку "Войти"')
    def get_text_enter_button(self):
        return self.get_text_of_element(AccountPageLocators.ENTER_BUTTON)

    @allure.step('Проверьте видимость кнопки кнопка "Войти"')
    def wait_visibility_enter_button(self):
        self.wait_visibility_element(AccountPageLocators.ENTER_BUTTON)

    @allure.step('Получение номера заказа в "История заказов"')
    def get_order_number(self):
        return self.get_text_of_element(AccountPageLocators.ORDER_HISTORY_NUMBER)


    @allure.step('Узнать статус заказа')
    def find_order_status(self):
        return self.find_element(AccountPageLocators.ORDER_HISTORY_STATUS)

    @allure.step('Авторизация')
    def login_user(self, user_data):
        self.set_text_to_element(AccountPageLocators.INPUT_EMAIL, user_data['email'])
        self.set_text_to_element(AccountPageLocators.INPUT_PASSWORD, user_data['password'])
        self.click_to_visible_element(AccountPageLocators.ENTER_BUTTON)


