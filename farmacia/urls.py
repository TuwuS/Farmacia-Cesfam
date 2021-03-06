from django.shortcuts import redirect
from django.urls import path, include
from . import views

#REST Framework 
from rest_framework import routers
router = routers.DefaultRouter()
router.register('medicamentos', views.MedicamentoViewSet)

urlpatterns = [
    # REST Framework
    path('api/', include(router.urls)),
    path('apiprescripciones', views.prescripciones),
    # Login.
    path('', views.login),
    path('login', views.login, name="login"),
    # Logout.
    path('logout', views.logout, name="logout"),
    # Register.
    path('register', views.register, name="register"),
    # Invitado.
    path('invitado', views.invitado, name="invitado"),
    # Medico.
    path('consulta-medicamentos', views.consultaMedicamentos, name="medicamentos"),
    path('recetas', views.recetas, name="prescripciones"),
    path('generar-prescripciones', views.generarPrescripciones, name="generar-presecipciones"),
    # Farmacia.
    path('recepcion-farmacia', views.recepcionFarmacia, name="recepcion-farmacia"),
    path('recepcion-entrega/<codigo>', views.recepcionEntrega, name="recepcion-entrega"),
    path('eliminarRecepcion/<codigo>', views.recepcionEliminar),
    # Stock.
    path('inventario', views.adminInventario, name="inventario"),
    path('agregar-medicamentos', views.agregarMedicamentos, name="agregar-medicamentos"),
    path('modificar-medicamentos/<codigo>', views.modificarMedicamentos, name="modificar-medicamentos"),
    path('eliminarMedicamentos/<codigo>', views.eliminarMedicamentos),
]
