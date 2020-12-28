
from rest_framework import serializers
from .models import Sentences
from languages.serializers import LanguageSerializer


class SentenceSerializer(serializers.ModelSerializer):
    sentence_lang = serializers.StringRelatedField()

    class Meta:
        model = Sentences
        fields = ['sentence_id', 'sentence_text', 'sentence_lang']
