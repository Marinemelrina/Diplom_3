from selenium.webdriver.common.by import By

class ForgotPasswordLocators:
    BUTTON_RESET = (By.XPATH, '//button[text()="Восстановить"]')  # кнопка "Восстановить"
    SAVE_BUTTON = (By.XPATH, '//button[text()="Сохранить"]')  # кнопка "Сохранить"
    PASSWORD_BUTTON = (By.XPATH, '//div[contains(@class,"icon-action")]')  # кнопка "Показать пароль"
    EMAIL_SELECTOR = (By.XPATH, '//label[text()="Email"]/following-sibling::input')  # поле ввода почты
    INPUT_PASSWORD = (By.XPATH, '//input[@type="password"]')  # поле ввода пароля
    ACTIVE_FIELD_PASSWORD = (By.CSS_SELECTOR, '.input.input_status_active')  # активное поле пароль