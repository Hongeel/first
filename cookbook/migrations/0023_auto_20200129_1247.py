# Generated by Django 2.2.9 on 2020-01-29 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0022_auto_20200129_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=80, verbose_name='Имя'),
        ),
    ]
