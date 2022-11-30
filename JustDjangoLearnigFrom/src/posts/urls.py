from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('posts/<int:pk>/', views.post, name='post'),
    path('blog/', views.blog, name='blog'),
]
