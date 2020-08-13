# posts/urls.py
from django.urls import path
from rest_framework.routers import SimpleRouter #new
from .views import UserViewSet, PostViewSet  # new

router = SimpleRouter()  # new
router.register('users', UserViewSet, basename='users')  # new
router.register('', PostViewSet, basename='posts')  # new

urlpatterns = router.urls  # new
