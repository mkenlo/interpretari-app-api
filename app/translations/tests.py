from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from .views import TranslationViewSet
from .models import Translation
from languages.models import Languages
from sentences.models import Sentences
from django.contrib.auth.models import User, Group

TRANSLATION_URL = reverse('translation-list')
SAMPLE_TEXT = "Hello, Sample sentence"

def sample_sentence(language="sample"):
    lang = sample_language()
    return Sentences.objects.create(sentence_text=SAMPLE_TEXT, sentence_lang=lang)


def sample_language(name="sample"):
    return Languages.objects.create(lang_name=name, lang_code=name[:3], lang_type="local")


def test_user():
    return User.objects.create(username="testy", first_name="test", last_name="test")


def sample_translation():
    user = test_user()
    sentence = sample_sentence()
    lang = sample_language("test")
    return Translation.objects.create(author=user, sentence = sentence, target_lang=lang)
    

class TranslationAPITest(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view_list = TranslationViewSet.as_view({'get':'list','post':'create'})
        self.view_detail = TranslationViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})
    

    def test_list_all(self):     
        data = sample_translation()
        response = self.view_list(self.factory.get(TRANSLATION_URL))
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(len(response.data),1)
        self.assertEqual(response.data[0]['sentence'], data.sentence.sentence_text)


    def test_add_item_shouldPass(self): 
        user = test_user()
        first = sample_language("first")
        text = sample_sentence()
        data = {"sentence": text.sentence_id, "target_lang": first.lang_id, "author":user.id}
        response = self.view_list(self.factory.post(TRANSLATION_URL, data))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_detail_item_shouldPass(self):
        data = sample_translation()
        response = self.view_detail(self.factory.get(TRANSLATION_URL), pk=data.translation_id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['sentence'], SAMPLE_TEXT)

    def test_upload_audio_shouldPass(self):
        data = sample_translation()
        request = self.factory.post("/", "file")