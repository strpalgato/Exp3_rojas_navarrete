from django.urls import path
from . import views
from .views import exit

urlpatterns = [
    path("index", views.index, name="index"),
    path("galeria", views.galeria, name="galeria"),
    path("mision", views.mision, name="mision"),
    path("register", views.register, name="register"),
    path("productos", views.productos, name="productos"),
    path("gestionProductos", views.gestionProductos, name="gestionProductos"),
    path("guardarProducto/", views.guardarProducto, name="guardarProducto"),
    path("edicionProductos/<codigo>", views.edicionProductos, name="edicionProductos"),
    path("editarProducto", views.editarProducto, name="editarProducto"),
    path("eliminarProducto/<codigo>", views.eliminarProducto, name="eliminarProducto"),
    path("logout", exit, name="exit"),
]
