# file: test_name.py
import time
import pytest
from main_page import MainPage
from config import *
from base_page import *
import allure


@allure.title("Чистим кеш приложения после теста")
@pytest.fixture(autouse=True)
def clear_app(d):
    yield
    d.app_clear(package)


class TestMobile:
    @pytest.mark.smoke
    @allure.title("Регистрация в приложении [Sign UP]")
    @allure.testcase("Проверка регистрации в приложении (1/3 steps) - 1-5")
    def test_tutorial(self, d):
        page = MainPage(d)
        time.sleep(5)
        assert BasePage.get_text(d, Tutorial.SKIP) == 'SKIP'
        # assert d.xpath(Tutorial.TEXT_1).get_text() == 'Are you lonely? ENTER?????'
        page.swipe('left')
        assert BasePage.get_text(d, Tutorial.SKIP) == 'SKIP'
        assert BasePage.get_text(d, Tutorial.TEXT_2) == 'You can create a group of interest. Invite friends. And to be always in the stream of life.'
        page.swipe('left')
        assert BasePage.get_text(d, Tutorial.SKIP) == 'SKIP'
        assert BasePage.get_text(d, Tutorial.TEXT_3) == 'Create an event and invite people to spend time together.'
        page.swipe('left')
        assert BasePage.get_text(d, Tutorial.SKIP) == 'SKIP'
        assert BasePage.get_text(d, Tutorial.TEXT_4) == 'Communicate. Enjoy life. Share your impressions.'
        page.swipe('left')
        time.sleep(3)
        assert BasePage.get_text(d, Tutorial.TEXT_5) == 'And besides, your application will help you find clients in case you are running a business.'
        assert BasePage.get_text(d, Tutorial.SKIP) == 'DONE'
        BasePage.get_screen(d)
        page.skip()


    @pytest.mark.smoke
    @allure.title("Регистрация в приложении [Sign UP]")
    @allure.testcase("Проверка регистрации в приложении (1/3 steps) - 6-8")
    @allure.step('Перейти в регистрацию, нажать назад')
    def test_signup_back(self, d):
        page = MainPage(d)
        page.skip()
        time.sleep(2)
        assert BasePage.get_text(d, Main.SIGNUP).get_text() == 'SIGN UP'
        assert BasePage.get_text(d, Main.SIGNIN).get_text() == 'SIGN IN'
        page.signup()
        assert BasePage.get_text(d, Registration.CURRENT_STEP) == '1'
        assert BasePage.get_text(d, Registration.ALL_STEP) == '/4'
        assert BasePage.get_text(d, Registration.STEPS_TEXT) == 'STEPS'
        BasePage(d).get_screen()
        page.back()
        assert BasePage.get_text(d, Main.TITLE) == 'YapMapApp'
        assert BasePage.get_text(d, Main.DESCRIPTION) == 'New generation social ecosystem'
        assert BasePage.get_text(d, Main.SIGNUP) == 'SIGN UP'
        assert BasePage.get_text(d, Main.SIGNIN) == 'SIGN IN'

    @pytest.mark.smoke
    @allure.title("Регистрация в приложении [Sign UP]")
    @allure.testcase("Проверка регистрации в приложении (1/3 steps) - 9-12")
    @allure.step('Ввести не валидные данные в поле email')
    def test_signup_invalid_email(self, d):
        page = MainPage(d)
        page.skip()
        page.signup()
        assert BasePage.get_text(d, Registration.TITLE) == 'New Account'
        page.enter_email('R2D2')
        page.signup()
        BasePage(d).get_screen()
        assert BasePage.get_text(d, Registration.ERROR) == 'Email is not valid'
        page.clear_email()
        assert BasePage.get_text(d, Registration.ERROR) != 'R2D2'
        page.signup()
        BasePage(d).get_screen()
        assert BasePage.get_text(d, Registration.ERROR) == 'Email must be more than 3 characters'

    @pytest.mark.smoke
    @allure.title("Регистрация в приложении [Sign UP]")
    @allure.testcase("Проверка регистрации в приложении (1/3 steps) - 13-18")
    @allure.step('Ввести не валидные данные в поле password')
    def test_signup_invalid_password(self, d):
        page = MainPage(d)
        page.skip()
        page.signup()
        page.enter_email(BasePage.generate_random_email(d))
        page.signup()
        assert BasePage.get_text(d, Registration.ERROR) == 'Password must be more than 8 characters'
        page.enter_password(invalid_password)
        page.click_show_pass()
        BasePage(d).get_screen()
        assert BasePage.get_text(d, Registration.PASSWORD) == invalid_password
        page.signup()
        BasePage(d).get_screen()
        assert BasePage.get_text(d, Registration.ERROR) == 'Password must be 8 to 15 characters and should contain at least one uppercase letter, lowercase, letter, digit and special character symbol.'
        page.clear_password()
        page.enter_password(valid_password)
        assert BasePage.get_text(d, Registration.PASSWORD) == valid_password
        page.signup()
        BasePage(d).get_screen()
        assert BasePage.get_text(d, Registration.ERROR) == 'Passwords do not match'

    @pytest.mark.smoke
    @allure.title("Регистрация в приложении [Sign UP]")
    @allure.testcase("Проверка регистрации в приложении (1/3 steps) - 19-22")
    @allure.step('Ввести валидные данные в поле password')
    def test_signup_valid_password(self, d):
        page = MainPage(d)
        page.skip()
        page.signup()
        page.enter_email(BasePage.generate_random_email(d))
        page.enter_password(valid_password)
        page.click_show_pass()
        page.confirm_password(valid_password)
        page.click_show_confirm_pass()
        BasePage(d).get_screen()
        assert BasePage.get_text(d, Registration.PASSWORD) == valid_password
        assert BasePage.get_text(d, Registration.CONFIRM_PASSWORD) == valid_password
        page.signup()
        # assert device.xpath(Registration.POPUP).get_text() == 'You must agree with terms_'
        page.click_terms_switch()
        page.signup()
        time.sleep(2)
        BasePage(d).get_screen()
        assert BasePage.get_text(d, Validation.TITLE) == 'Enter Validation Code'
        assert BasePage.get_text(d, Validation.DESCRIPTION) == 'You should be a receiving an email with a validation code'
        page.input_code()
        time.sleep(2)
        assert BasePage.get_text(d, Validation.DESCRIPTION) == 'Invalid validation code'
        page.click_resend()
        time.sleep(30)
        assert BasePage.get_text(d, Registration.CURRENT_STEP) == '2'
        assert BasePage.get_text(d, Registration.ALL_STEP) == '/4'
        assert BasePage.get_text(d, Registration.STEPS_TEXT) == 'STEPS'
        assert BasePage.get_text(d, Registration.UPLOAD_PICTURE_TEXT) == 'Upload a profile picture'
        page.upload_profile_picture()
        page.choose_dob_under_16()

        page.click_continue()
        assert BasePage.get_text(d, Registration.ERROR) == 'First Name is required'
        page.enter_first_name('Se')
        page.click_continue()
        assert BasePage.get_text(d, Registration.ERROR) == 'First Name must be more than 3 characters'
        page.clear_first_name()
        assert BasePage.get_text(d, Registration.FIRST_NAME) != 'Se'
        page.enter_first_name('Sergey')
        assert BasePage.get_text(d, Registration.FIRST_NAME) == 'Sergey'
        page.click_continue()
        assert BasePage.get_text(d, Registration.ERROR) == 'Last Name is required'
        page.enter_last_name('Vy')
        assert BasePage.get_text(d, Registration.LAST_NAME) == 'Vy'
        page.click_continue()
        assert BasePage.get_text(d, Registration.ERROR) == 'Last Name must be more than 3 characters'
        page.clear_last_name()
        assert BasePage.get_text(d, Registration.LAST_NAME) != 'Vy'
        page.enter_last_name('Vysotskiy')
        assert BasePage.get_text(d, Registration.LAST_NAME) == 'Vysotskiy'
        page.click_continue()
        assert BasePage.get_text(d, Registration.DOB_TEXT) == 'Year - Month - Day'
        page.choose_dob_under_16()
        BasePage(d).get_screen()
        assert BasePage.get_text(d, Registration.DOB_TEXT) != 'Year - Month - Day'
        # page.click_continue()
        # page.choose_gender('male')

    @pytest.mark.smoke
    @allure.title("Авторизация [Sign IN]")
    @allure.testcase("Проверка авторизации в приложении")
    def test_login(self, d):
        page = MainPage(d)
        BasePage(d).is_element_present(Main.BACK_BUTTON)
        page.skip()
        page.login(valid_email, valid_password)
