from django.urls import path
from . import views

app_name = 'goals'

urlpatterns = [
    path('', views.GoalListView.as_view(), name='list'),  # List all goals
    path('create/', views.GoalCreateView.as_view(), name='create'),  # Create a goal
    path('<int:pk>/update/', views.GoalUpdateView.as_view(), name='update'),  # Update a goal
    path('<int:pk>/delete/', views.GoalDeleteView.as_view(), name='delete'),  # Delete a goal
]
