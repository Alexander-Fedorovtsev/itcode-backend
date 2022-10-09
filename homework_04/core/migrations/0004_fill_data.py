from django.db import migrations, models


def fill_items(apps, schema):
    Item = apps.get_model("core", "Item")
    Item.objects.create(name="Купить молока к чаю")

def clear_items(apps, schema):
    Item = apps.get_model("core", "Item")
    Item.objects.filter(name="Купить молока к чаю").delete()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_item'),
    ]

    operations = [
        migrations.RunPython(
            code=fill_items,
            reverse_code=clear_items,
        )

    ]

