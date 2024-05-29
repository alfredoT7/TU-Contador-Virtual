from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import RegistroUsuarioForm, ExpenseForm, IncomeForm
from .models import Account, Transactions, User
from django.contrib.auth.decorators import login_required
#@login_required
def home(request):
    return render(request, 'authuser/home.html')

def InicioDeSesion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('PanelInicio')
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos')
    
    return render(request, 'authuser/InicioDeSesion.html')

def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            initial_balance = form.cleaned_data.get('initial_balance')
            Account.objects.create(user=user, balance=initial_balance)
            username = form.cleaned_data.get('username')
            messages.success(request, f'¡Cuenta creada para {username}!')
            print(f'cuenta creada para {username}')
            return redirect('home')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'authuser/Registro.html', {'form': form})
@login_required
def PanelInicio(request):
    if not request.user.is_authenticated:
        return redirect('InicioDeSesion')

    account = Account.objects.get(user=request.user)
    transactions = Transactions.objects.filter(user=request.user).order_by('-date')
    return render(request, 'authuser/PanelInicio.html', {'account': account, 'transactions': transactions})
@login_required
def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            account = Account.objects.get(user=request.user)
            account.balance -= expense.amount
            account.save()
            return redirect('PanelInicio')
    else:
        form = ExpenseForm()
    return render(request, 'authuser/add_expense.html', {'form': form})
@login_required
def add_income(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            income = form.save(commit=False)
            income.user = request.user
            income.save()
            account = Account.objects.get(user=request.user)
            account.balance += income.amount
            account.save()
            return redirect('PanelInicio')
    else:
        form = IncomeForm()
    return render(request, 'authuser/add_income.html', {'form': form})