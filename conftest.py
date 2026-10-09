"""Cada prueba abre su navegador y lo cierra al terminar.

Si la prueba falla, la captura queda en reports/capturas/.
"""

from pathlib import Path

import pytest

from utils.configuracion import cargar_credenciales
from utils.navegador import crear_driver
from utils.saucedemo import abrir_login, iniciar_sesion

RAIZ_PROYECTO = Path(__file__).resolve().parent
CARPETA_CAPTURAS = RAIZ_PROYECTO / "reports" / "capturas"


@pytest.fixture
def credenciales():
    return cargar_credenciales()


@pytest.fixture
def driver():
    navegador = crear_driver()
    yield navegador
    navegador.quit()


@pytest.fixture
def driver_logueado(driver, credenciales):
    """Deja la sesión en el inventario. El login no lo usa: tiene que probar el ingreso."""
    abrir_login(driver, credenciales["url_base"])
    iniciar_sesion(driver, credenciales["usuario"], credenciales["contrasena"])
    return driver


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Guarda una captura en reports/capturas/ cuando la prueba falla."""
    resultado = yield
    reporte = resultado.get_result()
    if reporte.when != "call" or not reporte.failed:
        return

    navegador = item.funcargs.get("driver")
    if navegador is None:
        return

    CARPETA_CAPTURAS.mkdir(parents=True, exist_ok=True)
    destino = CARPETA_CAPTURAS / f"{item.name}.png"
    try:
        navegador.save_screenshot(str(destino))
    except Exception as error:
        print(f"No se pudo guardar la captura: {error}")
        return
    print(f"Captura del fallo: {destino.relative_to(RAIZ_PROYECTO)}")
