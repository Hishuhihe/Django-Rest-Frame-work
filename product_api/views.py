from rest_framework import generics
from .models import AdvertisingCampaign
from .serializers import AdvertisingCampaignSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
import requests


class AdvertisingCampaignList(generics.ListCreateAPIView):
    queryset = AdvertisingCampaign.objects.all()
    serializer_class = AdvertisingCampaignSerializer

class AdvertisingCampaignDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AdvertisingCampaign.objects.all()
    serializer_class = AdvertisingCampaignSerializer


class AdvertisingCampaignReport(generics.RetrieveAPIView):
    queryset = AdvertisingCampaign.objects.all()
    serializer_class = AdvertisingCampaignSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        click_through_rate = instance.clicks / instance.views if instance.views > 0 else 0
        report = {
            'name': instance.name,
            'description': instance.description,
            'start_date': instance.start_date,
            'end_date': instance.end_date,
            'views': instance.views,
            'clicks': instance.clicks,
            'click_through_rate': click_through_rate
        }
        return Response(report)


#Post 
class FacebookPosts(APIView):
    def get(self, request, format=None):
        access_token = 'Page_token'
        page_id = 'id'
        url = f'https://graph.facebook.com/v12.0/{page_id}/posts?fields=id,message,created_time,insights.metric(post_impressions,post_clicks)&access_token={access_token}'
        response = requests.get(url)
        data = response.json()
        return Response(data)