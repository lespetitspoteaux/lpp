from django.urls import path, include
from . import views

urlpatterns = [
    path('dashboard/',views.dashboard,name='dashboard'),
    path('settings/',views.settings,name='settings'),
    path('password/', views.change_password, name='change_password'),
]
