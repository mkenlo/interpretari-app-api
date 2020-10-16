from languages.models import Languages
from .models import Sentences
from .serializers import SentenceSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
# Create your views here.


class SentenceViewSet(viewsets.ModelViewSet):
    serializer_class = SentenceSerializer
    queryset = Sentences.objects.all()
    
    def get_queryset(self):
        lang_name = self.request.query_params.get('language')
        istranslated= self.request.query_params.get('istranslated')
        queryset = Sentences.objects.all()
        if lang_name:
            queryset = queryset.filter(sentence_lang__lang_name=lang_name)
        if istranslated:
            if istranslated == "false":
                queryset  = queryset.filter(translations__isnull=True)
            elif istranslated == "true":
                queryset  = queryset.filter(translations__isnull=False)
        return queryset
    
    def perform_create(self, serializer):
        name = self.request.data.get('language')
        lang = Languages.objects.filter(lang_name=name).first()
        serializer.save(sentence_lang = lang)