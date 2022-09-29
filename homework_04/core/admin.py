from django.contrib import admin
from core import models


class ItemResultInLine(admin.TabularInline):
    model = models.Person


