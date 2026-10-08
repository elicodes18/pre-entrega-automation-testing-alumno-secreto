"""Automatización de login.

Criterio mínimo: espera explícita y validación de /inventory.html y de
Products / Swag Labs.
"""

from utils.saucedemo import (
    abrir_login,
    iniciar_sesion,
    texto_logo,
    titulo_pagina,
    titulo_seccion,
)


def test_login_redirige_al_inventario(driver, credenciales):
    """Ingresa con standard_user y comprueba la redirección a inventory.html."""
    abrir_login(driver, credenciales["url_base"])
    iniciar_sesion(driver, credenciales["usuario"], credenciales["contrasena"])

    assert "inventory.html" in driver.current_url, (
        f"El login no redirigió al inventario. URL actual: {driver.current_url}"
    )


def test_login_muestra_products_y_swag_labs(driver, credenciales):
    """Valida el encabezado Products y la marca Swag Labs después del login."""
    abrir_login(driver, credenciales["url_base"])
    iniciar_sesion(driver, credenciales["usuario"], credenciales["contrasena"])

    assert titulo_pagina(driver) == "Swag Labs", (
        f"El título de la pestaña no es Swag Labs: {titulo_pagina(driver)!r}"
    )
    assert titulo_seccion(driver) == "Products", (
        f"El encabezado del inventario no es Products: {titulo_seccion(driver)!r}"
    )
    assert texto_logo(driver) == "Swag Labs", (
        f"El logo no dice Swag Labs: {texto_logo(driver)!r}"
    )
