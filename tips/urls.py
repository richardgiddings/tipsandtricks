from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

app_name = 'tips'
urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='tips/index.html'), name='index'),
]