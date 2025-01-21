from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

# Register View
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Replace 'login' with your desired redirect
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

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