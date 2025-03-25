from django.shortcuts import render, get_object_or_404, redirect
from .models import Goal
from .forms import GoalForm

def goal_list(request):
    goals = Goal.objects.all()
    return render(request, "goals/list.html", {"goals": goals})

def goal_create(request):
    if request.method == "POST":
        form = GoalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("goals:goal_list")
    else:
        form = GoalForm()
    return render(request, "goals/form.html", {"form": form})

def goal_edit(request, pk):
    goal = get_object_or_404(Goal, pk=pk)
    if request.method == "POST":
        form = GoalForm(request.POST, instance=goal)
        if form.is_valid():
            form.save()
            return redirect("goals:goal_list")
    else:
        form = GoalForm(instance=goal)
    return render(request, "goals/form.html", {"form": form})

def goal_delete(request, pk):
    goal = get_object_or_404(Goal, pk=pk)
    if request.method == "POST":
        goal.delete()
        return redirect("goals:goal_list")
    return render(request, "goals/confirm_delete.html", {"goal": goal})
