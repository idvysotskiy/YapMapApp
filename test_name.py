# file: test_name.py
import time
import pytest
from main_page import MainPage
from config import *
from base_page import *
import allure


# @allure.title("Чистим кеш приложения после теста")
# @pytest.fixture(autouse=True)
# def clear_app(d):
#     yield
#     d.app_clear(package)


class TestMobile:
    @pytest.mark.smoke
    @allure.title("Регистрация в приложении [Sign UP]")
    @allure.testcase("Проверка регистрации в приложении (1/3 steps) - 1-5")
    def test_tutorial(self, d):
        page = MainPage(d)
        time.sleep(5)
        page.elements_welcome_page_1()
        page.swipe('left')
        page.elements_welcome_page_2()
        page.swipe('left')
        page.elements_welcome_page_3()
        page.swipe('left')
        page.elements_welcome_page_4()
        page.swipe('left')
        time.sleep(3)
        page.elements_welcome_page_5()
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
        page.elements_main_page()
        page.signup()
        page.elements_registration_step_1()
        BasePage(d).get_screen()
        page.back()
        page.elements_main_page()

    @pytest.mark.smoke
    @allure.title("Регистрация в приложении [Sign UP]")
    @allure.testcase("Проверка регистрации в приложении (1/3 steps) - 9-12")
    @allure.step('Ввести не валидные данные в поле email')
    def test_signup_invalid_email(self, d):
        page = MainPage(d)
        page.skip()
        page.signup()
        assert BasePage(d).get_text(Registration.TITLE) == 'New Account'
        page.enter_email('R2D2')
        page.signup()
        BasePage(d).get_screen()
        assert BasePage(d).get_text(Registration.ERROR) == 'Email is not valid'
        page.clear_email()
        assert BasePage(d).get_text(Registration.ERROR) != 'R2D2'
        page.signup()
        BasePage(d).get_screen()
        assert BasePage(d).get_text(Registration.ERROR) == 'Email must be more than 3 characters'

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
        assert BasePage(d).get_text(Registration.ERROR) == 'Password must be more than 8 characters'
        page.enter_password(invalid_password)
        page.click_show_pass()
        BasePage(d).get_screen()
        assert BasePage(d).get_text(Registration.PASSWORD) == invalid_password
        page.signup()
        BasePage(d).get_screen()
        assert BasePage(d).get_text(
            Registration.ERROR) == 'Password must be 8 to 15 characters and should contain at least one uppercase letter, lowercase, letter, digit and special character symbol.'
        page.clear_password()
        page.enter_password(valid_password)
        assert BasePage(d).get_text(Registration.PASSWORD) == valid_password
        page.signup()
        BasePage(d).get_screen()
        assert BasePage(d).get_text(Registration.ERROR) == 'Passwords do not match'

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
        assert BasePage(d).get_text(Registration.PASSWORD) == valid_password
        assert BasePage(d).get_text(Registration.CONFIRM_PASSWORD) == valid_password
        page.signup()
        # assert device.xpath(Registration.POPUP).get_text() == 'You must agree with terms_'
        page.click_terms_switch()
        page.signup()
        time.sleep(2)
        BasePage(d).get_screen()
        assert BasePage(d).get_text(Validation.TITLE) == 'Enter Validation Code'
        assert BasePage(d).get_text(
            Validation.DESCRIPTION) == 'You should be a receiving an email with a validation code'
        page.input_code()
        time.sleep(2)
        assert BasePage(d).get_text(Validation.DESCRIPTION) == 'Invalid validation code'
        page.click_resend()

        time.sleep(30)  # 25
        page.elements_registration_step_2()

        page.click_continue()  # 26
        # assert BasePage(d).get_text() == 'Upload a profile picture'

        page.upload_profile_picture()  # 27
        page.choose_dob_under_16()

        page.click_continue()  # 28
        assert BasePage(d).get_text(Registration.ERROR) == 'First Name is required'

        page.enter_first_name('Se')  # 29

        page.click_continue()  # 30
        assert BasePage(d).get_text(Registration.ERROR) == 'First Name must be more than 3 characters'

        page.clear_first_name()  # 31
        assert BasePage(d).get_text(Registration.FIRST_NAME) != 'Se'

        page.enter_first_name('Sergey')
        assert BasePage(d).get_text(Registration.FIRST_NAME) == 'Sergey'

        page.click_continue()
        assert BasePage(d).get_text(Registration.ERROR) == 'Last Name is required'

        page.enter_last_name('Vy')
        assert BasePage(d).get_text(Registration.LAST_NAME) == 'Vy'

        page.click_continue()
        assert BasePage(d).get_text(Registration.ERROR) == 'Last Name must be more than 3 characters'

        page.clear_last_name()
        assert BasePage(d).get_text(Registration.LAST_NAME) != 'Vy'

        page.enter_last_name('Vysotskiy')
        assert BasePage(d).get_text(Registration.LAST_NAME) == 'Vysotskiy'

        page.click_continue()
        assert BasePage(d).get_text(Registration.DOB_TEXT) == 'Year - Month - Day'

        page.choose_dob_under_16()
        BasePage(d).get_screen()
        assert BasePage(d).get_text(Registration.DOB_TEXT) != 'Year - Month - Day'

        page.click_continue()

        # page.choose_gender('male')

    @pytest.mark.smoke
    @allure.title("Авторизация [Sign IN]")
    @allure.testcase("Проверка авторизации в приложении")
    def test_login(self, d):
        page = MainPage(d)
        page.skip()
        page.login(valid_email, valid_password)
