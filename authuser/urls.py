from django.urls import reverse, path, include
from .views import home, InicioDeSesion
urlpatterns = [
    path('', home, name='home'),
    path('InicioDeSesion/', InicioDeSesion, name='InicioDeSesion'),
]
