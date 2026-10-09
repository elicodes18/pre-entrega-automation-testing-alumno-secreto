"""Login en SauceDemo.

La consigna pide espera explícita y la comprobación de /inventory.html,
de Products y de Swag Labs.
"""

from utils.saucedemo import (
    abrir_login,
    iniciar_sesion,
    texto_logo,
    titulo_pagina,
    titulo_seccion,
)


def test_login_redirige_al_inventario(driver, credenciales):
    """Entra con standard_user y verifica el paso a inventory.html."""
    abrir_login(driver, credenciales["url_base"])
    iniciar_sesion(driver, credenciales["usuario"], credenciales["contrasena"])

    assert "inventory.html" in driver.current_url, (
        f"Después del login la URL no es el inventario: {driver.current_url}"
    )


def test_login_muestra_products_y_swag_labs(driver, credenciales):
    """Después del login, comprueba Products y Swag Labs."""
    abrir_login(driver, credenciales["url_base"])
    iniciar_sesion(driver, credenciales["usuario"], credenciales["contrasena"])

    assert titulo_pagina(driver) == "Swag Labs", (
        f"La pestaña no dice Swag Labs: {titulo_pagina(driver)!r}"
    )
    assert titulo_seccion(driver) == "Products", (
        f"El encabezado no dice Products: {titulo_seccion(driver)!r}"
    )
    assert texto_logo(driver) == "Swag Labs", (
        f"El logo no dice Swag Labs: {texto_logo(driver)!r}"
    )
