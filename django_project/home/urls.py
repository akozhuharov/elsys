from django.urls import path
from home.views import index, create, detail

urlpatterns = [
    path('', index),
    path('create/', create),
    path('posts/<int:post_id>/', detail)
]