# file: base_page.py
import allure
from locators import *
from config import *
import random
import string
from datetime import date
import time


class BasePage:
    def __init__(self, d):
        self.d = d

    def current_date(self):
        current_date = date.today()
        return current_date

    def generate_random_email(self):
        domain = "@yandex.ru"
        username_length = random.randint(5, 10)
        rnd_name = ''.join(random.choice(string.ascii_lowercase) for _ in range(username_length))
        username = 'yapmap.tester+'
        return username + rnd_name + domain

    def is_element_present(self, locator):
        print(self.d.xpath(locator).exists)
        assert self.d.xpath(locator).exists == True, 'Element not found!'

    def get_screen(self):
        print('screen')
        # screen = "screen.png"
        # self.d.screenshot(screen)
        # allure.attach.file(f'./{screen}', attachment_type=allure.attachment_type.PNG)

    def click(self, locator, element_name=None):
        if element_name is not None:
            with allure.step("Клик по элементу '{element_name}'"):
                self.get_element(locator).click()
        else:
            self.get_element(locator).click()

    def set_text(self, locator, text, element_name=None):
        if element_name is not None:
            with allure.step("Заполнение поля '{element_name}' текстом '{text}'"):
                self.get_element(locator).set_text(text)
        else:
            self.get_element(locator).set_text(text)

    def get_element(self, locator):
        if locator[0] == '/' and locator[1] == '/':
            return self.d.xpath(locator)
        else:
            return self.d(resourceId=locator)

    def get_text(self, locator):
        return self.get_element(locator).get_text()

    def wait_a_moment(self):
        time.sleep(0.5)

    def wait_a_second(self):
        time.sleep(1)

    def swipe_down(self):
        self.d.swipe(400, self.d.window_size()[1] / 2, 400, self.d.window_size()[1] / 4)

    @allure.step('Сделать свайп влево')
    def swipe(self, swipe_ext):
        self.d.swipe_ext(swipe_ext, scale=0.8)

    # @allure.step('Сделать свайп вверх')
    # def swipe_page(self):
    #     self.d.swipe_ext(Direction.HORIZ_FORWARD)

    def clear_text(self, locator, element_name=None):
        if element_name is not None:
            with allure.step("Удалить текст из поля '{element_name}'"):
                self.get_element(locator).click()
        else:
            self.d.clear_text()

