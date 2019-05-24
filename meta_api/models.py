from django.db import models

class Bars(models.Model):
    pair = models.CharField(max_length=20)
    timeframe = models.CharField(max_length=5)
    datetime = models.DateTimeField()
    high = models.FloatField()
    low = models.FloatField()
    open = models.FloatField()
    close = models.FloatField()

    def __str__(self):
        return self.pair + ' ' + self.timeframe + ' ' + str(self.datetime)
# Create your models here.
