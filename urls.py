from django.conf.urls import url, patterns
from . import views

urlpatterns = [
    url(
        '^upload/(?P<upload_to>.*)/(?P<max_width>\d+)/(?P<max_height>\d+)/(?P<crop>\d+)',
        views.ajaximage,
        name='ajaximage'
    ),
]
