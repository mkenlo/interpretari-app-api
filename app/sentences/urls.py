from django.urls import path, include
from rest_framework import routers
from .views import SentenceViewSet

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'sentences', SentenceViewSet, basename = 'sentence')


urlpatterns = [
    path(r'', include(router.urls))
]