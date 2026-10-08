# Pre-entrega de automation testing — SauceDemo

Automatización de los flujos básicos de [SauceDemo](https://www.saucedemo.com/) para la pre-entrega de **Talento Tech Automation QA**.

El proyecto entra con el usuario de demostración `standard_user`, revisa el inventario y agrega el primer producto al carrito. Cada prueba abre su propio navegador: si una falla, las demás siguen corriendo.

## Propósito del proyecto

Poner en práctica lo visto hasta la clase 8:

- localizar elementos (id, clase, xpath)
- interactuar con formularios y botones
- usar esperas explícitas (`WebDriverWait`)
- validar URL, títulos, productos y el carrito

## Tecnologías utilizadas

- Python 3
- Pytest
- Selenium WebDriver
- pytest-html, para el reporte
- Git y GitHub

El navegador se elige solo, en este orden: Google Chrome, Brave, Firefox. En clase lo habitual es Chrome. Hace falta tener al menos uno de los tres instalado. Selenium descarga el driver correspondiente la primera vez (Selenium Manager).

## Estructura del proyecto

```text
datos/credenciales.json          URL y usuario de demostración
utils/configuracion.py           Lectura de esos datos
utils/navegador.py               Driver y esperas explícitas
utils/saucedemo.py               Login, catálogo y carrito
tests/test_login.py              Login
tests/test_catalogo.py           Título, productos y elementos de la interfaz
tests/test_carrito.py            Alta del primer producto y verificación en el carrito
pre-entrega-final/test_saucedemo.py
                                 Mismo conjunto, en la ruta de la consigna
conftest.py                      Navegador por prueba y captura si falla
reports/                         Reporte HTML
reports/capturas/                Capturas solo cuando una prueba falla
```

## Instalación de dependencias

Desde la raíz del proyecto:

```bash
python3 -m venv .venv
```

macOS y Linux:

```bash
source .venv/bin/activate
pip install -r requirements.txt
```

Windows:

```bash
.venv\Scripts\activate
pip install -r requirements.txt
```

## Cómo ejecutar las pruebas

Siempre desde la raíz del proyecto.

Comando de la consigna (genera `reporte.html` en la raíz):

```bash
pytest pre-entrega-final/test_saucedemo.py -v --html=reporte.html --self-contained-html
```

El mismo conjunto, con el reporte dentro de `reports/` (es el que queda en el repositorio):

```bash
pytest tests/ -v --html=reports/reporte.html --self-contained-html
```

Para ver la ventana del navegador:

```bash
MOSTRAR_NAVEGADOR=1 pytest tests/ -v
```

Para forzar un navegador:

```bash
NAVEGADOR=firefox pytest tests/ -v
NAVEGADOR=chrome pytest tests/ -v
```

## Casos que cubre

**Login**

- Abre `https://www.saucedemo.com/`
- Ingresa `standard_user` / `secret_sauce`
- Espera la redirección a `/inventory.html`
- Valida el título Swag Labs y el encabezado Products

**Catálogo**

- Valida el título de la página de inventario
- Comprueba que haya productos visibles
- Comprueba menú, filtro de orden y acceso al carrito
- Escribe en el reporte el nombre y el precio del primer producto

**Carrito**

- Agrega el primer producto
- Verifica que el contador quede en 1
- Abre el carrito y comprueba que ese producto esté, con el mismo nombre y precio

## Reporte y evidencias

- `reports/reporte.html` es el reporte HTML de Pytest de una ejecución correcta.
- Si una prueba falla, la captura queda en `reports/capturas/<nombre-de-la-prueba>.png`.
- El nombre y el precio del primer producto salen en la salida de Pytest y dentro del HTML, en el detalle de `test_primer_producto_tiene_nombre_y_precio`.

Las credenciales no son secretas: son el usuario público de la demo de Sauce Labs y están en `datos/credenciales.json`.
