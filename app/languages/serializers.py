from rest_framework import serializers
from .models import Languages 
from sentences.serializers import SentenceSerializer

class LanguageSerializer(serializers.ModelSerializer):
    sentences = SentenceSerializer(many=True, read_only=True)
    class Meta:
        model = Languages
        fields = ['lang_id', 'lang_name', 'lang_code', 'lang_type', 'sentences']