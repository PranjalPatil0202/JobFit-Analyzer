# pyrefly: ignore [missing-import]
from django.urls import path, include
# pyrefly: ignore [missing-import]
from rest_framework.routers import DefaultRouter
from .views import JobViewSet

router = DefaultRouter()
router.register(r'jobs', JobViewSet, basename='job')

urlpatterns = [
    path('recommend-jobs/', JobViewSet.as_view({'get': 'recommendations'}), name='recommend-jobs'),
    path('', include(router.urls)),
]
