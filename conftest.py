import pytest
import uiautomator2 as u2
from config import *

@allure.title("Запускаем приложение")
@pytest.fixture
def device():
    device_id = 'emulator-5554'
    d = u2.connect(device_id)
    d.app_start(package,stop=True)
    d.implicitly_wait(10.0)
    return d



