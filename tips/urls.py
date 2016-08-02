from django.conf.urls import url
from . import views

app_name = 'tips'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<section_id>\d+)/section/$', views.section, name='section'),
]