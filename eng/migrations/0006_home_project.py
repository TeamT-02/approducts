# Generated by Django 4.2.2 on 2023-06-11 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eng', '0005_home_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home_project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='images/img/project/')),
                ('title', models.CharField(max_length=30)),
            ],
        ),
    ]
