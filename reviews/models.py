from django.db import models
# Create your models here.

class Reviews(models.Model):
    review_name = models.CharField(max_length=32)
    def all_categories():
        return Reviews.objects.all()
    def __str__(self):
        return self.review_name
