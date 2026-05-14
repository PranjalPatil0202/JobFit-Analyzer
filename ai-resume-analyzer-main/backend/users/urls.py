from django.urls import path
from .views import RegisterView, ProtectedRouteView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('protected/', ProtectedRouteView.as_view(), name='protected_route'),
]
