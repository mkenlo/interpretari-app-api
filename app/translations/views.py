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


class TranslationViewSet(viewsets.ModelViewSet):
    serializer_class = TranslationSerializer
    queryset = Translation.objects.all()

    def get_queryset(self):
       
        queryset = Translation.objects.all()
        userid = self.request.query_params.get('author', None)
        sentenceid = self.request.query_params.get('sentence', None)
        source_lang_id = self.request.query_params.get('source_language', None)
        target_lang_id = self.request.query_params.get('target_language', None)
        if userid:
            queryset = queryset.filter(author__pk=userid)
        if sentenceid:
            queryset = queryset.filter(sentence__pk=sentenceid)
        if source_lang_id:
            queryset = queryset.filter(source_lang__pk=sentenceid)
        if sentenceid:
            queryset = queryset.filter(target_lang__pk=sentenceid)
        return queryset

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


    @action(methods=['GET'], detail=False, url_path="export/(?P<source>[^/]+)/(?P<target>[^/]+)")
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
        