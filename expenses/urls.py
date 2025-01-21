from django.urls import path
from .views import ExpenseListView, ExpenseCreateView, ExpenseUpdateView, ExpenseDeleteView

urlpatterns = [
    path('', ExpenseListView.as_view(), name='expense_list'),
    path('create/', ExpenseCreateView.as_view(), name='expense_create'),
    path('update/<int:pk>/', ExpenseUpdateView.as_view(), name='expense_update'),
    path('delete/<int:pk>/', ExpenseDeleteView.as_view(), name='expense_delete'),
]
