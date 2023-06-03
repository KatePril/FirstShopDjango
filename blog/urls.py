from django.urls import path
from .views import *

urlpatterns = [
    path('search/', search, name='search'),
    path('', blog, name='blog'),
    path('<str:slug>/', details, name='details'),
    path('tag/<str:tag>/', articles_tag_list, name='articles_tag'),
]
