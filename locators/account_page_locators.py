from selenium.webdriver.common.by import By

class AccountPageLocators:
    ENTER_BUTTON = (By.XPATH, '//button[text()="Войти"]')  # кнопка "Войти"
    NEW_PASSWORD = (By.XPATH, '//*[@href="/forgot-password"]')  # кнопка "Восстановить пароль"
    INPUT_EMAIL = (By.XPATH, '//label[text()="Email"]/following-sibling::input')  # поле ввода почты
    INPUT_PASSWORD = (By.XPATH, '//input[@type="password"]')  # поле ввода пароля
    PROFILE = (By.XPATH, '//*[@href="/account/profile"]')  # профиль
    ORDERS_HISTORY_BUTTON = (By.XPATH, '//*[@href="/account/order-history"]')  # история заказов
    EXIT = (By.XPATH, '//*[contains(@class, "Account_button")]')  # кнопка Выход
    ORDER_HISTORY_STATUS = (By.XPATH, '//p[text()="Выполнен"]')  # статус заказа в истории
    ORDER_HISTORY_NUMBER = (By.XPATH, '//*[contains(@class,"textBox")]//p[contains(@class,"digits-default")]')  # номер заказа
