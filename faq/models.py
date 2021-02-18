from django.db import models

# Create your models here.

class FAQ(models.Model):
    name = models.CharField(max_length=254)
    question = models.CharField(max_length=254, null=False, blank=False)
    answer = models.CharField(max_length=254, null=False, blank=False)

    def __str__(self):
        return self.name

    