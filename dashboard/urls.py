from django.urls import path
from . import views
from income.views import add_income


urlpatterns = [
    path('', views.dashboard, name='dashboard'),  # Dashboard page
    path('add-income/', add_income, name='add_income'),
    path("add-expense/", views.add_expense, name="add_expense"),
    path('update-financials/', views.update_financials, name='update_financials'),
    path("goals/", views.add_expense, name="list"),
    

]