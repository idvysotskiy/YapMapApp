# file: base_page.py
import allure

from locators import *
from config import *
import random
import string


# class InstallAPK:
#     def __init__(self, device):
#         self.device = device
#
#     def clear_app_data(self):
#         self.device.app_stop(package)
#         self.device.app_clear(package)
#
#     def install_app(self):
#         self.device.app_install(app_link)
#
#     def remove_app(self):
#         self.device.app_uninstall(package)
#
#     def stop_app(self):
#         self.device.app_stop(package)


class BasePage:
    def __init__(self, device):
        self.device = device

    # def find_element_by_text(self, element_text):
    # self.device.xpath(//*[@text=element_text])

    def generate_random_email(self):
        domain = "@example.com"
        username_length = random.randint(5, 10)
        username = ''.join(random.choice(string.ascii_lowercase) for _ in range(username_length))
        return username + domain

    def is_element_present(self, locator):
        assert self.device.xpath(locator).exists, 'Element not found!'

    def get_screen(self):
        screen = "screen.png"
        self.device.screenshot(screen)
        allure.attach.file(f'./{screen}', attachment_type=allure.attachment_type.PNG)


