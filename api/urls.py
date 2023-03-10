from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

app_name = 'api'

urlpatterns = [
    path('chatgpt/', views.ChatGPTView.as_view(), name='chatgpt'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/', include('users.urls', namespace='users')),
    path('skills/', include('skills.urls', namespace='skills')),
]