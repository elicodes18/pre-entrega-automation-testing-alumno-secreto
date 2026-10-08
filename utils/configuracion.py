"""Lee los datos externos del login (URL y credenciales de demostración)."""

import json
from pathlib import Path

RAIZ_PROYECTO = Path(__file__).resolve().parents[1]
RUTA_CREDENCIALES = RAIZ_PROYECTO / "datos" / "credenciales.json"


def cargar_credenciales():
    """Devuelve el diccionario con url_base, usuario y contrasena."""
    with RUTA_CREDENCIALES.open(encoding="utf-8") as archivo:
        return json.load(archivo)
