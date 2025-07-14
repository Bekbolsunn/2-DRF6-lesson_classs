from django.urls import path
from users.views import RegistrationAPIView, AuthorizationAPIView, ConfirmUserAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from users.views import CustomTokenObtainPairView
from users.oauth import GoogleLoginAPIView


urlpatterns = [
    path('registration/', RegistrationAPIView.as_view()),
    path('authorization/', AuthorizationAPIView.as_view()),
    path('confirm/', ConfirmUserAPIView.as_view()),

    path('jwt-token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('jwt-token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('jwt-token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('google-login/', GoogleLoginAPIView.as_view()),
]