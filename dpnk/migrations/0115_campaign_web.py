# Generated by Django 2.0.3 on 2018-08-10 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dpnk', '0114_auto_20180809_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='web',
            field=models.URLField(blank=True, default='http://www.dopracenakole.cz', verbose_name='Web kampáně'),
        ),
    ]