from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='posts'),
    path('<slug:slug>', views.post_detail, name='post-details') #posts/my-first-post
]
