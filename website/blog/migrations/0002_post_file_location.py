# Generated by Django 2.0.7 on 2018-08-01 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='file_location',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
    ]
