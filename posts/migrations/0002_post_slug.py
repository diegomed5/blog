# Generated by Django 4.1.2 on 2022-10-13 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='fix-me'),
            preserve_default=False,
        ),
    ]
