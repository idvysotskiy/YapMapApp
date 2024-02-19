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

    # def get_verification_code(self):
    #     '''Метод для ожидания прихода кода подтверждения на почту через протокол IMAP'''
    #     imap_server = IMAPClient('imap.yandex.ru', ssl=True)
    #     imap_server.login(valid_email_reg, app_key)
    #     imap_server.select_folder('INBOX')
    #     imap_server.idle()
    #     while True:
    #         responses = imap_server.idle_check(timeout=5)
    #         if responses:
    #             imap_server.idle_done()
    #             break
    #     messages = imap_server.search(['UNSEEN', 'FROM', 'support@yapmap.app'])
    #     if messages:
    #         latest_message_id = messages[-1]
    #         message_data = imap_server.fetch([latest_message_id], ['BODY[]'])
    #         for message in message_data.values():
    #             body = message[b'BODY[]']
    #             if body:
    #                 decoded_body = body.decode('utf-8')
    #                 pattern = r": \d{6}"
    #                 match = re.search(pattern, decoded_body)
    #                 if match:
    #                     verification_code = match.group(0)[2:]
    #                     code = str(verification_code)
    #                     print(code)
    #                     return code
    #     imap_server.logout()

    # def input_code(self):
    #     code = self.get_verification_code()
    #     print(code)
    #     self.d.xpath(Validation.CODE_1).click()
    #     self.d.send_keys(code)
    @allure.step('Ввести проверочный код')
    def input_code(self):
        self.d.xpath(Validation.CODE_1).click()
        self.d.send_keys('1')
        self.d.xpath(Validation.CODE_2).click()
        self.d.send_keys('2')
        self.d.xpath(Validation.CODE_3).click()
        self.d.send_keys('3')
        self.d.xpath(Validation.CODE_4).click()
        self.d.send_keys('4')
        BasePage.get_screen(self)

    @allure.step('Нажать кнопку "RESEND"')
    def click_resend(self):
        self.d.xpath(Validation.RESEND).click()

    @allure.step('Выбрать фото профиля')
    def upload_profile_picture(self):
        self.d.xpath(Registration.UPLOAD_PICTURE).click()
        self.d.xpath(Registration.PERMISSION_ALLOW).click()
        self.d.xpath(Registration.TAKE_PICTURE_ALLOW).click()
        self.d.xpath(Registration.PHOTO).click()
        self.d.xpath(Registration.ACCEPT_PHOTO).click()

    @allure.step('Выбрать дату рождения')
    def choose_dob(self):
        self.d.xpath(Registration.YEAR).click()
        self.d.xpath(Registration.PICK_YEAR).click()
        self.d.xpath(Registration.PICK_DAY).click()
        self.d.xpath(Registration.CALENDAR_OK).click()

    @allure.step('Выбрать гендер')
    def choose_gender(self, gender):
        if gender == 'male':
            self.d.xpath(Registration.MALE).click()
        if gender == 'female':
            self.d.xpath(Registration.FEMALE).click()

    @allure.step('Нажать кнопку продолжить')
    def click_continue(self):
        self.d.xpath(Registration.CONTINUE).click()

    @allure.step('Заполнить поле First Name')
    def enter_first_name(self, first_name):
        self.d.xpath(Registration.FIRST_NAME).click()
        self.d.send_keys(first_name)

    @allure.step('Заполнить поле Last Name')
    def enter_last_name(self, last_name):
        self.d.xpath(Registration.LAST_NAME).click()
        self.d.send_keys(last_name)







