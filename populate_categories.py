import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ContadorVirtual.settings')
django.setup()

from authuser.models import Category

categories = [
    ('Salario', 'income'),
    ('Intereses', 'income'),
    ('Ventas', 'income'),
    ('Alquiler', 'income'),
    ('Otros Ingresos', 'income'),
    ('Comida', 'expense'),
    ('Transporte', 'expense'),
    ('Entretenimiento', 'expense'),
    ('Educación', 'expense'),
    ('Salud', 'expense'),
    ('Ropa', 'expense'),
    ('Otros Gastos', 'expense'),
]

for name, category_type in categories:
    Category.objects.create(name=name, category_type=category_type)

print('Categorías predefinidas añadidas correctamente.')