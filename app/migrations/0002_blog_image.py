# Generated by Django 4.1.2 on 2022-10-26 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to=''),
        ),
    ]
