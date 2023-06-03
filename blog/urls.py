from django.urls import path
from .views import details, blog

urlpatterns = [
    path('', blog, name='blog'),
    path('<str:slug>/', details, name='details'),
]
