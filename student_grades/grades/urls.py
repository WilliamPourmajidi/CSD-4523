from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Default route to your index view
    path('result/', views.result, name='result'),  # Route to the result view
]