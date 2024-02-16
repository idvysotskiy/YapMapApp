# file: base_page.py
import allure
from locators import *
from config import *
import random
import string


class BasePage:
    def __init__(self, d):
        self.d = d

    def generate_random_email(self):
        domain = "@example.com"
        username_length = random.randint(5, 10)
        username = ''.join(random.choice(string.ascii_lowercase) for _ in range(username_length))
        return username + domain

    def is_element_present(self, locator):
        assert self.d.xpath(locator).exists, 'Element not found!'

    def get_screen(self):
        screen = "screen.png"
        self.d.screenshot(screen)
        allure.attach.file(f'./{screen}', attachment_type=allure.attachment_type.PNG)


