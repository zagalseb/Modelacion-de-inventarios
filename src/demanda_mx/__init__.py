"""demanda-mx: datos simulados de demanda en CDMX, Guadalajara y Monterrey.

Dos conjuntos de datos (mismas columnas que los Excel originales):
  - load_demanda_original(): demanda simulada base (1,200 pedidos)
  - load_demanda_estres():   demanda sesgada al alza (1,297 pedidos)
"""
from importlib.resources import files
import pandas as pd

__version__ = "0.2.0"
__all__ = ["load_demanda", "load_demanda_original", "load_demanda_estres"]

_ARCHIVOS = {"original": "demanda_original.csv", "estres": "demanda_estres.csv"}


def load_demanda(nombre: str = "original") -> pd.DataFrame:
    """Devuelve un DataFrame con columnas 'Cantidad demandada', 'Fecha del pedido', 'Ubicación'.

    nombre: 'original' (base) o 'estres' (demanda sesgada).
    """
    if nombre not in _ARCHIVOS:
        raise ValueError(f"nombre debe ser uno de {list(_ARCHIVOS)}, no {nombre!r}")
    path = files("demanda_mx") / "data" / _ARCHIVOS[nombre]
    with path.open("r", encoding="utf-8") as f:
        return pd.read_csv(f, parse_dates=["Fecha del pedido"])


def load_demanda_original() -> pd.DataFrame:
    return load_demanda("original")


def load_demanda_estres() -> pd.DataFrame:
    return load_demanda("estres")
