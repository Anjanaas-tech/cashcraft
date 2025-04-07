from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Income
from .forms import IncomeForm

@login_required
def add_income(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        date = request.POST.get('date')
        category = request.POST.get('category','Uncategorized')
        source = request.POST.get('source')

        Income.objects.create(
            amount=amount,
            date=date,
            category=category,
            source=source,
            user=request.user
        )
        return redirect('income_list')  # Ensure this matches your URL name
    return render(request, 'income/add_income.html')


@login_required
def income_list(request):
    incomes = Income.objects.filter(user=request.user)
    return render(request, 'income/income_list.html', {'incomes': incomes})



# Class-based view for listing incomes
class IncomeListView(LoginRequiredMixin, ListView):
    model = Income
    template_name = "income/list.html"
    context_object_name = "incomes"
    login_url = "/accounts/login/"

    def get_queryset(self):
        return Income.objects.filter(user=self.request.user)

# Class-based view for creating income
class IncomeCreateView(LoginRequiredMixin, CreateView):
    model = Income
    form_class = IncomeForm
    template_name = 'income/add_income.html'
    success_url = reverse_lazy('income_list')
    login_url = "/accounts/login/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# Class-based view for updating income
class IncomeUpdateView(LoginRequiredMixin, UpdateView):
    model = Income
    fields = ['category', 'amount', 'date', 'source']
    template_name = 'income/update.html'
    success_url = reverse_lazy('income_list')
    login_url = "/accounts/login/"

# Class-based view for deleting income
class IncomeDeleteView(LoginRequiredMixin, DeleteView):
    model = Income
    template_name = "income/delete.html"
    success_url = reverse_lazy("income_list")
    login_url = "/accounts/login/"