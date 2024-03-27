import time
from pages.base import BasePage
from pages.locators import ResetLocators
from tests.config import Config



class ResetPage(BasePage):
    """Создаем класс страницы "Восстановление пароля" """
    def __init__(self, driver, timeout=10):
        super().__init__(driver, timeout)
        url = Config.BASE_URL or "https://b2c.passport.rt.ru/auth/"
        driver.get(url)
        self.username = driver.find_element(*ResetLocators.AUTH_LOGIN)
        self.btn = driver.find_element(*ResetLocators.CONTINUE_BTN)

    def enter_username(self, value):
        """ Ввод логина """
        self.username.send_keys(value)

    def btn_click_continue(self):
        """ Кнопка "Продолжить" """
        self.btn.click()
        time.sleep(10)

    def get_right_elem_reset_page(self):
        """ Получаем названия табов блока восстановления пароля"""
        # Получаем названия табов
        tabs = self.find_elements(ResetLocators.RIGHT_BLOCK_TABS)
        tabs_text = "".join([x.text for x in tabs]).split('\n')
        return tabs_text

    def get_text_from_login(self):
        """ Получить текст из поля ввода логина"""
        text_login = self.find_element(ResetLocators.RESET_LOGIN_TEXT)
        return text_login.text

    def go_back_to_auth(self):
        """ Вернуться в авторизации """
        self.find_element(ResetLocators.BACK_BTN).click()

    def get_text_of_form(self):
        self.find_element()


