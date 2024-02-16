from base_page import BasePage
from locators import *
from config import *
from uiautomator2 import UiObject
from uiautomator2 import Direction
import allure


class MainPage(BasePage):
    def __init__(self, device):
        super().__init__(device)

    def skip(self):
        # Ожидание элемента в течение 10 секунд
        element = self.device.xpath(Tutorial.SKIP).wait(timeout=10)
        element.click()

    def test_elem(self, locator):
        elem = self.device.xpath(locator)
        assert elem.exists, f'Element {locator} not found!'

    @allure.step('Сделать свайп влево')
    def swipe(self, swipe_ext):
        self.device.swipe_ext(swipe_ext, scale=0.8)

    @allure.step('Сделать свайп вверх')
    def swipe_page(self):
        self.device.swipe_ext(Direction.HORIZ_FORWARD)

    @allure.step('Авторизоваться в приложении')
    def login(self, email, password):
        with allure.step('Нажать кнопку "Sig in" на главном экране'):
            self.device.xpath(Main.SIGNIN).click()
        with allure.step('Ввести email'):
            self.device.xpath(Authorization.EMAIL).click()
            self.device.send_keys(email)
        with allure.step('Ввести password'):
            self.device.xpath(Authorization.PASSWORD).click()
            self.device.send_keys(password)
            BasePage.get_screen(self)
        with allure.step('Нажать кнопку Sig in на экране авторизации'):
            self.device.xpath(Authorization.SIGNIN).click()

    @allure.step('Нажать кнопку "SIGN UP" на главном экране')
    def signup(self):
        element = self.device.xpath(Main.SIGNUP).wait(timeout=5)
        element.click()

    @allure.step('Ввести email')
    def enter_email(self, email):
        element = self.device.xpath(Registration.EMAIL).wait(timeout=5)
        element.click()
        self.device.send_keys(email)

    @allure.step('Ввести password')
    def enter_password(self, password):
        element = self.device.xpath(Registration.PASSWORD).wait(timeout=5)
        element.click()
        self.device.send_keys(password)

    @allure.step('Ввести подтверждение пароля')
    def confirm_password(self, password):
        element = self.device.xpath(Registration.CONFIRM_PASSWORD).wait(timeout=5)
        element.click()
        self.device.send_keys(password)

    # def enter_invite_code(self, invite):
        # self.device.xpath(Registration.INVITE_CODE).click()
        # self.device.send_keys(invite)

    @allure.step('Нажать свитч согласия с пользовательским соглашением')
    def click_terms_switch(self):
        self.device.xpath(Registration.TETMS_SWITCH).click()

    @allure.step('Нажать "глаз" показать пароль')
    def click_show_pass(self):
        self.device.xpath(Registration.SHOW_PASSWORD).click()

    @allure.step('Нажать "глаз" показать пароль для подтверждения пароля')
    def click_show_confirm_pass(self):
        self.device.xpath(Registration.SHOW_CONFIRM_PASSWORD).click()

    @allure.step('Нажать кнопку "SIGN UP" на экране регистрации')
    def sign_up(self):
        self.device.xpath(Registration.SIGN_UP).click()

    @allure.step('Очистить поле email')
    def clear_email(self):
        self.device.xpath(Registration.EMAIL).click()
        self.device.clear_text()

    @allure.step('Очистить поле password')
    def clear_password(self):
        self.device.xpath(Registration.PASSWORD).click()
        self.device.clear_text()

    def test_text(self, text):
        assert self.device.xpath(Validation.TITLE).get_text() == text

    # def input_valid_data_signup(self):
    #     self.device.xpath(Registration.EMAIL).
    @allure.step('Нажать кнопку "Назад"')
    def back(self):
        self.device.xpath(Main.BACK_BUTTON).click()

    def element_exists(self, locator):
        self.device.xpath(locator).exists(timeout=10)
