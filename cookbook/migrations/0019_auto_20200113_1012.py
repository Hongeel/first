# Generated by Django 2.2.7 on 2020-01-13 10:12

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0018_post_s_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='s_content',
            field=ckeditor_uploader.fields.RichTextUploadingField(max_length=650, null=True, verbose_name='Краткое сожержимое'),
        ),
    ]
