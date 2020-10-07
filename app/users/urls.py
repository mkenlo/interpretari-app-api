from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'', UserViewSet, basename = 'user')

urlpatterns = [
    path(r'', include(router.urls))]