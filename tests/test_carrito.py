"""Interacción con productos (clase 8): agregar al carrito y verificar el ítem."""

from utils.saucedemo import (
    abrir_carrito,
    agregar_primer_producto,
    contador_carrito,
    items_del_carrito,
)


def test_agregar_primer_producto_incrementa_el_contador(driver_logueado):
    """Al agregar el primer producto, el contador del carrito queda en 1."""
    nombre, precio = agregar_primer_producto(driver_logueado)

    assert contador_carrito(driver_logueado) == "1", (
        f"El contador del carrito tenía que quedar en 1 y quedó en {contador_carrito(driver_logueado)!r}."
    )
    print(f"Producto agregado: {nombre} | Precio: {precio}")


def test_producto_agregado_aparece_en_el_carrito(driver_logueado):
    """El producto agregado aparece en cart.html, con el mismo nombre y el mismo precio."""
    nombre, precio = agregar_primer_producto(driver_logueado)
    abrir_carrito(driver_logueado)

    assert "cart.html" in driver_logueado.current_url, (
        f"No se abrió el carrito. La URL quedó en {driver_logueado.current_url}."
    )
    items = items_del_carrito(driver_logueado)
    assert len(items) == 1, f"En el carrito tenía que haber 1 producto y hay {len(items)}."
    assert items[0]["nombre"] == nombre, (
        f"El carrito muestra {items[0]['nombre']!r} y se había agregado {nombre!r}."
    )
    assert items[0]["precio"] == precio, (
        f"En el carrito el precio es {items[0]['precio']!r} y en el catálogo era {precio!r}."
    )
