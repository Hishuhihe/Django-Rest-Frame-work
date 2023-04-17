from django.urls import path
from .views import AdvertisingCampaignList, AdvertisingCampaignDetail, AdvertisingCampaignReport, FacebookPosts

urlpatterns = [
    path('campaigns/', AdvertisingCampaignList.as_view(), name='campaign-list'),
    path('campaigns/<int:pk>/', AdvertisingCampaignDetail.as_view(), name='campaign-detail'),
    path('campaigns/report/<int:pk>', AdvertisingCampaignReport.as_view(), name='campaign-report'),
    path('facebook/posts/', FacebookPosts.as_view(), name='facebook_posts'),
]
