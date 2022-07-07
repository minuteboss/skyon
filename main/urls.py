from django.urls import path
from . import views


urlpatterns = [
	path('accounts/signup/', views.signup, name="register"),
    path('dashboard/',views.dashboard, name="dashboard"),
]    