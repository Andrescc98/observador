# Generated by Django 2.2.4 on 2019-09-14 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articulo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='f_publicacion',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
