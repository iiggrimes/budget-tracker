from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from .views import budget_list, budget_create, budget_delete

##problem, why is register grey


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='tracker/login.html'), name='login'),
    #path('logout/', auth_views.LogoutView.as_view(template_name='tracker/logout.html'), name='logout'),
    path('logout/', views.custom_logout_view, name='logout'),
    path('', views.home, name='home'),  # Home view
    path('budgets/', budget_list, name='budget_list'), # either this one or the bottom one
    path('budget/', views.budget_list, name='budget_list'),
    path('budgets/new/', budget_create, name='budget_create'),
    path('budgets/<int:pk>/delete/', budget_delete, name='budget_delete'),
    path('add_expense/', views.add_expense_view, name='add_expense'),
    path('home/', views.home, name='home'),
    path('create_budget/', views.create_budget, name='create_budget'),

]