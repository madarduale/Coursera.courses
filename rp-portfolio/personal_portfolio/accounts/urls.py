from django.urls import path
from . import views

urlpatterns = [
    path('',views.signup_view, name="signup_view"),
    path('Login',views.loginPage, name="Login"),
    path('Logout',views.logoutUser, name="Logout"),
]