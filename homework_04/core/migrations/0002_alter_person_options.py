# Generated by Django 3.2.15 on 2022-10-02 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': 'Человек', 'verbose_name_plural': 'Люди'},
        ),
    ]
