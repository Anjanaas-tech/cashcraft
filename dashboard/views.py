from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.db.models import Sum
from .models import Expense, Goal
from accounts.models import User  
from income.models import Income
from income.forms import IncomeForm


@login_required
def dashboard(request):
    users = User.objects.all()

    # Fetch total income for the logged-in user
    total_income = Income.objects.filter(user=request.user).aggregate(Sum('amount'))['amount__sum'] or 0

    # Fetch total expenses for the logged-in user
    total_expenses = Expense.objects.filter(user=request.user).aggregate(Sum('amount'))['amount__sum'] or 0

    # Fetch goals for the logged-in user
    goals = Goal.objects.filter(user=request.user)

    # Calculate the progress for each goal
    goal_progress = []
    for goal in goals:
        # Calculate the current balance for this goal (sum of allocated amounts)
        current_balance = sum(expense.amount for expense in Expense.objects.filter(user=request.user, category=goal.category))
        
        # Ensure remaining balance calculation is accurate
        remaining_balance = max(goal.target_amount - current_balance, 0)

        # Calculate progress percentage safely
        progress = (current_balance / goal.target_amount) * 100 if goal.target_amount else 0

        goal_progress.append({
            'goal_name': goal.name,
            'target_amount': goal.target_amount,
            'current_balance': current_balance,
            'remaining_balance': remaining_balance,
            'progress': progress
        })

    # Fetch expenses for the logged-in user
    user_expenses = Expense.objects.filter(user=request.user)

    # Render the dashboard with the data
    return render(request, 'dashboard/dashboard.html', {
        'users': users,
        'total_income': total_income,
        'total_expenses': total_expenses,
        'goal_progress': goal_progress,
        'user_expenses': user_expenses,
    })



@login_required
def add_expense(request):
    if request.method == "POST":
        amount = request.POST.get("amount")
        category = request.POST.get("category")
        date = request.POST.get("date")
        description = request.POST.get("description", "")

        # Save the expense data
        Expense.objects.create(
            user=request.user,
            amount=amount,
            category=category,
            date=date,
            description=description,
        )
        messages.success(request, "Expense added successfully.")
        return redirect("dashboard")

    categories = ["Food", "Transport", "Bills", "Entertainment", "Miscellaneous"]
    return render(request, "dashboard/add_expense.html", {"categories": categories})


@login_required
def update_financials(request):
    if request.method == 'POST':
        # Process the financial data (income, expense, budget)
        messages.success(request, "Financial data updated successfully.")
        return redirect('dashboard')  # Redirect back to the dashboard
    
    return HttpResponse("Invalid request", status=400)
