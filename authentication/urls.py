from django.urls import path , include
from rest_framework_simplejwt.views import TokenRefreshView
import authentication.views as views
app_name = "accounts"

urlpatterns = [
    path('register/', views.RegisterationView.as_view(), name="register"),
    path('login/', views.LoginView.as_view(), name="login"),
    path('user/', views.UserDetailView.as_view(), name="user"),
    
]