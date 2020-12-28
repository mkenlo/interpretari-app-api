from django.urls import path, include
from rest_framework import routers
from .views import LanguageViewSet

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'languages', LanguageViewSet, basename = 'language')


urlpatterns = [
    path(r'', include(router.urls))
]