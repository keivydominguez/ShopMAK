# Generated by Django 2.2 on 2019-04-22 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_auto_20190405_1828'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productos',
            name='Foto_producto',
        ),
        migrations.CreateModel(
            name='Imagenes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='img/')),
                ('producto_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='productos.Productos')),
            ],
        ),
    ]