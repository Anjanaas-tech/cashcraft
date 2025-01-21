from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Income
from .forms import IncomeForm


class IncomeListView(ListView):
    model = Income
    template_name = 'income/list.html'
    context_object_name = 'incomes'

class IncomeCreateView(CreateView):
    model = Income
    form_class = IncomeForm
    template_name = 'income/create.html'
    success_url = reverse_lazy('income_list')

class IncomeUpdateView(UpdateView):
    model = Income
    form_class = IncomeForm
    template_name = 'income/update.html'
    success_url = reverse_lazy('income_list')

class IncomeDeleteView(DeleteView):
    model = Income
    template_name = 'income/delete.html'
    success_url = reverse_lazy('income_list')
