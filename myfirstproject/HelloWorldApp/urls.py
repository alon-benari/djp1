from django.conf.urls import include, url
from . import views
from django.views.generic.base import TemplateView

from django.contrib import admin


urlpatterns = [
    url(r'admin$', include(admin.site.urls)),
    url(r'index$', TemplateView.as_view(template_name='index.html'))
]
