# authuser/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User,Transactions,Category

class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)
    initial_balance = forms.FloatField(label='Balance Inicial', required=True, min_value=0)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'initial_balance', 'password1', 'password2']

class ExpenseForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.filter(category_type='expense'))

    class Meta:
        model = Transactions
        fields = ['amount', 'description', 'category']

class IncomeForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.filter(category_type='income'))

    class Meta:
        model = Transactions
        fields = ['amount', 'description', 'category']