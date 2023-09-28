from reactpy import component, html, use_state
from .models import Producto
from reactpy_django.hooks import use_query

def get_productos():
    return Producto.objects.all()

@component
def show_producto():
    producto, set_producto = use_state("-")

    
    return html.label(
        'Codigo de barras: ', input_producto(set_producto)
        ,html.div("Producto: " + producto)
    )

@component
def input_producto(set_producto):
    productos = use_query(get_productos)
    def handle_change(event):
        productoEncontrado = [item for item in productos.data if str(item.codigoBarras) == str(event["target"]["value"])]
        if len(productoEncontrado)>0:
            set_producto(productoEncontrado[0].nombre)
        else:
            set_producto("-")
        
        
    return html.input(
        {
            "type":"number",
            "name":"producto",
            "required id":"id_producto",
            "on_change": handle_change
        }
    )


    