from django.conf.urls import url
from app01.views import *
urlpatterns = [
    url(r'^login/',Login.as_view()),
    url(r'^books/',Books.as_view()),
]