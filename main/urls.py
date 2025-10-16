from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sevval/', views.sevval, name='sevval'),
    path('merve/', views.merve, name="merve")
]