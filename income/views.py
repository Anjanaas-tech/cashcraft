from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages  # Import messages for debugging
from .models import Income
from .forms import IncomeForm

class IncomeListView(ListView):
    model = Income
    template_name = "income/list.html"
    context_object_name = "incomes"  

    def get_queryset(self):
        return Income.objects.filter(user=self.request.user)  # Fetch only the logged-in user's income

class IncomeCreateView(CreateView):
    model = Income
    form_class = IncomeForm
    template_name = 'dashboard/add_income.html'
    success_url = reverse_lazy('income_add')

    def form_valid(self, form):
        form.instance.user = self.request.user  # Assign logged-in user
        response = super().form_valid(form)
        form = IncomeForm()  # Clear form after submission
        return response

class IncomeUpdateView(UpdateView):
    model = Income
    template_name = "income/update.html"  
    fields = ["title", "amount", "date"]
    success_url = reverse_lazy("income_list")  

class IncomeDeleteView(DeleteView):
    model = Income
    template_name = "income/delete.html"  
    success_url = reverse_lazy("income_list")


