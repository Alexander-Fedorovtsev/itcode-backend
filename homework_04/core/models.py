from django.db import models


class Person(models.Model):
    name = models.CharField("Имя", max_length=255)
    phone = models.IntegerField("Номер телефона")

"""class ItemResult(models.Model):
    item ="""

