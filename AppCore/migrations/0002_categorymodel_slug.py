# Generated by Django 4.2 on 2023-06-03 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCore', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorymodel',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]