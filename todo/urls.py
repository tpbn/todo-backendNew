from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet
from .views_superuser import create_superuser_view

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = router.urls + [
    path('create-superuser/', create_superuser_view, name='create-superuser'),
]
