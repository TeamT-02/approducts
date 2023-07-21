# Generated by Django 4.2.2 on 2023-06-11 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eng', '0006_home_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home_project_about',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images_one', models.ImageField(upload_to='images/img/project/one/')),
                ('images_two', models.ImageField(upload_to='images/img/project/two/')),
                ('title', models.CharField(max_length=55)),
                ('text', models.TextField()),
            ],
        ),
    ]