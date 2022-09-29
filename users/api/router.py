from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from users.api.views import UserView, RegisterView

urlpatterns = [
    path('auth/login', TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('auth/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/me', UserView.as_view()),
    path('register', RegisterView.as_view()),
]
