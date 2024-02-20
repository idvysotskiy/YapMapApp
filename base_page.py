# file: base_page.py
import allure
from locators import *
from config import *
import random
import string
from datetime import date


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
        assert self.d.xpath(locator).exists, 'Element not found!'

    def get_screen(self):
        # print('screen')
        screen = "screen.png"
        self.d.screenshot(screen)
        allure.attach.file(f'./{screen}', attachment_type=allure.attachment_type.PNG)


