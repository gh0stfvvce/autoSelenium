from selenium import webdriver

# URL de la página a testear
url = "https://www.ejemplo.com"

# Inicializa el controlador del navegador (en este caso, Firefox)
driver = webdriver.Firefox()

# Abre la página web en el navegador
driver.get(url)

try:
    # Obtiene las cookies actuales
    cookies_actuales = driver.get_cookies()

    # Manipula las cookies (por ejemplo:)
    for cookie in cookies_actuales:
        if cookie['name'] == 'usuario_id':
            cookie['value'] = 'nuevo_valor'

    # Actualiza las cookies en el navegador
    driver.delete_all_cookies()
    for cookie in cookies_actuales:
        driver.add_cookie(cookie)

    # Recarga la página para aplicar los cambios
    driver.refresh()

finally:
    # Cierra el navegador al finalizar
    driver.quit()
