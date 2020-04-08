from django.urls import path

from . import views

urlpatterns = [
    path('api/prompts/random/', views.prompt_random, name='prompt-random'),
]