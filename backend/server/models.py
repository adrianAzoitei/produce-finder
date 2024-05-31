from django.db import models

class Produce(models.Model):
    name = models.CharField(max_length=256)
