"""Interacción con productos: alta en el carrito y verificación del ítem (clase 8)."""

from utils.saucedemo import (
    abrir_carrito,
    agregar_primer_producto,
    contador_carrito,
    items_del_carrito,
)


def test_agregar_primer_producto_incrementa_el_contador(driver_logueado):
    """El badge del carrito queda en 1 al agregar el primer producto."""
    nombre, precio = agregar_primer_producto(driver_logueado)

    assert contador_carrito(driver_logueado) == "1", (
        f"El contador del carrito no quedó en 1: {contador_carrito(driver_logueado)!r}"
    )
    print(f"Producto agregado: {nombre} | Precio: {precio}")


def test_producto_agregado_aparece_en_el_carrito(driver_logueado):
    """El producto agregado figura en cart.html con el mismo nombre y precio."""
    nombre, precio = agregar_primer_producto(driver_logueado)
    abrir_carrito(driver_logueado)

    assert "cart.html" in driver_logueado.current_url, (
        f"No se abrió el carrito. URL actual: {driver_logueado.current_url}"
    )
    items = items_del_carrito(driver_logueado)
    assert len(items) == 1, f"Se esperaba 1 ítem en el carrito y hay {len(items)}."
    assert items[0]["nombre"] == nombre, (
        f"En el carrito está {items[0]['nombre']!r} y se había agregado {nombre!r}."
    )
    assert items[0]["precio"] == precio, (
        f"El precio del carrito es {items[0]['precio']!r} y en el catálogo era {precio!r}."
    )
