# Pre-entrega de automation testing — SauceDemo

Pre-entrega de **Talento Tech Automation QA**, Ciudad de Buenos Aires.

El repositorio lleva el nombre que pide la consigna: `pre-entrega-automation-testing-alumno-secreto`.

Se automatiza el ingreso a [SauceDemo](https://www.saucedemo.com/), la revisión del inventario y la carga del primer producto en el carrito. Cada prueba abre su propio navegador. Si una falla, las demás siguen.

## Propósito del proyecto

Aplicar lo visto hasta la clase 8:

- localizar elementos por id, clase y xpath
- completar el formulario de acceso
- usar esperas explícitas (`WebDriverWait`), sin pausas fijas
- comprobar la URL, los títulos, los productos y el carrito

## Tecnologías utilizadas

- Python 3
- Pytest
- Selenium WebDriver
- pytest-html, para el reporte
- Git y GitHub

El navegador se elige en este orden: Google Chrome, Brave, Firefox. En la cursada se usa Chrome. Hace falta tener al menos uno de los tres instalado. La primera vez, Selenium Manager descarga el driver que corresponda.

## Estructura del proyecto

```text
datos/credenciales.json          URL y usuario de la demo
utils/configuracion.py           Lectura de esos datos
utils/navegador.py               Navegador y esperas explícitas
utils/saucedemo.py               Login, catálogo y carrito
tests/test_login.py              Login
tests/test_catalogo.py           Título, productos y elementos de la pantalla
tests/test_carrito.py            Agrega el primer producto y lo revisa en el carrito
pre-entrega-final/test_saucedemo.py
                                 Los mismos casos, en la ruta de la consigna
conftest.py                      Un navegador por prueba y captura si falla
reports/                         Reporte HTML
reports/capturas/                Capturas, solo cuando una prueba falla
```

## Instalación de dependencias

Desde la raíz del proyecto, creá el entorno e instalá las dependencias.

```bash
python3 -m venv .venv
```

En macOS y Linux:

```bash
source .venv/bin/activate
pip install -r requirements.txt
```

En Windows:

```bash
.venv\Scripts\activate
pip install -r requirements.txt
```

## Cómo ejecutar las pruebas

Ejecutá las pruebas desde la raíz del proyecto.

Comando de la consigna. Deja `reporte.html` en la raíz:

```bash
pytest pre-entrega-final/test_saucedemo.py -v --html=reporte.html --self-contained-html
```

El mismo conjunto, con el reporte en `reports/` (es el que queda en el repositorio):

```bash
pytest tests/ -v --html=reports/reporte.html --self-contained-html
```

Para ver la ventana del navegador:

```bash
MOSTRAR_NAVEGADOR=1 pytest tests/ -v
```

Para elegir el navegador:

```bash
NAVEGADOR=firefox pytest tests/ -v
NAVEGADOR=chrome pytest tests/ -v
```

## Casos de prueba

**Login**

- Abre `https://www.saucedemo.com/`
- Ingresa `standard_user` / `secret_sauce`
- Espera el paso a `/inventory.html`
- Comprueba el título Swag Labs y el encabezado Products

**Catálogo**

- Comprueba el título de la página de inventario
- Comprueba que haya productos a la vista
- Comprueba el menú, el filtro de orden y el acceso al carrito
- Deja en el reporte el nombre y el precio del primer producto

**Carrito**

- Agrega el primer producto
- Verifica que el contador quede en 1
- Abre el carrito y comprueba que ese producto esté, con el mismo nombre y el mismo precio

## Reporte y evidencias

- `reports/reporte.html` es el reporte HTML de una ejecución correcta.
- Si una prueba falla, la captura queda en `reports/capturas/<nombre-de-la-prueba>.png`.
- El nombre y el precio del primer producto salen en la salida de Pytest y en el detalle de `test_primer_producto_tiene_nombre_y_precio`.

Las credenciales no son un secreto: son el usuario público de la demo de Sauce Labs y están en `datos/credenciales.json`.

## Anonimato de los commits

Hace más de diez años que evito publicar datos personales en GitHub, y no voy a empezar ahora. Lo que había que aclarar ya está en las notas de AV: el profesor las vio.

Por eso esta pre-entrega figura a nombre de **Alumno Secreto** (`alumno.secreto@anon.local`), con un correo que no es personal. Esa identidad está configurada solo en esta carpeta y no cambia la de Git en el resto de la máquina.
