"""Navegación y verificación del catálogo (clases 6 a 8)."""

from utils.saucedemo import (
    carrito_visible,
    filtro_visible,
    menu_visible,
    obtener_productos,
    titulo_pagina,
    titulo_seccion,
)


def test_titulo_de_inventario_es_correcto(driver_logueado):
    """El título de la pestaña es Swag Labs y el de la sección es Products."""
    assert titulo_pagina(driver_logueado) == "Swag Labs"
    assert titulo_seccion(driver_logueado) == "Products"


def test_hay_productos_visibles(driver_logueado):
    """Comprueba que haya al menos un producto visible en el inventario."""
    productos = obtener_productos(driver_logueado)
    assert len(productos) >= 1, "No se encontró ningún producto visible."


def test_menu_filtro_y_carrito_estan_visibles(driver_logueado):
    """Valida el menú, el filtro de orden y el acceso al carrito."""
    assert menu_visible(driver_logueado), "No se ve el menú lateral."
    assert filtro_visible(driver_logueado), "No se ve el filtro de productos."
    assert carrito_visible(driver_logueado), "No se ve el enlace del carrito."


def test_primer_producto_tiene_nombre_y_precio(driver_logueado):
    """Lista en el reporte el nombre y el precio del primer producto."""
    primero = obtener_productos(driver_logueado)[0]

    assert primero["nombre"], "El primer producto no tiene nombre."
    assert primero["precio"].startswith("$"), (
        f"El precio no tiene el formato esperado: {primero['precio']!r}"
    )
    print(f"Primer producto: {primero['nombre']} | Precio: {primero['precio']}")
