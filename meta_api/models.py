from django.db import models

class Ticks(models.Model):
    name = models.CharField(max_length=20)

# Create your models here.
