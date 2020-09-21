from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from .views import SentenceViewSet
from .models import Sentences
from languages.models import Languages


SENTENCE_URL = reverse('sentence-list')
SAMPLE_TEXT = "Hello, Sample sentence"
SAMPLE_LANG = "sample"

def sample_sentence(language="sample"):
    lang = sample_language()
    return Sentences.objects.create(sentence_text=SAMPLE_TEXT, sentence_lang=lang)

def sample_language():
    return Languages.objects.create(lang_name=SAMPLE_LANG, lang_code=SAMPLE_LANG[:3], lang_type="local")


class SentenceAPITest(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view_list = SentenceViewSet.as_view({'get':'list','post':'create'})
        self.view_detail = SentenceViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})


    def test_list_all(self):     
        sample_sentence()
        response = self.view_list(self.factory.get(SENTENCE_URL))
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(len(response.data),1)
        self.assertEqual(response.data[0]['sentence_text'], SAMPLE_TEXT)


    def test_add_item_shouldPass(self): 
        sample_language()
        data = {"sentence_text": "Hi, "+SAMPLE_TEXT, "language":SAMPLE_LANG}
        response = self.view_list(self.factory.post(SENTENCE_URL, data))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['sentence_text'], data['sentence_text'])

    
    def test_detail_item_shouldPass(self):
        data = sample_sentence()
        response = self.view_detail(self.factory.get(SENTENCE_URL), pk=data.sentence_id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['sentence_text'], SAMPLE_TEXT)


    def test_remove_item_shouldPass(self):
        data = sample_sentence()
        request = self.factory.delete(SENTENCE_URL)
        response = self.view_detail(request, pk=data.sentence_id)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)