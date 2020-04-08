from django.urls import path

from . import views

urlpatterns = [
    path('api/jokes/', views.joke_list, name='joke-list'),
    path('api/jokes/<int:pk>', views.joke_detail, name='joke-detail'),
]