import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MisHuellitas.settings")
django.setup()

from inventario.models import Categoria, Producto
import pandas as pd

inventario = pd.read_csv("inventario.csv")

categorias_raw = inventario['Categoria'].unique()
print(categorias_raw)
categorias = []
for i in categorias_raw:
    cat = Categoria(
        nombre = i, 
    )
    categorias.append(cat)
    
Categoria.objects.bulk_create(categorias)

productos = []
for i in range(len(inventario)):
    print( inventario.loc[i, "ID"]
          ,inventario.loc[i, "Nombre Producto"]
          ,inventario.loc[i, "Cantidad"]
          ,inventario.loc[i, "Precio"]
          ,inventario.loc[i, "Categoria"])
    cat = Categoria.objects.get(nombre=inventario.loc[i, "Categoria"])

    prod = Producto(
        codigoBarras = inventario.loc[i, "ID"],
        nombre = inventario.loc[i, "Nombre Producto"],
        cantidad = inventario.loc[i, "Cantidad"],
        precio =  inventario.loc[i, "Precio"],
        categoria = cat
    )
    productos.append(prod)
Producto.objects.bulk_create(productos)