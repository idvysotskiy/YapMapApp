# file: test_name.py
import time
import pytest
from main_page import MainPage
from config import *
from base_page import *
import allure


@allure.title("Чистим кеш приложения после теста")
@pytest.fixture(autouse=True)
def clear_app(device):
    yield
    device.app_clear(package)


class TestMobile:
    @pytest.mark.smoke
    @allure.title("Регистрация в приложении [Sign UP]")
    @allure.testcase("Проверка регистрации в приложении (1/3 steps)")
    def test_tutorial(self, device):
        page = MainPage(device)
        time.sleep(5)
        assert device.xpath(Tutorial.SKIP).get_text() == 'SKIP'
        # assert device.xpath(//*[contains( @ text, 'Se')])
        page.swipe('left')
        page.swipe('left')
        page.swipe('left')
        page.swipe('left')
        page.skip()
        BasePage.get_screen(device)

    @pytest.mark.smoke
    @allure.title("Регистрация в приложении [Sign UP]")
    @allure.testcase("Проверка регистрации в приложении (1/3 steps)")
    @allure.step('Перейти в регистрацию, нажать назад')
    def test_signup_back(self, device):
        page = MainPage(device)
        page.skip()
        page.signup()
        BasePage.get_screen(device)
        page.back()

    @pytest.mark.smoke
    @allure.title("Регистрация в приложении [Sign UP]")
    @allure.testcase("Проверка регистрации в приложении (1/3 steps)")
    @allure.step('Ввести не валидные данные в поле email')
    def test_signup_invalid_email(self, device):
        page = MainPage(device)
        page.skip()
        page.signup()
        page.enter_email('R2D2')
        page.signup()
        BasePage.get_screen(device)
        assert device.xpath(Registration.ERROR).get_text() == 'Email is not valid'
        page.clear_email()
        page.signup()
        BasePage.get_screen(device)
        assert device.xpath(Registration.ERROR).get_text() == 'Email must be more than 3 characters'

    @pytest.mark.smoke
    @allure.title("Регистрация в приложении [Sign UP]")
    @allure.testcase("Проверка регистрации в приложении (1/3 steps)")
    @allure.step('Ввести не валидные данные в поле password')
    def test_signup_invalid_password(self, device):
        page = MainPage(device)
        page.skip()
        page.signup()
        page.enter_email(BasePage.generate_random_email(device))
        page.signup()
        page.enter_password(invalid_password)
        page.click_show_pass()
        BasePage.get_screen(device)
        assert device.xpath(Registration.PASSWORD).get_text() == invalid_password
        page.signup()
        BasePage.get_screen(device)
        assert device.xpath(Registration.ERROR).get_text() == 'Password must be more than 8 characters'
        page.clear_password()
        page.enter_password(valid_password)
        page.signup()
        BasePage.get_screen(device)
        assert device.xpath(Registration.ERROR).get_text() == 'Passwords do not match'

    @pytest.mark.smoke
    @allure.title("Регистрация в приложении [Sign UP]")
    @allure.testcase("Проверка регистрации в приложении (1/3 steps)")
    @allure.step('Ввести валидные данные в поле password')
    def test_signup_valid_password(self, device):
        page = MainPage(device)
        page.skip()
        page.signup()
        page.enter_email(BasePage.generate_random_email(device))
        page.confirm_password(valid_password)
        page.click_show_confirm_pass()
        BasePage.get_screen(device)
        assert device.xpath(Registration.CONFIRM_PASSWORD).get_text() == valid_password
        page.signup()
        # assert device.xpath(Registration.POPUP).get_text() == 'You must agree with terms'
        page.click_terms_switch()
        page.signup()
        time.sleep(5)
        BasePage.get_screen(device)
        assert device.xpath(Validation.TITLE).get_text() == 'Enter Validation Code'
        assert device.xpath(
            Validation.DESCRIPTION).get_text() == 'You should be a receiving an email with a validation code'

        # page.enter_signup_data(valid_email, valid_password)

    @pytest.mark.smoke
    @allure.title("Авторизация [Sign IN]")
    @allure.testcase("Проверка авторизации в приложении")
    def test_login(self, device):
        page = MainPage(device)
        page.skip()
        page.login(valid_email, valid_password)
