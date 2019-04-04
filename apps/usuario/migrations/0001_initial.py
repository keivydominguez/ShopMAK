# Generated by Django 2.2 on 2019-04-04 21:17

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('Usario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('Telefono', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('Calle', models.CharField(max_length=50)),
                ('Colonia', models.CharField(max_length=50)),
                ('CodigoPostal', models.CharField(max_length=5)),
                ('Municipio', models.CharField(max_length=50)),
                ('Estado', models.CharField(max_length=50)),
                ('Pais', models.CharField(max_length=20)),
            ],
        ),
    ]