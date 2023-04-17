from django.db import models

class AdvertisingCampaign(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    views = models.IntegerField(default=0)
    clicks = models.IntegerField(default=0)
