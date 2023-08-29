from django.db import models
from django.urls import reverse 
# Create your models here.
class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.nombre
    
    def get_absolute_url (self ):
        return reverse( 'categoria_detail', args =[str(self.id)])

class Producto(models.Model):
    codigoBarras = models.BigIntegerField(primary_key=True)
    nombre = models.CharField(max_length=100, unique=True)
    cantidad = models.FloatField(default=0.0) 
    precio =  models.FloatField(default=0.0)
    categoria = models.ForeignKey("Categoria",on_delete=models.PROTECT)
    
    def __str__(self):
        return self.nombre  

    def get_absolute_url (self ):
        return reverse( 'producto_detail', args =[str(self.codigoBarras)])

class Venta(models.Model):
    CANTIDAD = "Cantidad"
    PRECIO = "Precio"
    TIPO_VENTA_CHOICES = [
        (CANTIDAD, "Cantidad"),
        (PRECIO, "Precio"),
    ]

    id = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(auto_now=True)
    vendedor = models.ForeignKey("auth.User",on_delete=models.PROTECT)
    producto = models.ForeignKey("Producto",on_delete=models.PROTECT)    
    tipo_venta = models.CharField(max_length=100,choices=TIPO_VENTA_CHOICES, default=CANTIDAD)
    cantidad_o_precio = models.FloatField(default=0.0) 
    precio_base =  models.FloatField(default=0.0)
    descuento = models.FloatField(default=0.0)
    comentario = models.TextField(default="Sin Comentarios")
    precio_final =  models.FloatField(default=0.0)

    def getCantidad(self):
        if(self.tipo_venta == self.CANTIDAD):
            return self.cantidad_o_precio
        else:
            return self.cantidad_o_precio / self.producto.precio 
    
    def getPrecioBase(self):
        return self.producto.precio * self.cantidad_o_precio
        
    
    def getPrecioTotal(self):
        return self.precio_base - self.descuento
    
    def reducirInventarioProducto(self, producto):
        producto = Producto.objects.get(codigoBarras = producto)
        producto.cantidad = producto.cantidad - self.cantidad_o_precio
        producto.save()

    def save(self, *args, **kwargs):
        self.cantidad_o_precio = self.getCantidad()
        self.reducirInventarioProducto(self.producto.codigoBarras)
        self.precio_base = self.getPrecioBase()
        self.precio_final = self.getPrecioTotal()
        super(Venta, self).save(*args, **kwargs)
    
    def get_absolute_url (self ):
        return reverse( 'venta_detail', args =[str(self.id)])

class Compra(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField(auto_now=True)
    comprador = models.ForeignKey("auth.User",on_delete=models.PROTECT)
    producto = models.ForeignKey("Producto",on_delete=models.PROTECT)    
    cantidad = models.PositiveIntegerField(default=0) 
    precio =  models.FloatField(default=0.0)
    