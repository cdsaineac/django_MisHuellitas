from django.forms import ModelForm, NumberInput
from .models import *

class VentaForm(ModelForm):
    class Meta:
        model = Venta
        exclude = ['vendedor','precio_base','precio_final']
        widgets={
            "producto": NumberInput(), 
        }
    
class CompraForm(ModelForm):
    class Meta:
        model = Compra
        exclude = ['comprador']
        widgets={
            "producto": NumberInput(), 
        }
    
    