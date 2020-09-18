
from rest_framework import serializers
from .models import Sentences


class SentenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sentences
        fields = ['sentence_id', 'sentence_text']