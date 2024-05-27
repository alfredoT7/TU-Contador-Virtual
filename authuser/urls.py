from django.urls import reverse, path, include
from .views import home, InicioDeSesion,registro_usuario,PanelInicio,add_expense,add_income
urlpatterns = [
    path('', home, name='home'),
    path('InicioDeSesion/', InicioDeSesion, name='InicioDeSesion'),
    path('Registro/', registro_usuario, name='Registro'),
    path('PanelInicio/', PanelInicio, name='PanelInicio'),
    path('add_expense/', add_expense, name='add_expense'),
    path('add_income/', add_income, name='add_income'),
]
