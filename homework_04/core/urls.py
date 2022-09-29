from django.contrib import admin
from django.urls import path, include
import core


urlpatterns = [
    path("", core.views.index),
]
