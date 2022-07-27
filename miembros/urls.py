from django.urls import path
from miembros.views import  RegistroView

urlpatterns = [
    path('registro/', RegistroView.as_view(), name="registro"),
    
    
    
]
