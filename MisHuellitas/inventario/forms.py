from django.forms import ModelForm, NumberInput
from .models import *

class VentaForm(ModelForm):
    class Meta:
        model = Venta
        exclude = ['vendedor','precio_base','precio_final']
        widgets={
            "producto": NumberInput(), 
        }
        
    
    