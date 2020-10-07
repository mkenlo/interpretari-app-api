from rest_framework import viewsets, status,serializers
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import TranslationSerializer, AudioFileSerializer
from .models import Translation
from languages.models import Languages
from sentences.models import Sentences
from django.contrib.auth.models import User
from django.conf import settings 
from . import utils
import os

# Create your views here.
class TranslationViewSet(viewsets.ModelViewSet):
    serializer_class = TranslationSerializer
    queryset = Translation.objects.all()

    def perform_create(self, serializer):
        
        target_lang_id = self.request.data.get('target_lang')         
        target_lang = Languages.objects.get(lang_id=target_lang_id)
        
        sentence_id = self.request.data.get('sentence')
        sentence = Sentences.objects.get(sentence_id = sentence_id)
            
        author_id = self.request.data.get('author')
        author = User.objects.get(id=author_id)
        if sentence.sentence_lang == target_lang:
            raise serializers.ValidationError('Target Language must not be equal to Sentence Language')
        
        if serializer.is_valid():
            serializer.save(author = author, sentence = sentence, target_lang = target_lang)
        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )       
   
    
    @action(methods=['POST'], detail=True, url_path="upload")
    def upload_audio(self, request, pk=None):
        # upload audio translation file 
        
        translation = self.get_object() # fetch the translation object with the id in the request
        serializer = AudioFileSerializer(translation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


    @action(methods=['GET', 'POST'], detail=False, url_path="export/(?P<source>[^/]+)/(?P<target>[^/]+)")
    def export(self, request, source, target):
        return Response(
            status = status.HTTP_200_OK,
            data = utils.export_translation_per_language(source, target)
        )
    
    @action(methods=['GET'], detail=False, url_path="files/(?P<filename>[^/]+)")
    def files(self, request, filename):
        return Response(
            status = status.HTTP_200_OK,
            data = {"detail":"File is about to be downloaded"}
        )
        