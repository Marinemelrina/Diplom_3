import allure
from locators.forgot_password_locators import ForgotPasswordLocators
from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):
    @allure.step('Ввод email в поле для восстановления пароля')
    def set_email_for_reset_password(self, email):
        self.set_text_to_element(ForgotPasswordLocators.EMAIL_SELECTOR, email)

    @allure.step('Клик по кнопке "Восстановить"')
    def click_reset_btn(self):
        self.move_to_element_and_click(ForgotPasswordLocators.BUTTON_RESET)

    @allure.step('Клик по иконке Показать/скрыть пароль')
    def click_on_show_password_icon(self):
        self.click_to_visible_element(ForgotPasswordLocators.PASSWORD_BUTTON)

    @allure.step('Найти кнопку сохранить')
    def find_save_button(self):
        return self.find_element(ForgotPasswordLocators.SAVE_BUTTON)

    @allure.step('Убедиться, что поле ввода пароля активно')
    def check_input_password_field(self):
        return self.find_element(ForgotPasswordLocators.ACTIVE_FIELD_PASSWORD)