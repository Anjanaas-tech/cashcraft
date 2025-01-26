from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

# Register View
def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect("register")
        if len(password1) < 8:
            messages.error(request, "Password must be at least 8 characters.")
            return redirect("register")
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect("register")
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
            return redirect("register")

        # Save the user
        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()
        messages.success(request, "Account created successfully! Please log in.")
        return redirect("login")

    return render(request, "accounts/register.html")

# Login View
class LoginView(LoginView):
    template_name = 'accounts/login.html'

# Logout View
class LogoutView(LogoutView):
    next_page = 'login'

def profile_view(request):
    return redirect('dashboard')  # Redirects to the 'dashboard' URL

@login_required
def edit_profile(request):
    user = request.user  # Get the logged-in user

    if request.method == "POST":
        # Process form data (e.g., updating user profile details)
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')

        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()

        context = {"success_message": "Profile updated successfully!"}
        return render(request, "accounts/edit_profile.html", context)

    # For GET request, just show the profile edit form
    return render(request, "accounts/edit_profile.html", {"user": user})