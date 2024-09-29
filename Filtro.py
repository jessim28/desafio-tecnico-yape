from asyncio import timeout
from calendar import calendar
from lib2to3.pgen2.driver import Driver
from os import times, wait
import time
from selenium.webdriver.common.by import By

import Funcion

driver = Funcion.principal()
t = 4

# Aplicar cambios y buscar
driver.find_element(By.XPATH, "//*[@class = 'android.widget.Button' and (@text = 'Search' or . = 'Search') and @resource-id = 'com.booking:id/facet_search_box_cta']").click()
time.sleep(t)

#Clasificacion por precio
driver.find_element(By.XPATH, '//android.widget.FrameLayout[@resource-id="com.booking:id/sr_topbar_frame"]/android.widget.LinearLayout/android.view.ViewGroup[1]').click()

driver.find_element(By.XPATH, '//android.widget.CheckedTextView[@text="Price (low to high)"]').click()
time.sleep(t)

#Filtro por precio
driver.find_element(By.XPATH, '//android.widget.TextView[@resource-id="com.booking:id/toolbar_item_label" and @text="Filter"]').click()
time.sleep(t)

driver.find_element(By.XPATH, '//android.widget.TextView[@resource-id="com.booking:id/text" and @text="US$0 - US$1,200 ⁦(311)"]').click()
time.sleep(t)

#Cerrar la aplicación
driver.quit()