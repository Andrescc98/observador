# Generated by Django 2.2.4 on 2019-09-14 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articulo', '0003_articulo_titulo'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='imagen',
            field=models.ImageField(blank=True, upload_to='imagen_articulo'),
        ),
    ]
