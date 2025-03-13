from django.urls import path
from .views import ExpenseListView, ExpenseCreateView, ExpenseUpdateView, ExpenseDeleteView
from . import views

app_name = "expenses"

urlpatterns = [

    path("list/", ExpenseListView.as_view(), name="list"),
    path('create/', ExpenseCreateView.as_view(), name='expense_create'),
    path('update/<int:pk>/', ExpenseUpdateView.as_view(), name='expense_update'),
    path('delete/<int:pk>/', ExpenseDeleteView.as_view(), name='expense_delete'),
    path("create/", views.ExpenseCreateView.as_view(), name="create_expense"),
]
