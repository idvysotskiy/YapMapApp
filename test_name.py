# file: test_name.py
import time
import pytest
from selenium.webdriver.common.by import By

from main_page import MainPage
from config import *
from base_page import *
import allure
from selenium import webdriver



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
        assert d.xpath(Tutorial.SKIP).get_text() == 'SKIP'
        # assert d.xpath(Tutorial.TEXT_1).get_text() == 'Are you lonely? ENTER?????'
        page.swipe('left')
        assert d.xpath(Tutorial.SKIP).get_text() == 'SKIP'
        assert d.xpath(
            Tutorial.TEXT_2).get_text() == 'You can create a group of interest. Invite friends. And to be always in the stream of life.'
        page.swipe('left')
        assert d.xpath(Tutorial.SKIP).get_text() == 'SKIP'
        assert d.xpath(Tutorial.TEXT_3).get_text() == 'Create an event and invite people to spend time together.'
        page.swipe('left')
        assert d.xpath(Tutorial.SKIP).get_text() == 'SKIP'
        assert d.xpath(Tutorial.TEXT_4).get_text() == 'Communicate. Enjoy life. Share your impressions.'
        page.swipe('left')
        time.sleep(3)
        assert d.xpath(
            Tutorial.TEXT_5).get_text() == 'And besides, your application will help you find clients in case you are running a business.'
        assert d.xpath(Tutorial.SKIP).get_text() == 'DONE'
        page.skip()
        # BasePage.get_screen(d)
        # element = d.xpath(Main.SIGNUP)
        # assert d.exists(element)
        # element = d.xpath(Main.SIGNIN)
        # assert d.exists(Main.SIGNIN)
        # BasePage.is_element_present(d, MainPage.signup)

        # BasePage.get_screen(d)

    @pytest.mark.smoke
    @allure.title("Регистрация в приложении [Sign UP]")
    @allure.testcase("Проверка регистрации в приложении (1/3 steps) - 6-8")
    @allure.step('Перейти в регистрацию, нажать назад')
    def test_signup_back(self, d):
        page = MainPage(d)
        page.skip()
        assert d.xpath(Main.SIGNUP).get_text() == 'SIGN UP'
        assert d.xpath(Main.SIGNIN).get_text() == 'SIGN IN'
        page.signup()
        assert d.xpath(Registration.CURRENT_STEP).get_text() == '1'
        assert d.xpath(Registration.ALL_STEP).get_text() == '/4'
        assert d.xpath(Registration.STEPS_TEXT).get_text() == 'STEPS'
        BasePage.get_screen(d)
        page.back()
        assert d.xpath(Main.TITLE).get_text() == 'YapMapApp'
        assert d.xpath(Main.DESCRIPTION).get_text() == 'New generation social ecosystem'
        assert d.xpath(Main.SIGNUP).get_text() == 'SIGN UP'
        assert d.xpath(Main.SIGNIN).get_text() == 'SIGN IN'

    @pytest.mark.smoke
    @allure.title("Регистрация в приложении [Sign UP]")
    @allure.testcase("Проверка регистрации в приложении (1/3 steps) - 9-12")
    @allure.step('Ввести не валидные данные в поле email')
    def test_signup_invalid_email(self, d):
        page = MainPage(d)
        page.skip()
        page.signup()
        assert d.xpath(Registration.TITLE).get_text() == 'New Account'
        page.enter_email('R2D2')
        page.signup()
        BasePage.get_screen(d)
        assert d.xpath(Registration.ERROR).get_text() == 'Email is not valid'
        page.clear_email()
        assert d.xpath(Registration.ERROR).get_text() != 'R2D2'
        page.signup()
        BasePage.get_screen(d)
        assert d.xpath(Registration.ERROR).get_text() == 'Email must be more than 3 characters'

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
        assert d.xpath(Registration.ERROR).get_text() == 'Password must be more than 8 characters'
        page.enter_password(invalid_password)
        page.click_show_pass()
        BasePage.get_screen(d)
        assert d.xpath(Registration.PASSWORD).get_text() == invalid_password
        page.signup()
        BasePage.get_screen(d)
        assert d.xpath(
            Registration.ERROR).get_text() == 'Password must be 8 to 15 characters and should contain at least one uppercase letter, lowercase, letter, digit and special character symbol.'
        page.clear_password()
        page.enter_password(valid_password)
        assert d.xpath(Registration.PASSWORD).get_text() == valid_password
        page.signup()
        BasePage.get_screen(d)
        assert d.xpath(Registration.ERROR).get_text() == 'Passwords do not match'

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
        BasePage.get_screen(d)
        assert d.xpath(Registration.PASSWORD).get_text() == valid_password
        assert d.xpath(Registration.CONFIRM_PASSWORD).get_text() == valid_password
        page.signup()
        # assert device.xpath(Registration.POPUP).get_text() == 'You must agree with terms_'
        page.click_terms_switch()
        page.signup()
        time.sleep(2)
        BasePage.get_screen(d)
        assert d.xpath(Validation.TITLE).get_text() == 'Enter Validation Code'
        assert d.xpath(Validation.DESCRIPTION).get_text() == 'You should be a receiving an email with a validation code'
        page.input_code()
        time.sleep(2)
        assert d.xpath(Validation.DESCRIPTION).get_text() == 'Invalid validation code'
        page.click_resend()
        time.sleep(30)
        assert d.xpath(Registration.CURRENT_STEP).get_text() == '2'
        assert d.xpath(Registration.ALL_STEP).get_text() == '/4'
        assert d.xpath(Registration.STEPS_TEXT).get_text() == 'STEPS'
        assert d.xpath(Registration.UPLOAD_PICTURE_TEXT) == 'Upload a profile picture'
        page.upload_profile_picture()
        page.choose_dob_under_16()

        page.click_continue()
        assert d.xpath(Registration.FIRST_NAME_ERROR) == 'First Name is required'
        page.enter_first_name('Se')
        page.click_continue()
        assert d.xpath(Registration.FIRST_NAME_ERROR) == 'First Name must be more than 3 characters'
        page.clear_first_name()
        assert d.xpath(Registration.FIRST_NAME) != 'Se'
        page.enter_first_name('Sergey')
        assert d.xpath(Registration.FIRST_NAME) == 'Sergey'
        page.click_continue()
        assert d.xpath(Registration.LAST_NAME_ERROR) == 'Last Name is required'
        page.enter_last_name('Vy')
        assert d.xpath(Registration.LAST_NAME) == 'Vy'
        page.click_continue()
        assert d.xpath(Registration.LAST_NAME_ERROR) == 'Last Name must be more than 3 characters'
        page.clear_last_name()
        assert d.xpath(Registration.LAST_NAME) != 'Vy'
        page.enter_last_name('Vysotskiy')
        assert d.xpath(Registration.LAST_NAME) == 'Vysotskiy'
        page.click_continue()
        assert d.xpath(Registration.DOB_TEXT) == 'Year - Month - Day'
        page.choose_dob_under_16()
        BasePage.get_screen(self)
        assert d.xpath(Registration.DOB_TEXT) != 'Year - Month - Day'
        # page.click_continue()
        # page.choose_gender('male')

    @pytest.mark.smoke
    @allure.title("Авторизация [Sign IN]")
    @allure.testcase("Проверка авторизации в приложении")
    def test_login(self, d):
        page = MainPage(d)
        page.skip()
        page.login(valid_email, valid_password)
