from django.urls import path
from .views import IncomeListView, IncomeCreateView, IncomeUpdateView, IncomeDeleteView
from . import views

urlpatterns = [
    path('', IncomeListView.as_view(), name='income_list'),
    path('create/', IncomeCreateView.as_view(), name='income_create'),
    path('update/<int:pk>/', IncomeUpdateView.as_view(), name='income_update'),
    path('delete/<int:pk>/', IncomeDeleteView.as_view(), name='income_delete'),
    path('add-income/', views.add_income, name='add_income'),
    path('list/', views.income_list, name='income_list'),
]
