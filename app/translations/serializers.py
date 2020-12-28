
from rest_framework import serializers
from .models import Translation


class TranslationSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    sentence = serializers.StringRelatedField()
    target_lang = serializers.StringRelatedField()

    class Meta:
        model = Translation
        fields = ['translation_id', 'author', 'sentence',
                  'target_lang', 'audiofile', 'recorded_on']


class AudioFileSerializer(serializers.ModelSerializer):
    """Serializer for uploading audio files to translations object"""
    class Meta:
        model = Translation
        fields = ('translation_id', 'audiofile')
        read_only_fields = ('translation_id',)
