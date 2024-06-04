from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_bananas, name='all_bananas'),
]
