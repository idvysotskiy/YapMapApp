from base_page import BasePage
from locators import *
from config import *
from uiautomator2 import UiObject
from uiautomator2 import Direction
import allure


class MainPage(BasePage):
    def __init__(self, d):
        super().__init__(d)

    @allure.step('Нажать кнопку "Done/Skip"')
    def skip(self):
        # Ожидание элемента в течение 10 секунд
        element = self.d.xpath(Tutorial.SKIP).wait(timeout=10)
        element.click()

    def test_elem(self, locator):
        elem = self.d.xpath(locator)
        assert elem.exists, f'Element {locator} not found!'

    @allure.step('Сделать свайп влево')
    def swipe(self, swipe_ext):
        self.d.swipe_ext(swipe_ext, scale=0.8)

    @allure.step('Сделать свайп вверх')
    def swipe_page(self):
        self.d.swipe_ext(Direction.HORIZ_FORWARD)

    @allure.step('Авторизоваться в приложении')
    def login(self, email, password):
        with allure.step('Нажать кнопку "Sig in" на главном экране'):
            self.d.xpath(Main.SIGNIN).click()
        with allure.step(f'Ввести в поле email: {email}'):
            self.d.xpath(Authorization.EMAIL).click()
            self.d.send_keys(email)
        with allure.step(f'Ввести в поле password: {password}'):
            self.d.xpath(Authorization.PASSWORD).click()
            self.d.send_keys(password)
            BasePage.get_screen(self)
        with allure.step('Нажать кнопку Sig in на экране авторизации'):
            self.d.xpath(Authorization.SIGNIN).click()

    @allure.step('Нажать кнопку "SIGN UP" на главном экране')
    def signup(self):
        element = self.d.xpath(Main.SIGNUP).wait(timeout=5)
        element.click()

    @allure.step('Ввести email')
    def enter_email(self, email):
        element = self.d.xpath(Registration.EMAIL).wait(timeout=5)
        element.click()
        self.d.send_keys(email)

    @allure.step('Ввести password')
    def enter_password(self, password):
        element = self.d.xpath(Registration.PASSWORD).wait(timeout=5)
        element.click()
        self.d.send_keys(password)

    @allure.step('Ввести подтверждение пароля')
    def confirm_password(self, password):
        element = self.d.xpath(Registration.CONFIRM_PASSWORD).wait(timeout=5)
        element.click()
        self.d.send_keys(password)

    # def enter_invite_code(self, invite):
        # self.device.xpath(Registration.INVITE_CODE).click()
        # self.device.send_keys(invite)

    @allure.step('Нажать свитч "Согласиться с правилами"')
    def click_terms_switch(self):
        self.d.xpath(Registration.TETMS_SWITCH).click()

    @allure.step('Нажать "глаз" показать пароль')
    def click_show_pass(self):
        self.d.xpath(Registration.SHOW_PASSWORD).click()

    @allure.step('Нажать "глаз" показать пароль для подтверждения пароля')
    def click_show_confirm_pass(self):
        self.d.xpath(Registration.SHOW_CONFIRM_PASSWORD).click()

    @allure.step('Нажать кнопку [SIGN UP] на экране регистрации')
    def sign_up(self):
        self.d.xpath(Registration.SIGN_UP).click()

    @allure.step('Удалить текст из поля [Email]')
    def clear_email(self):
        self.d.xpath(Registration.EMAIL).click()
        self.d.clear_text()

    @allure.step('Удалить текст из поля [password]')
    def clear_password(self):
        self.d.xpath(Registration.PASSWORD).click()
        self.d.clear_text()

    def test_text(self, text):
        assert self.d.xpath(Validation.TITLE).get_text() == text

    # def input_valid_data_signup(self):
    #     self.device.xpath(Registration.EMAIL).
    @allure.step('Нажать кнопку "Назад"')
    def back(self):
        self.d.xpath(Main.BACK_BUTTON).click()

    def element_exists(self, locator):
        self.d.xpath(locator).exists(timeout=10)
