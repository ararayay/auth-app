from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from auth_app.views import RegisterAPIView, LoginAPIView, LogoutAPIView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('register/', RegisterAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('logout/', LogoutAPIView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]
