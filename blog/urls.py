from django.urls import path
from .views import details, blog, articles_tag_list

urlpatterns = [
    path('', blog, name='blog'),
    path('<str:slug>/', details, name='details'),
    path('tag/<str:tag>/', articles_tag_list, name='articles_tag'),
]
