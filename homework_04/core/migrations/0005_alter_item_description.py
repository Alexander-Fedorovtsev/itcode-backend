# Generated by Django 3.2.15 on 2022-10-09 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_fill_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(blank=True, help_text='Описание модельки', verbose_name='Описание'),
        ),
    ]