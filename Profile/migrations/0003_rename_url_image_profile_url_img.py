# Generated by Django 4.0.1 on 2022-03-10 05:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0002_profile_delete_tablaprofile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='url_image',
            new_name='url_img',
        ),
    ]