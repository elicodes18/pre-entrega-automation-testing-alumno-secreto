"""Arma el navegador y las esperas explícitas.

La consigna pide WebDriverWait. No se usa time.sleep.
"""

import os
import shutil
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as OpcionesChrome
from selenium.webdriver.firefox.options import Options as OpcionesFirefox
from selenium.webdriver.support import expected_conditions as condiciones
from selenium.webdriver.support.ui import WebDriverWait

TIEMPO_ESPERA_SEGUNDOS = 15

RUTA_CHROME = Path("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")
RUTA_BRAVE = Path("/Applications/Brave Browser.app/Contents/MacOS/Brave Browser")
RUTA_FIREFOX = Path("/Applications/Firefox.app/Contents/MacOS/firefox")


def crear_driver():
    """Abre Chrome, Brave o Firefox. Si hay Chrome, usa ese.

    NAVEGADOR=chrome|brave|firefox elige uno.
    MOSTRAR_NAVEGADOR=1 muestra la ventana. Si no está, la prueba corre sin ventana.
    """
    pedido = os.getenv("NAVEGADOR", "auto").strip().lower()
    mostrar = _quiere_ver_el_navegador()

    if pedido == "chrome":
        return _crear_chrome(mostrar, _buscar_chrome())
    if pedido == "brave":
        if not RUTA_BRAVE.exists():
            raise RuntimeError("Pediste NAVEGADOR=brave, pero Brave no está instalado.")
        return _crear_chrome(mostrar, RUTA_BRAVE)
    if pedido == "firefox":
        if not _hay_firefox():
            raise RuntimeError("Pediste NAVEGADOR=firefox, pero Firefox no está instalado.")
        return _crear_firefox(mostrar)
    if pedido != "auto":
        raise RuntimeError(
            f"NAVEGADOR='{pedido}' no es válido. Usá auto, chrome, brave o firefox."
        )

    chrome = _buscar_chrome()
    if chrome is not None:
        return _crear_chrome(mostrar, chrome)
    if RUTA_BRAVE.exists():
        return _crear_chrome(mostrar, RUTA_BRAVE)
    if _hay_firefox():
        return _crear_firefox(mostrar)
    raise RuntimeError(
        "No hay Chrome, Brave ni Firefox. Instalá uno para correr las pruebas."
    )


def esperar_visible(driver, localizador, timeout=TIEMPO_ESPERA_SEGUNDOS):
    """Espera hasta que el elemento esté visible en la página."""
    return WebDriverWait(driver, timeout).until(
        condiciones.visibility_of_element_located(localizador)
    )


def esperar_clickeable(driver, localizador, timeout=TIEMPO_ESPERA_SEGUNDOS):
    """Espera hasta que el elemento se pueda clickear."""
    return WebDriverWait(driver, timeout).until(
        condiciones.element_to_be_clickable(localizador)
    )


def esperar_url_contiene(driver, texto, timeout=TIEMPO_ESPERA_SEGUNDOS):
    """Espera hasta que la URL actual contenga el texto indicado."""
    return WebDriverWait(driver, timeout).until(condiciones.url_contains(texto))


def esperar_texto(driver, localizador, texto, timeout=TIEMPO_ESPERA_SEGUNDOS):
    """Espera hasta que el elemento contenga el texto indicado."""
    return WebDriverWait(driver, timeout).until(
        condiciones.text_to_be_present_in_element(localizador, texto)
    )


def _quiere_ver_el_navegador():
    valor = os.getenv("MOSTRAR_NAVEGADOR", "").strip().lower()
    return valor in {"1", "true", "si", "sí", "yes"}


def _buscar_chrome():
    if RUTA_CHROME.exists():
        return RUTA_CHROME
    ejecutable = shutil.which("google-chrome") or shutil.which("chromium") or shutil.which("chrome")
    if ejecutable:
        return Path(ejecutable)
    return None


def _hay_firefox():
    return RUTA_FIREFOX.exists() or shutil.which("firefox") is not None


def _crear_chrome(mostrar, binario):
    if binario is None or not Path(binario).exists():
        raise RuntimeError("Google Chrome no está instalado.")
    opciones = OpcionesChrome()
    opciones.binary_location = str(binario)
    if not mostrar:
        opciones.add_argument("--headless=new")
    opciones.add_argument("--window-size=1440,900")
    opciones.add_argument("--disable-gpu")
    opciones.add_argument("--no-sandbox")
    opciones.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=opciones)
    driver.set_window_size(1440, 900)
    return driver


def _crear_firefox(mostrar):
    opciones = OpcionesFirefox()
    if not mostrar:
        opciones.add_argument("-headless")
    if RUTA_FIREFOX.exists():
        opciones.binary_location = str(RUTA_FIREFOX)
    driver = webdriver.Firefox(options=opciones)
    driver.set_window_size(1440, 900)
    return driver
