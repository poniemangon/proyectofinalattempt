# Generated by Django 4.0.5 on 2022-08-03 03:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_delete_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='imagen',
        ),
    ]
