# Generated by Django 2.2.7 on 2020-01-22 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='company',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]