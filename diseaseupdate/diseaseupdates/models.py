from django.db import models

# Create your models here.
class Diseaseupdates(models.Model):
    symptoms = models.CharField(max_length=200)
    trends = models.CharField(max_length=20000)
    measures = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    