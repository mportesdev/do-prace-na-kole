# Generated by Django 2.0.9 on 2019-01-19 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stravasync', '0003_auto_20181120_2026'),
    ]

    operations = [
        migrations.AddField(
            model_name='stravaaccount',
            name='refresh_token',
            field=models.CharField(default='', max_length=256),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='stravaaccount',
            name='access_token',
            field=models.CharField(max_length=256),
        ),
    ]
