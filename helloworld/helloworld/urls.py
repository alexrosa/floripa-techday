"""helloworld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib import admin

from restaurant.views import RestaurantView
from restaurant.views import RestaurantListView

urlpatterns = [
    path('restaurant-list/', RestaurantListView.as_view(), name='restaurant-list'),
    path('restaurant-add/<int:user_id>/',
         RestaurantView.as_view(), name='restaurant'),
    path('restaurant/', RestaurantView.as_view(), name='home'),
]
