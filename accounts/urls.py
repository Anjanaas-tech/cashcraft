from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),  # Registration page
    path('login/', views.LoginView.as_view(), name='login'),  # Login page
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'), 
    path('profile/', views.profile_view, name='profile'),
    path("edit-profile/", views.edit_profile, name="edit_profile"),
    
]
