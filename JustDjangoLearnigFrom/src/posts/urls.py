from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('posts/<slug:slug>/', views.post_detail, name='post'),
    path('blog/', views.blog, name='blog'),
]
