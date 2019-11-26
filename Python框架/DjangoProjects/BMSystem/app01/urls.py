from django.conf.urls import url
from app01.views import *
urlpatterns = [
    url(r'^login/', Login.as_view(),name="login"),
    url(r'^books/$', Books.as_view(),name="books"),
    url(r'^books/add/', AddBooks.as_view(),name="add_books"),
    url(r'^books/edit/', EditBooks.as_view(),name="edit_books"),
    url(r'^upload/', upload,name="upload"),
]