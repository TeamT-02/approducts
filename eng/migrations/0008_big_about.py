# Generated by Django 4.2.2 on 2023-06-12 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eng', '0007_home_project_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='Big_About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('images_one', models.ImageField(upload_to='images/img/about_us/one/')),
                ('images_two', models.ImageField(upload_to='images/img/about_us/two/')),
                ('text', models.TextField()),
            ],
        ),
    ]
