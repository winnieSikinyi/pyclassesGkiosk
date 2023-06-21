from django.db import models
class Orders(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField()
