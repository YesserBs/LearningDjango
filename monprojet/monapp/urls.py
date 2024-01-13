from django.urls import path
from . import views

urlpatterns = [
    path('', views.ma_vue, name='ma_vue'),
]
