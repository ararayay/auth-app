from django.contrib import admin
from django.urls import path

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework_simplejwt.views import TokenRefreshView

from auth_app.views import LoginAPIView, LogoutAPIView, RegisterAPIView, UserAPIView
from auth_app.views.access.permissions import PermissionAPIView
from auth_app.views.access.roles import RoleAPIView
from auth_app.views.mock.projects import ProjectsAPIView
from auth_app.views.mock.reports import ReportsAPIView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

    path('register/', RegisterAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('logout/', LogoutAPIView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('user/', UserAPIView.as_view()),

    path('projects/', ProjectsAPIView.as_view()),
    path('reports/', ReportsAPIView.as_view()),

    path('access/permissions/', PermissionAPIView.as_view()),
]
