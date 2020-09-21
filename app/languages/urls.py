from django.urls import path, include
from rest_framework import routers
from .views import LanguageViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'', LanguageViewSet, basename = 'language')


urlpatterns = [
    path(r'', include(router.urls))
]