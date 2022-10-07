from django.contrib import admin
from django.urls import path, include
import core.views


urlpatterns = [
    path("", core.views.index),
    path("persons/", core.views.persons),
    path("persons/<int:id>", core.views.person)
]
