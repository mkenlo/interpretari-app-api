from django.urls import path, include

from .views import SentenceList, SentenceDetail

urlpatterns = [
    path("", SentenceList.as_view(), name="sentence_list"),
    path("<int:pk>", SentenceDetail.as_view(), name="sentence_detail")
] 