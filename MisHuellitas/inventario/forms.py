from django.forms import ModelForm, NumberInput
from django.core.exceptions import ValidationError
from .models import *

class VentaForm(ModelForm):
    class Meta:
        model = Venta
        exclude = ['vendedor','precio_base','precio_final']
        widgets={
            "producto": NumberInput(), 
        }
    def clean(self):
        cleaned_data = super().clean()
        cantidad_vendida = cleaned_data.get("cantidad_o_precio")

        if cantidad_vendida < 0:
            raise ValidationError(
                "La cantidad o precio no puede ser negativo"
            )

class VentaFormUpdate(ModelForm):
    class Meta:
        model = Venta
        exclude = ['vendedor','precio_base','precio_final']
        widgets={
            "producto": NumberInput(), 
        }

    def clean(self):
        cleaned_data = super().clean()
        cantidad_vendida = cleaned_data.get("cantidad_o_precio")

        if cantidad_vendida < 0:
            raise ValidationError(
                "La cantidad o precio no puede ser negativo"
            )

    
class CompraForm(ModelForm):
    class Meta:
        model = Compra
        exclude = ['comprador']
        widgets={
            "producto": NumberInput(), 
        }
        
    def clean(self):
        cleaned_data = super().clean()
        cantidad = cleaned_data.get("cantidad")

        if cantidad < 0:
            raise ValidationError(
                "La cantidad comprada no puede ser negativa"
            )
    
    