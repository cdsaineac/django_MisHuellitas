from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import *

urlpatterns=[
    path('/', HomePageView.as_view()),
    path('home/', HomePageView.as_view(), name ='home'),
    path('admin/', TemplateView.as_view(),name ='admin'),
    path('categorias/', login_required(CategoriaListView.as_view()), name='categoria_list'),
    path('categorias/nuevacategoria/', login_required(CategoriaCreateView.as_view()), name='categoria_new'),
    path('categorias/<int:pk>/edit/', login_required(CategoriaUpdateView.as_view()), name ='categoria_edit'), 
    path('categorias/<int:pk>/', login_required(CategoriaDetailView.as_view()), name ='categoria_detail'), 
    path('categorias/<int:pk>/delete/ ', login_required(CategoriaDeleteView.as_view()), name ='categoria_delete'),
    path('productos/', login_required(ProductoListView.as_view()), name='producto_list'),
    path('productos/nuevoproducto/', login_required(ProductoCreateView.as_view()), name='producto_new'),
    path('productos/<int:pk>/edit/', login_required(ProductoUpdateView.as_view()), name ='producto_edit'), 
    path('productos/<int:pk>/', login_required(ProductoDetailView.as_view()), name ='producto_detail'), 
    path('productos/<int:pk>/delete/ ', login_required(ProductoDeleteView.as_view()), name ='producto_delete'),
    path('ventas/', login_required(VentaListView.as_view()), name='venta_list'),
    path('ventas/nuevaventa/', login_required(VentaCreateView.as_view()), name='venta_new'),
    path('ventas/<int:pk>/edit/', login_required(VentaUpdateView.as_view()), name ='venta_edit'), 
    path('ventas/<int:pk>/', login_required(VentaDetailView.as_view()), name ='venta_detail'), 
    path('ventas/<int:pk>/delete/ ', login_required(VentaDeleteView.as_view()), name ='venta_delete'),
    path('compras/', login_required(CompraListView.as_view()), name='compra_list'),
    path('compras/nuevacompra/', login_required(CompraCreateView.as_view()), name='compra_new'),
    path('compras/<int:pk>/edit/', login_required(CompraUpdateView.as_view()), name ='compra_edit'), 
    path('compras/<int:pk>/', login_required(CompraDetailView.as_view()), name ='compra_detail'), 
    path('compras/<int:pk>/delete/ ', login_required(CompraDeleteView.as_view()), name ='compra_delete')
]
