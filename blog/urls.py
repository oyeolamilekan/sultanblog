from django.conf.urls import url
from . import views


urlpatterns = [
    # post views
    url(r'^$', views.post_index, name='post_index'),
    url(r'^blog/$', views.post_list, name='post_list'),
    url(r'^feedback/$', views.feedback, name='feedback'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$',views.post_detail,name='post_detail'),
]