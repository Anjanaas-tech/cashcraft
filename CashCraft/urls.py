from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),   
    path('dashboard/', include('dashboard.urls')), 
    path('income/', include('income.urls')), 
    path('expenses/', include(('expenses.urls', 'expenses'), namespace='expenses')),  # <-- KEEP THIS ONE
    path('goals/', include('goals.urls')),
    path('', views.landing_page, name='landing_page'),
]
