from django.db import models

class User(models.Model):
    user_id = models.UUIDField(primary_key=True)

class Detection(models.Model):
    bboxes = models.JSONField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

