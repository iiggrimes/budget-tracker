#from django.shortcuts import render
# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from .models import Budget
from .forms import BudgetForm

def custom_logout_view(request):
    logout(request)
    return redirect('login')
@login_required
def budget_list(request):
    budgets = Budget.objects.filter(user=request.user)
    return render(request, 'tracker/budget_list.html', {'budgets': budgets})

@login_required
def budget_create(request):
    if request.method == 'POST':
        form = BudgetForm(request.POST)
        if form.is_valid():
            budget = form.save(commit=False)
            budget.user = request.user
            budget.save()
            return redirect('budget_list')
    else:
        form = BudgetForm()
    return render(request, 'tracker/budget_form.html', {'form': form})

@login_required
def budget_delete(request, pk):
    budget = Budget.objects.get(pk=pk, user=request.user)
    if request.method == 'POST':
        budget.delete()
        return redirect('budget_list')
    return render(request, 'tracker/budget_confirm_delete.html', {'budget': budget})
@login_required
def home(request):
    return render(request, 'tracker/home.html')
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        else:
            print(form.errors)  # Print form errors to the console for debugging
    else:
        form = RegisterForm()
    return render(request, 'tracker/register.html', {'form': form})

