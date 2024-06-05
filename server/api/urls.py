from django.urls import path
from .views import video_feed, start_camera, stop_camera

urlpatterns = [
    path('video_feed/', video_feed, name='video_feed'),
    path('start_camera/', start_camera, name='start_camera'),
    path('stop_camera/', stop_camera, name='stop_camera'),
]
