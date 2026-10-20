"""demanda-mx: datos simulados de demanda en CDMX, Guadalajara y Monterrey."""
from importlib.resources import files
import pandas as pd

__version__ = "0.1.0"


def load_demanda() -> pd.DataFrame:
    """Devuelve un DataFrame con columnas: cantidad (int), fecha (datetime), ubicacion (str)."""
    path = files("demanda_mx") / "data" / "demanda.csv"
    with path.open("r", encoding="utf-8") as f:
        return pd.read_csv(f, parse_dates=["fecha"])
