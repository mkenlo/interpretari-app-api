from django.db import models
from languages.models import Languages


# Create your models here.
class Sentences(models.Model):
    sentence_id = models.AutoField(primary_key=True)
    sentence_text = models.CharField(max_length=300)
    sentence_lang= models.ForeignKey(Languages, related_name='sentences',on_delete=models.CASCADE)

    def __str__(self):
        return self.sentence_text



