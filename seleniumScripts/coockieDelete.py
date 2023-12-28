from selenium import webdriver

# URL de la página a testear
url = "https://www.ejemplo.com"

# Inicializa el controlador del navegador (en este caso, Firefox)
driver = webdriver.Firefox()

try:
    # Abre la página web en el navegador
    driver.get(url)

    # Elimina todas las cookies
    driver.delete_all_cookies()

    # Recarga la página para aplicar los cambios
    driver.refresh()

finally:
    # Cierra el navegador al finalizar
    driver.quit()
