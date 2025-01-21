from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Goal
from .forms import GoalForm


class GoalListView(ListView):
    model = Goal
    template_name = 'goals/list.html'
    context_object_name = 'goals'

class GoalCreateView(CreateView):
    model = Goal
    form_class = GoalForm
    template_name = 'goals/form.html'
    success_url = reverse_lazy('goals:list')

class GoalUpdateView(UpdateView):
    model = Goal
    form_class = GoalForm
    template_name = 'goals/form.html'
    success_url = reverse_lazy('goals:list')

class GoalDeleteView(DeleteView):
    model = Goal
    template_name = 'goals/confirm_delete.html'
    success_url = reverse_lazy('goals:list')
