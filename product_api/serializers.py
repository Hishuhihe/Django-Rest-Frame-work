from rest_framework import serializers
from .models import AdvertisingCampaign

class AdvertisingCampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvertisingCampaign
        fields = '__all__'
