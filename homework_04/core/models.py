import datetime
from django.utils.timezone import now
from django.db import models




class Item(models.Model):
    name = models.CharField("Название", max_length=255, blank=True, null=True, unique=True)
    description = models.TextField("Описание", help_text="Описание модельки", blank=True)
    priority = models.IntegerField("приоритет сортировки", default=1, db_index=True)
    done = models.DateTimeField("выполнено", null=True, blank=True, editable=False)
    created = models.DateTimeField("Создан", auto_now_add=True)
    update = models.DateTimeField("Обновлен", auto_now=True)
    deleted = models.DateTimeField("время удаления", auto_now=True)

    class Meta:
        verbose_name = "Дела"
        verbose_name_plural = "Список дел"
        ordering = ("priority", "created")

    def __str__(self):
        return self.name

    def duration(self) -> datetime.timedelta:
        return now() - self.created


class ItemResult(models.Model):
    item = models.OneToOneField(Item, on_delete=models.CASCADE)
    image = models.ImageField()


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
