from asyncio import timeout
from calendar import calendar
from os import times, wait
import time
import self
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By

import Funcion

driver = Funcion.principal()
t = 4

# Aplicar cambios y buscar
driver.find_element(By.XPATH, "//*[@class = 'android.widget.Button' and (@text = 'Search' or . = 'Search') and @resource-id = 'com.booking:id/facet_search_box_cta']").click()
time.sleep(t)

# Elegir hotel y reservar
driver.swipe(697,2019.9,697,1894.9,0)
time.sleep(t)

driver.find_element(By.XPATH, '(//android.view.ViewGroup[@resource-id="com.booking:id/sr_hotel_card_price_view"])[2]').click()
time.sleep(t)
driver.tap([(939, 1891.9)])

#Selecionar Habitación
driver.find_element(By.XPATH, '//android.widget.TextView[@resource-id="com.booking:id/rooms_item_select_text_view"]').click()

#Seleccionar reserva
driver.find_element(By.XPATH, '//android.widget.FrameLayout[@resource-id="com.booking:id/main_action"]').click()
time.sleep(t)

#Cerrar la aplicación
driver.quit()
