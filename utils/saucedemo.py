"""Acciones sobre saucedemo.com: login, catálogo y carrito."""

from selenium.webdriver.common.by import By

from utils.navegador import (
    esperar_clickeable,
    esperar_texto,
    esperar_url_contiene,
    esperar_visible,
)

CAMPO_USUARIO = (By.ID, "user-name")
CAMPO_CONTRASENA = (By.ID, "password")
BOTON_LOGIN = (By.ID, "login-button")
LOGO = (By.CLASS_NAME, "app_logo")
TITULO_SECCION = (By.CLASS_NAME, "title")
PRODUCTO = (By.CLASS_NAME, "inventory_item")
NOMBRE_PRODUCTO = (By.CLASS_NAME, "inventory_item_name")
PRECIO_PRODUCTO = (By.CLASS_NAME, "inventory_item_price")
MENU = (By.ID, "react-burger-menu-btn")
FILTRO = (By.CLASS_NAME, "product_sort_container")
LINK_CARRITO = (By.CLASS_NAME, "shopping_cart_link")
BADGE_CARRITO = (By.CLASS_NAME, "shopping_cart_badge")
ITEM_CARRITO = (By.CLASS_NAME, "cart_item")


def abrir_login(driver, url):
    """Abre la home y espera a que el formulario de login esté listo."""
    driver.get(url)
    esperar_visible(driver, CAMPO_USUARIO)


def iniciar_sesion(driver, usuario, contrasena):
    """Completa el login y espera la redirección al inventario."""
    esperar_visible(driver, CAMPO_USUARIO).send_keys(usuario)
    esperar_visible(driver, CAMPO_CONTRASENA).send_keys(contrasena)
    esperar_clickeable(driver, BOTON_LOGIN).click()
    # Criterio mínimo: la URL tiene que pasar a /inventory.html.
    esperar_url_contiene(driver, "inventory.html")
    esperar_texto(driver, TITULO_SECCION, "Products")
    esperar_texto(driver, LOGO, "Swag Labs")


def titulo_pagina(driver):
    """Título de la pestaña del navegador. En SauceDemo es Swag Labs."""
    return driver.title


def titulo_seccion(driver):
    """Encabezado visible de la sección. En el inventario es Products."""
    return esperar_visible(driver, TITULO_SECCION).text


def texto_logo(driver):
    """Texto de la marca que aparece en el encabezado."""
    return esperar_visible(driver, LOGO).text


def obtener_productos(driver):
    """Lista los productos visibles con su nombre, precio y botón."""
    esperar_visible(driver, PRODUCTO)
    productos = []
    for item in driver.find_elements(*PRODUCTO):
        productos.append(
            {
                "nombre": item.find_element(*NOMBRE_PRODUCTO).text.strip(),
                "precio": item.find_element(*PRECIO_PRODUCTO).text.strip(),
            }
        )
    return productos


def menu_visible(driver):
    return esperar_visible(driver, MENU).is_displayed()


def filtro_visible(driver):
    return esperar_visible(driver, FILTRO).is_displayed()


def carrito_visible(driver):
    return esperar_visible(driver, LINK_CARRITO).is_displayed()


def agregar_primer_producto(driver):
    """Hace clic en Add to cart del primer producto y espera el contador en 1."""
    productos = obtener_productos(driver)
    if not productos:
        raise AssertionError("No hay productos visibles para agregar al carrito.")
    primero = productos[0]
    esperar_clickeable(driver, (By.XPATH, "(//div[@class='inventory_item']//button)[1]")).click()
    esperar_texto(driver, BADGE_CARRITO, "1")
    return primero["nombre"], primero["precio"]


def contador_carrito(driver):
    """Número que muestra el badge del carrito."""
    return esperar_visible(driver, BADGE_CARRITO).text.strip()


def abrir_carrito(driver):
    """Entra al carrito y espera a que cargue cart.html con al menos un ítem."""
    esperar_clickeable(driver, LINK_CARRITO).click()
    esperar_url_contiene(driver, "cart.html")
    esperar_visible(driver, ITEM_CARRITO)


def items_del_carrito(driver):
    """Lee nombre y precio de cada ítem de la página del carrito."""
    esperar_visible(driver, ITEM_CARRITO)
    items = []
    for item in driver.find_elements(*ITEM_CARRITO):
        items.append(
            {
                "nombre": item.find_element(*NOMBRE_PRODUCTO).text.strip(),
                "precio": item.find_element(*PRECIO_PRODUCTO).text.strip(),
            }
        )
    return items
