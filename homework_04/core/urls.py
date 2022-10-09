from django.contrib import admin
from django.urls import path, include
import core.views


urlpatterns = [
    path("", core.views.Index.as_view()),
    path("persons/", core.views.PersonList.as_view()),
    # path("persons/<int:id>", core.views.person)
]
