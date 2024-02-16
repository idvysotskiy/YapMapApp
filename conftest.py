import pytest
import uiautomator2 as u2
from config import *
import allure


@allure.title("Запускаем приложение")
@pytest.fixture
def d():
    device_id = 'emulator-5554'
    device = u2.connect(device_id)
    device.app_start(package, stop=True)
    device.implicitly_wait(10.0)
    return d
