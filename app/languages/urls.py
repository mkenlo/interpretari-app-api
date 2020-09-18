from django.urls import path, include
from rest_framework import routers

from .views import LanguageList, LanguageDetail

urlpatterns = [
    path("", LanguageList.as_view(), name="language_list"),
    path("<int:pk>", LanguageDetail.as_view(), name="language_detail")
] 