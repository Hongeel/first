# Generated by Django 2.2.7 on 2019-12-03 13:25

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0005_auto_20191203_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='Содержимое'),
        ),
    ]
