from django.conf.urls import url
import views

urlpatterns = [
    # ex: /chargen/
    url(r'^$', views.page_index, name='index'),
    # ex: /chargen/5/
    #url(r'^(?P<app_id>[0-9]+)/$', views.detail, name='detail'),
]
