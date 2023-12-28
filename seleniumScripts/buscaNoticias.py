from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class PruebasNoticias:
    def __init__(self, navegador="chrome"):
        # Configurar el navegador según la elección del usuario (predeterminado: Chrome)
        if navegador.lower() == "firefox":
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Chrome()

    def buscar_noticias_por_palabra(self, url, palabra_clave):
        self.driver.get(url)
        
        # Lógica para ingresar términos de búsqueda y hacer clic en el botón de búsqueda
        campo_busqueda = self.driver.find_element_by_name("q")
        campo_busqueda.send_keys(palabra_clave)
        campo_busqueda.send_keys(Keys.RETURN)
        
        # Esperar a que la página cargue completamente
        time.sleep(5)

        # Lógica para verificar y mostrar titulares interesantes
        titulares = self.driver.find_elements_by_class_name("titular")
        for titular in titulares:
            print(titular.text)

    def cerrar_navegador(self):
        self.driver.quit()

# Palabra clave para la búsqueda
palabra_clave = "ciberseguridad"

# Uso de la clase
url_sitio = input("Ingresa la URL del sitio web: ")
navegador_elegido = input("Elige el navegador (chrome o firefox): ")

pruebas_noticias = PruebasNoticias(navegador=navegador_elegido)
pruebas_noticias.buscar_noticias_por_palabra(url_sitio, palabra_clave)
pruebas_noticias.cerrar_navegador()
