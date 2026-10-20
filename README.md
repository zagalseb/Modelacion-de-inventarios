# demanda-mx

Datos simulados de demanda (Ciudad de México, Guadalajara, Monterrey), 01/01/2026–10/10/2026.

```python
from demanda_mx import load_demanda_original, load_demanda_estres
df = load_demanda_original()   # 1,200 pedidos (base)
df_estres = load_demanda_estres()  # 1,297 pedidos (demanda sesgada al alza)
```
Columnas: `Cantidad demandada`, `Fecha del pedido`, `Ubicación`.
