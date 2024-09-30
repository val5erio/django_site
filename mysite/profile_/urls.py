from django.urls import path
from . import views

urlpatterns = [
    path('', views.info_profile, name='info_profile'),
]
