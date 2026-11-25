from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepageViews, name='homepage')
]