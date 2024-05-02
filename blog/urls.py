from django.contrib import admin
from django.urls import path,include
from blog import views

urlpatterns = [
    path('', views.blogPage , name = 'blogPage'),
    path('<str:slug>' ,views.blogPost , name='blogPost')
]