from django.urls import path
from miembros.views import    RegistroView, EdicionUserView, NuevaPassView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('registro/', RegistroView.as_view(), name="registro"),
    path('editar-user/', EdicionUserView.as_view(), name="editar-user"),
    path('password/', NuevaPassView.as_view(template_name='registration/nuevo-pass.html'), name='nuevo-pass'),
    
    
    
    

    
    
    
]
