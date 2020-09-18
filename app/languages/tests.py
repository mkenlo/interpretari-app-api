from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from .views import LanguageList, LanguageDetail
from .models import Languages


LANGUAGE_URL = reverse('language_list')


def sample_language(code):
    return Languages.objects.create(lang_name="Sample", lang_code=code, lang_type="local")


# Create your tests here.
class LanguageTest(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view_list = LanguageList.as_view()
        self.view_detail = LanguageDetail.as_view()
        self.data = {"lang_name":"Sample", "lang_code":"SAM", "lang_type":"local"}
               

    def test_list_all(self):     
        for i in range(5):
            sample_language(str(i))
        response = self.view_list(self.factory.get(LANGUAGE_URL))
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(len(response.data),5)


    def test_add_item_shouldPass(self):
        response = self.view_list(self.factory.post(LANGUAGE_URL, self.data))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['lang_name'], self.data['lang_name'])

    
    def test_detail_item_shouldPass(self):
        lang = sample_language("SAM")
        response = self.view_detail(self.factory.get(LANGUAGE_URL), pk=lang.lang_id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['lang_name'], lang.lang_name)

    
    def test_update_item_shouldPass(self):
        lang = sample_language("SAM")
        request = self.factory.put(LANGUAGE_URL, self.data, format="json")
        response = self.view_detail(request, pk=lang.lang_id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['lang_name'], self.data['lang_name'])
        

    def test_remove_item_shouldPass(self):
        lang = sample_language("SAM")
        request = self.factory.delete(LANGUAGE_URL)
        response = self.view_detail(request, pk=lang.lang_id)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


    def test_add_item_shouldFailed(self):
        self.data['lang_code'] = "INVALID CODE LENGTH"
        response = self.view_list(self.factory.post(LANGUAGE_URL, self.data))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)