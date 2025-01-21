from django.urls import path
from .views import IncomeListView, IncomeCreateView, IncomeUpdateView, IncomeDeleteView

urlpatterns = [
    path('', IncomeListView.as_view(), name='income_list'),
    path('create/', IncomeCreateView.as_view(), name='income_create'),
    path('update/<int:pk>/', IncomeUpdateView.as_view(), name='income_update'),
    path('delete/<int:pk>/', IncomeDeleteView.as_view(), name='income_delete'),
]
