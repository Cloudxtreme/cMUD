from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.page_index, name='index'),
    url(r'^vampire/', views.page_vampire, name='vampire'),
    url(r'^werewolf/', views.page_werewolf, name='werewolf'),
    url(r'^genie/', views.page_genie, name='genie'),
]
