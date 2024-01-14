from django.urls import path
from . import views

urlpatterns = [
    path('', views.ma_vue, name='ma_vue'),
    path('page2/', views.page2, name='page2'),
]
