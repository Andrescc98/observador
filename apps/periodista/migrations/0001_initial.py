# Generated by Django 2.2.4 on 2019-09-14 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Periodista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(blank=True, max_length=30)),
                ('correo', models.EmailField(max_length=254)),
                ('descripcion', models.TextField()),
            ],
        ),
    ]
