from django.db import models

# Create your models here.
class Languages(models.Model):
    LANG_TYPE = [
        ('local', 'local'),
        ('foreign', 'foreign')
    ]
    lang_id = models.AutoField(primary_key=True)
    lang_code = models.CharField(max_length=3, unique=True)
    lang_name = models.CharField(max_length=100)
    lang_type = models.CharField(max_length=100, choices=LANG_TYPE,default='foreign')


    def __str__(self):
        return self.lang_name