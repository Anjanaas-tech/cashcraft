from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin  # For login protection
from .models import Goal
from .forms import GoalForm

# ------------------------
# Goal List View
# ------------------------
class GoalListView(LoginRequiredMixin, ListView):
    model = Goal
    template_name = 'goals/list.html'
    context_object_name = 'goals'

    # Show only the current user's goals
    def get_queryset(self):
        return Goal.objects.filter(user=self.request.user)

# ------------------------
# Goal Create View
# ------------------------
class GoalCreateView(LoginRequiredMixin, CreateView):
    model = Goal
    form_class = GoalForm
    template_name = 'goals/form.html'
    success_url = reverse_lazy('goals:list')

    # Attach the logged-in user before saving
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# ------------------------
# Goal Update View
# ------------------------
class GoalUpdateView(LoginRequiredMixin, UpdateView):
    model = Goal
    form_class = GoalForm
    template_name = 'goals/form.html'
    success_url = reverse_lazy('goals:list')

    # Ensure users can only edit their own goals
    def get_queryset(self):
        return Goal.objects.filter(user=self.request.user)

# ------------------------
# Goal Delete View
# ------------------------
class GoalDeleteView(LoginRequiredMixin, DeleteView):
    model = Goal
    template_name = 'goals/confirm_delete.html'
    success_url = reverse_lazy('goals:list')

    # Ensure users can only delete their own goals
    def get_queryset(self):
        return Goal.objects.filter(user=self.request.user)
