from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.db.models import Sum
from .models import Income, Expense, Goal
from accounts.models import User  # Assuming your custom user model is in accounts app


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
    goal_progress = [
        {
            'goal_name': goal.name,
            'target_amount': goal.target_amount,
            'current_amount': sum(expense.amount for expense in Expense.objects.filter(user=request.user, category=goal.category)),
            'progress': (sum(expense.amount for expense in Expense.objects.filter(user=request.user, category=goal.category)) / goal.target_amount) * 100 if goal.target_amount else 0
        }
        for goal in goals
    ]

    # Fetch expenses for the logged-in user
    user_expenses = Expense.objects.filter(user=request.user)

    # Render the dashboard with the data
    return render(request, 'dashboard/dashboard.html', {
        'users': users,
        'total_income': total_income,
        'total_expenses': total_expenses,
        'goal_progress': goal_progress,
        'user_expenses': user_expenses,  # Pass user_expenses to template
    })


@login_required
def add_income(request):
    if request.method == "POST":
        amount = request.POST.get('amount')
        source = request.POST.get('source')  # Get source from the form
        description = request.POST.get('description')
        date = request.POST.get('date')

        # Validate the input and save
        if amount and source and description and date:
            Income.objects.create(
                amount=amount,
                source=source,  # Save the source
                description=description,
                date=date,
                user=request.user  # Assuming you have a user field
            )
            messages.success(request, "Income added successfully.")
            return redirect('dashboard')  # Redirect to the dashboard
        else:
            messages.error(request, "Please fill in all fields.")

    return render(request, 'dashboard/add_income.html')


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
