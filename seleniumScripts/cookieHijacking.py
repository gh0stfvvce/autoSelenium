from selenium import webdriver

# URL de la página a testear
url = "https://www.ejemplo.com"

# Inicializa el controlador del navegador (en este caso, Firefox)
driver = webdriver.Firefox()

try:
    # Abre la página web en el navegador
    driver.get(url)

    # Obtiene las cookies actuales
    cookies_actuales = driver.get_cookies()

    # Modifica las cookies según tus necesidades
    for cookie in cookies_actuales:
        if cookie['name'] == 'session_id':
            cookie['value'] = 'nuevo_valor'

    # Elimina todas las cookies existentes
    driver.delete_all_cookies()

    # Agrega las cookies modificadas al navegador
    for cookie in cookies_actuales:
        driver.add_cookie(cookie)

    # Recarga la página para aplicar los cambios
    driver.refresh()

finally:
    # Cierra el navegador al finalizar
    driver.quit()
