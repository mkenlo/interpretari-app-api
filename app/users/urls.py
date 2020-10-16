from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, GroupViewSet

router = routers.SimpleRouter(trailing_slash=False)
router.register('users', UserViewSet, basename = 'user')
router.register('groups', GroupViewSet)


urlpatterns = [
    path(r'', include(router.urls))]