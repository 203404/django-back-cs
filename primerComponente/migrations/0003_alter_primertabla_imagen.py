# Generated by Django 4.0.1 on 2022-02-02 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primerComponente', '0002_primertabla_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='primertabla',
            name='imagen',
            field=models.ImageField(blank='', default='', upload_to='media/'),
        ),
    ]