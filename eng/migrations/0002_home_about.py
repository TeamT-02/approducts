# Generated by Django 4.2.2 on 2023-06-11 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eng', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home_about',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images_one', models.ImageField(upload_to='images/img/about/')),
                ('images_two', models.ImageField(upload_to='images/img/about/')),
                ('title', models.CharField(max_length=45)),
                ('text', models.TextField()),
            ],
        ),
    ]
