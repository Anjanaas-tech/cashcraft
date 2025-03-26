from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Expense
from .forms import ExpenseForm

class ExpenseListView(ListView):
    model = Expense
    template_name = 'expenses/list.html'
    context_object_name = 'expenses'

class ExpenseCreateView(CreateView):
    model = Expense
    form_class = ExpenseForm
    template_name = 'expenses/create.html'
    success_url = reverse_lazy('expenses:list')  # Namespaced reference

class ExpenseUpdateView(UpdateView):
    model = Expense
    form_class = ExpenseForm
    template_name = 'expenses/update.html'
    success_url = reverse_lazy('expenses:list')  # Fix this

    def get_success_url(self):
        return reverse('expenses:list')  # Fix this

class ExpenseDeleteView(DeleteView):
    model = Expense
    template_name = 'expenses/delete.html'
    success_url = reverse_lazy('expenses:list')  # Fix this
