from django.contrib import admin
from django.urls import path

from auth_app.views import RegisterAPIView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('register/', RegisterAPIView.as_view()),
]
