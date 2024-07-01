from selenium.webdriver.common.by import By

class HeaderLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, '//p[text()="Конструктор"]/parent::a')  # кнопка "Конструктор"
    ORDERS_LIST_BUTTON = (By.XPATH, '//p[text()="Лента Заказов"]/parent::a')  # кнопка "Лента Заказов"
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, '//*[@href="/account"]')  # кнопка "Личный Кабинет"