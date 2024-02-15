import self as self

from base_page import *

# APP
package = 'com.yapmap.yapmap'
app_link = 'app_link'

# Reg valid data
valid_name_lat = "Ivan"
valid_surname_lat = 'Ivanov'
valid_name_kir = "Иван"
valid_surname_kir = 'Иванов'
valid_password = 'Qwerty1!'
valid_email = 'idgwynbleidd@gmail.com'
valid_phone = '9639447845'

rnd_email = BasePage.generate_random_email

invalid_email = 'r2d2'
invalid_password = 'Qwer'

# Промокоды (купоны):


# Номер карты                   Тип		                        Результат оплаты	Результат оплаты по токену
card_1 = 4242424242424242  # Карта Visa с 3-D Secure		    Успешный результат	Успешный результат
card_2 = 5555555555554444  # Карта Mastercard с 3-D Secure	    Успешный результат	Успешный результат
card_3 = 2200000000000004  # Карта МИР с 3-D Secure		        Успешный результат	Успешный результат
card_4 = 4012888888881881  # Карта Visa с 3-D Secure		    Недостаточно средств на карте
card_5 = 5105105105105100  # Карта Mastercard с 3-D Secure	    Недостаточно средств на карте
card_6 = 2202202202202200  # Карта МИР с 3-D Secure		        Недостаточно средств на карте
card_7 = 4000000000003055  # Карта Visa без 3-D Secure		    Успешный результат	Успешный результат
card_8 = 5205000000003055  # Карта Mastercard без 3-D Secure	Успешный результат	Успешный результат
card_9 = 2202000000003055  # Карта МИР без 3-D Secure		    Успешный результат	Успешный результат
card_10 = 4111111111111111  # Карта Visa без 3-D Secure		    Успешный результат	Недостаточно средств на карте
card_11 = 5200828282828210  # Карта Mastercard без 3-D Secure	Успешный результат	Недостаточно средств на карте
card_12 = 2200000022222222  # Карта МИР без 3-D Secure		    Успешный результат	Недостаточно средств на карте
card_13 = 4000056655665556  # Карта Visa без 3-D Secure		    Недостаточно средств на карте
card_14 = 5404000000000043  # Карта Mastercard без 3-D Secure	Недостаточно средств на карте
card_15 = 2203000000000043  # Карта МИР без 3-D Secure		    Недостаточно средств на карте


