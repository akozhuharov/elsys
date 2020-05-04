from django.urls import path
from home.views import index,create

urlpatterns = [
    path('', index),
    path('create/', create)
]