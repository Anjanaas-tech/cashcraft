from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),  # Registration page
    path('login/', views.LoginView.as_view(), name='login'),  # Login page
    path('logout/', views.LogoutView.as_view(), name='logout'),  # Logout view
    path('profile/', views.profile_view, name='profile'),
    path("edit-profile/", views.edit_profile, name="edit_profile"),
    
]
