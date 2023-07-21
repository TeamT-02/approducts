# Generated by Django 4.2.2 on 2023-06-15 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eng', '0012_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=60)),
                ('subject', models.CharField(max_length=150)),
                ('text', models.TextField()),
            ],
        ),
    ]