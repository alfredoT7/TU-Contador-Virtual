from django.urls import reverse, path, include
from .views import home, InicioDeSesion,registro_usuario
urlpatterns = [
    path('', home, name='home'),
    path('InicioDeSesion/', InicioDeSesion, name='InicioDeSesion'),
    path('Registro/', registro_usuario, name='Registro'),
]
