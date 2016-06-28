from django.conf.urls import url
from views import sheet

urlpatterns = [
    url(r'^(?P<char_name>\w+)/$', sheet, name="sheet")
]