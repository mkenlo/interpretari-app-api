from languages.models import Languages
from .models import Sentences
from .serializers import SentenceSerializer
from rest_framework import viewsets
# Create your views here.


class SentenceViewSet(viewsets.ModelViewSet):
    serializer_class = SentenceSerializer
    queryset = Sentences.objects.all()
    
    def get_queryset(self):
        lang_name = self.request.query_params.get('language')
        queryset = Sentences.objects.all()
        if lang_name:
            lang = Languages.objects.filter(lang_name=lang_name).first()
            queryset = queryset.filter(sentence_lang=lang)
        return queryset
    
    def perform_create(self, serializer):
        name = self.request.data.get('language')
        lang = Languages.objects.filter(lang_name=name).first()
        serializer.save(sentence_lang = lang)
    
