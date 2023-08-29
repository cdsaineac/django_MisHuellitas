from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.edit import (UpdateView,DeleteView,CreateView, FormView)
from django.urls import reverse, reverse_lazy 
from .forms import *
from .models import *


# Create your views here.

class HomePageView (TemplateView):
    template_name = 'home.html'

class CategoriaListView (ListView):
    model = Categoria
    template_name = 'categorias/list.html'

class CategoriaCreateView(CreateView):
    model = Categoria
    template_name = 'categorias/new.html'
    fields = ('nombre',)

class CategoriaDetailView(DetailView):
    model = Categoria
    template_name = 'categorias/detail.html'

class CategoriaUpdateView(UpdateView):
    model = Categoria
    fields = ('nombre',)
    template_name = 'categorias/edit.html'

class CategoriaDeleteView(DeleteView):
    model = Categoria
    template_name = 'categorias/delete.html'
    success_url = reverse_lazy( 'categoria_list')

class ProductoListView (ListView):
    model = Producto
    template_name = 'productos/list.html'

class ProductoCreateView(CreateView):
    model = Producto
    template_name = 'productos/new.html'
    fields = ('codigoBarras','nombre','cantidad','precio','categoria')

class ProductoDetailView(DetailView):
    model = Producto
    template_name = 'productos/detail.html'

class ProductoUpdateView(UpdateView):
    model = Producto
    fields = ('codigoBarras','nombre','cantidad','precio','categoria')
    template_name = 'productos/edit.html'

class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = 'productos/delete.html'
    success_url = reverse_lazy( 'producto_list')

class VentaListView (ListView):
    model = Venta
    template_name = 'ventas/list.html'

class VentaCreateView(CreateView):
    model = Venta
    form_class = VentaForm
    template_name = 'ventas/new.html'
    
    def form_valid(self, form):
        form.instance.vendedor = self.request.user
        return super(VentaCreateView, self).form_valid(form)
    
class VentaDetailView(DetailView):
    model = Venta
    template_name = 'ventas/detail.html'

class VentaUpdateView(UpdateView):
    model = Venta
    fields = ('vendedor','producto','cantidad_o_precio','descuento','comentario')
    template_name = 'ventas/edit.html'

class VentaDeleteView(DeleteView):
    model = Venta
    template_name = 'ventas/delete.html'
    success_url = reverse_lazy('venta_list')

class CompraListView (ListView):
    model = Compra
    template_name = 'compras/list.html'

class CompraCreateView(CreateView):
    model = Compra
    form_class = CompraForm
    template_name = 'compras/new.html'
    
    def form_valid(self, form):
        form.instance.vendedor = self.request.user
        return super(CompraCreateView, self).form_valid(form)
    
class CompraDetailView(DetailView):
    model = Compra
    template_name = 'compras/detail.html'

class CompraUpdateView(UpdateView):
    model = Compra
    fields = ('comprador','producto','cantidad','precio','comentario')
    template_name = 'compras/edit.html'

class CompraDeleteView(DeleteView):
    model = Compra
    template_name = 'compras/delete.html'
    success_url = reverse_lazy('compra_list')