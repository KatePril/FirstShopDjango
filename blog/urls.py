from django.urls import path
from .views import details, blog

urlpatterns = [
    path('', blog, name='blog'),
    path('<int:id>/', details, name='details'),
]
