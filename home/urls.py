from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('lessons/', views.lessons, name='lessons'),
    path('lessons/<int:lesson_id>/', views.lesson_detail, name='lesson_detail'),  # New URL pattern
]