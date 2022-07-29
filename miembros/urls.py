from django.urls import path
from miembros.views import  RegistroView, EdicionUserView

urlpatterns = [
    path('registro/', RegistroView.as_view(), name="registro"),
    path('editar-user/', EdicionUserView.as_view(), name="editar-user")
    
    
    
]
