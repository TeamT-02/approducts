# Generated by Django 4.2.2 on 2023-06-11 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eng', '0002_home_about'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='home_about',
            name='images_two',
        ),
    ]