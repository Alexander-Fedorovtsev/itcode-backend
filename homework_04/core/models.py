from django.db import models


class Person(models.Model):
    name = models.CharField("Имя", max_length=255)
    phone = models.IntegerField("Номер телефона")

    class Meta:
        verbose_name = "Человек"
        verbose_name_plural = "Люди"

    def __str__(self):
        return self.name


"""class ItemResult(models.Model):
    item ="""
