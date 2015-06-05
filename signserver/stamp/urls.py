from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from stamp import views

urlpatterns = [
    url(r'^$', views.StampAdd.as_view()),
    url(r'^(?P<refid>[0-9]+)/$', views.StampDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)