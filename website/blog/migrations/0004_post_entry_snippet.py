# Generated by Django 2.0.7 on 2018-08-02 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180802_0044'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='entry_snippet',
            field=models.TextField(default='', max_length=1000),
            preserve_default=False,
        ),
    ]