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
        self.click(Tutorial.SKIP)

    @allure.step('Сделать свайп влево')
    def swipe(self, swipe_ext):
        self.d.swipe_ext(swipe_ext, scale=0.8)

    @allure.step('Сделать свайп вверх')
    def swipe_page(self):
        self.d.swipe_ext(Direction.HORIZ_FORWARD)

    @allure.step('Авторизоваться в приложении')
    def login(self, email, password):
        self.click(Main.SIGNIN)
        self.set_text(Authorization.EMAIL, email)
        self.set_text(Authorization.PASSWORD, password)
        BasePage.get_screen(self)
        self.click(Authorization.SIGNIN)

    @allure.step('Нажать кнопку "SIGN UP" на главном экране')
    def signup(self):
        self.click(Main.SIGNUP)

    @allure.step('Ввести email')
    def enter_email(self, email):
        self.set_text(Registration.EMAIL, email)

    @allure.step('Ввести password')
    def enter_password(self, password):
        self.set_text(Registration.PASSWORD, password)

    @allure.step('Ввести подтверждение пароля')
    def confirm_password(self, password):
        self.set_text(Registration.CONFIRM_PASSWORD, password)

    # def enter_invite_code(self, invite):
    # self.set_text(Registration.INVITE_CODE, invite)

    @allure.step('Нажать свитч "Согласиться с правилами"')
    def click_terms_switch(self):
        self.click(Registration.TETMS_SWITCH)

    @allure.step('Нажать "глаз" показать пароль')
    def click_show_pass(self):
        self.click(Registration.SHOW_PASSWORD)

    @allure.step('Нажать "глаз" показать пароль для подтверждения пароля')
    def click_show_confirm_pass(self):
        self.click(Registration.SHOW_CONFIRM_PASSWORD)

    @allure.step('Нажать кнопку [SIGN UP] на экране регистрации')
    def sign_up(self):
        self.click(Registration.SIGN_UP)

    @allure.step('Удалить текст из поля [Email]')
    def clear_email(self):
        self.d.xpath(Registration.EMAIL).click()
        self.d.clear_text()

    @allure.step('Удалить текст из поля [password]')
    def clear_password(self):
        self.d.xpath(Registration.PASSWORD).click()
        self.d.clear_text()

    def test_text(self, text):
        assert self.get_text(Validation.TITLE) == text

    # def input_valid_data_signup(self):
    #     self.device.xpath(Registration.EMAIL).
    @allure.step('Нажать кнопку "Назад"')
    def back(self):
        self.click(Main.BACK_BUTTON)

    @allure.step('Ввести проверочный код')
    def input_code(self):
        self.set_text(Validation.CODE_1, '1')
        self.set_text(Validation.CODE_2, '2')
        self.set_text(Validation.CODE_3, '3')
        self.set_text(Validation.CODE_4, '4')
        BasePage.get_screen(self)

    @allure.step('Нажать кнопку "RESEND"')
    def click_resend(self):
        self.click(Validation.RESEND)

    @allure.step('Выбрать фото профиля')
    def upload_profile_picture(self):
        self.click(Registration.UPLOAD_PICTURE)
        self.click(Registration.PERMISSION_ALLOW)
        self.click(Registration.TAKE_PICTURE_ALLOW)
        self.click(Registration.PHOTO)
        self.click(Registration.ACCEPT_PHOTO)

    @allure.step('Выбрать дату рождения 2002/02')
    def choose_dob_over_16(self):
        self.click(Registration.YEAR)
        self.click(Registration.PICK_YEAR)
        self.click(Registration.PICK_DAY)
        self.click(Registration.CALENDAR_OK)

    @allure.step('Выбрать дату рождения 2008/02')
    def choose_dob_under_16(self):
        self.click(Registration.PICK_DAY)
        self.click(Registration.CALENDAR_OK)

    @allure.step('Выбрать гендер')
    def choose_gender(self, gender):
        if gender == 'male':
            self.click(Registration.MALE)
        if gender == 'female':
            self.click(Registration.FEMALE)

    @allure.step('Нажать кнопку продолжить')
    def click_continue(self):
        self.click(Registration.CONTINUE)

    @allure.step('Заполнить поле First Name')
    def enter_first_name(self, first_name):
        self.set_text(Registration.FIRST_NAME, first_name)

    @allure.step('Заполнить поле Last Name')
    def enter_last_name(self, last_name):
        self.set_text(Registration.LAST_NAME, last_name)

    @allure.step('Удалить текст из поля [First Name]')
    def clear_first_name(self):
        self.d.xpath(Registration.FIRST_NAME).click()
        self.d.clear_text()

    @allure.step('Удалить текст из поля [Last Name]')
    def clear_last_name(self):
        self.d.xpath(Registration.LAST_NAME).click()
        self.d.clear_text()
