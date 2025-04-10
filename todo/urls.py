from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token  # added this line for tken
from .views import TaskViewSet, SecureHelloView 

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = router.urls + [
    path('api-token-auth/', obtain_auth_token),
    path('secure-hello/', SecureHelloView.as_view()),
]