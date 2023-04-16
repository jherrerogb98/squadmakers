
from django.contrib import admin
from django.urls import path, include
from jokes import views

urlpatterns = [
    path('jokes', views.JokeView.as_view(), name='JokeView'),
    path('jokes/<int:joke_id>/', views.JokeViewbyId.as_view(), name='Joke View by Id'),
    path('get_random/', views.get_random, name='get random'),
    path('get_random/<str:type_joke>', views.get_random, name='get random'),
    path('get_mcm/', views.get_mcm, name='get random'),
]
