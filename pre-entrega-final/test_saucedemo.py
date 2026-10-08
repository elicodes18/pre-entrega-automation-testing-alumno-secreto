"""Punto de entrada que pide la consigna para el reporte HTML.

Los casos están en tests/ y las acciones en utils/. Este archivo los
reúne para poder correr:

    pytest pre-entrega-final/test_saucedemo.py -v --html=reporte.html --self-contained-html
"""

from tests.test_carrito import (
    test_agregar_primer_producto_incrementa_el_contador as _agregar,
)
from tests.test_carrito import (
    test_producto_agregado_aparece_en_el_carrito as _en_carrito,
)
from tests.test_catalogo import test_hay_productos_visibles as _hay_productos
from tests.test_catalogo import (
    test_menu_filtro_y_carrito_estan_visibles as _interfaz,
)
from tests.test_catalogo import (
    test_primer_producto_tiene_nombre_y_precio as _primer_producto,
)
from tests.test_catalogo import test_titulo_de_inventario_es_correcto as _titulo
from tests.test_login import (
    test_login_muestra_products_y_swag_labs as _login_textos,
)
from tests.test_login import test_login_redirige_al_inventario as _login_url


def test_login_redirige_al_inventario(driver, credenciales):
    """Ingresa con standard_user y comprueba la redirección a inventory.html."""
    _login_url(driver, credenciales)


def test_login_muestra_products_y_swag_labs(driver, credenciales):
    """Valida el encabezado Products y la marca Swag Labs después del login."""
    _login_textos(driver, credenciales)


def test_titulo_de_inventario_es_correcto(driver_logueado):
    """El título de la pestaña es Swag Labs y el de la sección es Products."""
    _titulo(driver_logueado)


def test_hay_productos_visibles(driver_logueado):
    """Comprueba que haya al menos un producto visible en el inventario."""
    _hay_productos(driver_logueado)


def test_menu_filtro_y_carrito_estan_visibles(driver_logueado):
    """Valida el menú, el filtro de orden y el acceso al carrito."""
    _interfaz(driver_logueado)


def test_primer_producto_tiene_nombre_y_precio(driver_logueado):
    """Lista en el reporte el nombre y el precio del primer producto."""
    _primer_producto(driver_logueado)


def test_agregar_primer_producto_incrementa_el_contador(driver_logueado):
    """El badge del carrito queda en 1 al agregar el primer producto."""
    _agregar(driver_logueado)


def test_producto_agregado_aparece_en_el_carrito(driver_logueado):
    """El producto agregado figura en cart.html con el mismo nombre y precio."""
    _en_carrito(driver_logueado)
