from django.urls import path
from django.contrib.auth.views import LoginView
from users.views import ProfileAPIView

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('profile/', ProfileAPIView.as_view())
]