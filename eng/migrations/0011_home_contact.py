# Generated by Django 4.2.2 on 2023-06-13 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eng', '0010_testimonials'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home_Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.TextField()),
            ],
        ),
    ]
