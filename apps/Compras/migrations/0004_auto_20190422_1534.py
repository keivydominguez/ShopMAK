# Generated by Django 2.2 on 2019-04-22 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Compras', '0003_auto_20190405_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compras',
            name='Fecha_compras',
            field=models.DateField(),
        ),
    ]
