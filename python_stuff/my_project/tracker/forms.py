from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Budget, Expense

class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['amount']

class ExpenseForm(forms.ModelForm):
    CATEGORY_CHOICES = [
        ('Food', 'Food'),
        ('Transportation', 'Transportation'),
        ('Entertainment', 'Entertainment'),
        ('Accommodation', 'Accommodation'),
        ('Amenities', 'Amenities'),
        ('Healthcare', 'Healthcare'),
        ('Investments', 'Investments'),
        ('Travel', 'Travel'),
        ('Other', 'Other'),
    ]

    category = forms.ChoiceField(choices=CATEGORY_CHOICES)
    class Meta:
        model = Expense
        fields = ['name', 'amount', 'category']

#class BudgetForm(forms.ModelForm):
#    class Meta:
#       model = Budget
#        fields = ['name', 'amount']

#class RegisterForm(UserCreationForm):
#    email = forms.EmailField()

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Enter a valid email address.")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {
            'username': 'Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
            'password1': 'Your password must contain at least 8 characters and cannot be entirely numeric.',
        }