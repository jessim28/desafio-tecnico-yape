from asyncio import timeout
from calendar import calendar
from os import times, wait
import time
import self
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v85.dom import scroll_into_view_if_needed
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Configuración de Appium
desired_caps = {
    "platformName": "Android",  # Puede ser "iOS" si estás en iOS
    "deviceName": "emulator-5554",  # Nombre de tu dispositivo/emulador
    'platformVersion': '13',
    #"app": "/Users/jessicmujica/Downloads/app-debug.apk",  # Ruta de la app
    "appPackage": "com.booking",  # El paquete de la app
    "appActivity": "com.booking.startup.HomeActivity",  # Actividad principal
    "automationName": "uiautomator2"
}

desired_caps_options = UiAutomator2Options().load_capabilities(desired_caps)

# Conexión con Appium Server
driver = webdriver.Remote(command_executor="http://127.0.0.1:4723", options=desired_caps_options)

# Espera explícita para asegurar que los elementos se carguen
t=4
time.sleep(t)

# Inicia la app

# Tap en los diferentes objetos
driver.find_element(By.XPATH, "//*[@class = 'android.widget.ImageButton' and (@text = '' or . = '')]").click()
time.sleep(t)

driver.find_element(By.XPATH, "//*[@class = 'android.widget.ImageView' and @resource-id = 'com.booking:id/facet_search_box_basic_field_icon' and (@text = '' or . = '')]").click()
time.sleep(t)

# Ingresar el destino 'Cusco'
driver.find_element(By.XPATH, "//hierarchy/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.view.ViewGroup[1]/android.widget.EditText[1]").send_keys("Cusco")
time.sleep(t)

# Continuar con los taps
driver.find_element(By.XPATH, "//android.widget.ImageView").click()

# Seleccionar fechas
driver.find_element(By.XPATH, '//android.view.View[@content-desc="01 October 2024"]').click()
driver.find_element(By.XPATH, '//android.view.View[@content-desc="25 October 2024"]').click()
time.sleep(t)

driver.find_element(By.XPATH, "//*[@class = 'android.widget.Button' and (@text = 'Select dates' or . = 'Select dates') and @resource-id = 'com.booking:id/facet_date_picker_confirm']").click()
time.sleep(t)

# Modificar número de habitaciones y personas
driver.find_element(By.XPATH, "//*[@class = 'android.widget.TextView' and (@text = '1 room · 2 adults · 0 children' or . = '1 room · 2 adults · 0 children') and @resource-id = 'com.booking:id/facet_search_box_basic_field_label']").click()
time.sleep(t)

# Seleccionar edad de los niños
driver.find_element(By.XPATH, '(//android.widget.Button[@resource-id="com.booking:id/bui_input_stepper_add_button"])[3]').click()
time.sleep(t)

driver.swipe(734.9,1594.9,734.9,799.9,0)
time.sleep(t)

driver.find_element(By.XPATH, "//*[@class = 'android.widget.Button' and (@text = 'OK' or . = 'OK') and @resource-id = 'android:id/button1']").click()
time.sleep(t)

driver.find_element(By.XPATH, "//*[@class = 'android.widget.Button' and (@text = 'APPLY' or . = 'APPLY') and @resource-id = 'com.booking:id/group_config_apply_button']").click()
time.sleep(t)

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
#driver.find_element(By.XPATH, '//android.widget.Button[@resource-id="com.booking:id/main_action"]').click()

driver.find_element(By.XPATH, '//android.widget.FrameLayout[@resource-id="com.booking:id/main_action"]').click()
time.sleep(t)

#Cerrar la aplicación
driver.quit()
