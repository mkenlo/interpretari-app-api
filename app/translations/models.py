import os
from django.db import models
from django.contrib.auth.models import User
from sentences.models import Sentences 
from languages.models import Languages


def translation_directory_path(instance, filename):
    source = instance.sentence.sentence_lang.lang_code
    target = instance.target_lang.lang_code
    return "_".join([source.lower(), target.lower(), filename.lower()])


class Translation(models.Model):
    translation_id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    sentence = models.ForeignKey(Sentences, on_delete=models.CASCADE, related_name='translations')
    target_lang = models.ForeignKey(Languages, on_delete=models.CASCADE)
    audiofile = models.FileField(upload_to=translation_directory_path, null=True)
    recorded_on = models.DateTimeField(auto_now_add=True)



