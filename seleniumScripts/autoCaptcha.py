from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import traceback
import datetime

def realizar_automatizacion(url, tiempo_espera):
    try:
        # Inicializa el controlador del navegador (en este caso, Firefox)
        driver = webdriver.Firefox()

        # Abre la página web con captcha
        driver.get(url)

        # Espera hasta que el captcha esté presente
        WebDriverWait(driver, tiempo_espera).until(
            EC.presence_of_element_located((By.ID, "captcha-input"))
        )

        # Encuentra el elemento del captcha por su id
        captcha_element = driver.find_element(By.ID, "captcha-input")

        # Ingresa la respuesta al captcha (esto es solo un ejemplo, no real)
        captcha_element.send_keys("respuesta_del_captcha")

        # Envía la tecla Enter para enviar la respuesta
        captcha_element.send_keys(Keys.RETURN)

        # Espera hasta que se procese la respuesta al captcha
        WebDriverWait(driver, tiempo_espera).until(
            EC.invisibility_of_element_located((By.ID, "captcha-input"))
        )

    except TimeoutException:
        # Manejo de tiempo de espera excedido
        print("Error: Tiempo de espera excedido.")
        tomar_captura_de_pantalla(driver, "timeout_error")

    except NoSuchElementException:
        # Manejo de elemento no encontrado
        print("Error: Elemento no encontrado.")
        tomar_captura_de_pantalla(driver, "element_not_found")

    except Exception as e:
        # Manejo de otros errores
        print(f"Error inesperado: {str(e)}")
        tomar_captura_de_pantalla(driver, "unexpected_error")
        traceback.print_exc()

    finally:
        # Cierra el navegador al finalizar
        driver.quit()

def tomar_captura_de_pantalla(driver, nombre_archivo):
    try:
        fecha_hora_actual = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        nombre_completo = f"{nombre_archivo}_{fecha_hora_actual}.png"
        driver.save_screenshot(nombre_completo)
        print(f"Captura de pantalla guardada como: {nombre_completo}")
    except Exception as e:
        print(f"Error al tomar la captura de pantalla: {str(e)}")

# Configuración
url_ejemplo = "https://www.ejemplo.com"
tiempo_espera_ejemplo = 10  # Segundos

# Ejecuta la automatización
realizar_automatizacion(url_ejemplo, tiempo_espera_ejemplo)
