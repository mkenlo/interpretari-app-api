from django.urls import path, include
from rest_framework import routers
from .views import TranslationViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'', TranslationViewSet, basename = 'translation')

urlpatterns = [
    path(r'', include(router.urls))
]