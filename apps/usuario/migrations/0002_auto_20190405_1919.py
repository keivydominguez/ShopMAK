# Generated by Django 2.2 on 2019-04-05 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='Telefono',
            field=models.CharField(max_length=16),
        ),
    ]
