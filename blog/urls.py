from django.conf.urls import url
from . import views

# 정규표현식 부분 안된다. 
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'post/(?P<pk>\d+)/$', views.post_detail, name='post_detail')
]