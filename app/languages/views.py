from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Languages
from .serializers import LanguageSerializer
from rest_framework import viewsets
# Create your views here.


class LanguageList(ListCreateAPIView):
    serializer_class = LanguageSerializer
    queryset = Languages.objects.all()
    
    def get_queryset(self):
        lang_type = self.request.query_params.get('language_type')
        queryset = Languages.objects.all()
        if lang_type:
            queryset = queryset.filter(lang_type=lang_type)
        return queryset
    
    
class LanguageDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = LanguageSerializer
    queryset = Languages.objects.all()

