from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

app_name = 'tips'
urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    url(r'^section/(?P<section_id>\d+)$', TemplateView.as_view(template_name='index.html'), name='index'),
]