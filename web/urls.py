"""
Url definition file to redistribute incoming URL requests to django
views. Search the Django documentation for "URL dispatcher" for more
help.

"""
from django.conf.urls import url, include

# default evennia patterns
from evennia.web.urls import urlpatterns
import views as web_views


# eventual custom patterns
custom_patterns = [
    url(r'^chargen/', include('web.chargen.urls',
                              namespace='chargen', app_name='chargen')),
    url(r'^charinfo/', include('web.charinfo.urls',
                               namespace='charinfo', app_name='charinfo')),
    url(r'^curses/', include('web.curses.urls',
                             namespace='curses', app_name='curses')),
    url(r'^areas/', include('web.areas.urls',
                            namespace='areas', app_name='areas')),
    url(r'^faqs/', web_views.page_faqs, name='faqs'),
    url(r'^features/', web_views.page_features, name='features'),
    url(r'^$', web_views.page_index, name="index"),
]

# this is required by Django.
urlpatterns = custom_patterns + urlpatterns