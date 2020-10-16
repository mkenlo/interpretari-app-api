from django.urls import path, include
from rest_framework import routers
from .views import TranslationViewSet

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'translations', TranslationViewSet, basename = 'translation')

urlpatterns = [
    path(r'', include(router.urls))
]