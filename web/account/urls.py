from django.conf.urls import url
from django.contrib.auth.views import login, logout
import views

urlpatterns = [
    url(r'^$', views.page_index, name='index'),
    url(r'^login/$', login, {'template_name': 'account/login.html'}, name="login"),
    url(r'^logout/$', logout, {'next_page': '/'}, name="logout"),
]
