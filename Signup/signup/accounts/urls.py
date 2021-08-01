from django.urls import path

# from accounts.views import home_view, signup_view, activation_sent_view, activate
from accounts.views import home_view, signup_view, loginPage, logoutUser

urlpatterns = [
    path('', home_view, name="home"),
    path('signup/', signup_view, name="signup"),
    path('login/', loginPage, name="login"),
    path('logout/', logoutUser, name="logout"),
    # path('sent/', activation_sent_view, name="activation_sent"),
    # path('activate/<slug:uidb64>/<slug:token>/', activate, name='activate'),
]