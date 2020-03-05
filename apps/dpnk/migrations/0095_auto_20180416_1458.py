# Generated by Django 2.0.4 on 2018-04-16 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dpnk', '0094_auto_20180412_1730'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='campaign',
            options={'permissions': (('can_see_application_links', 'Can see application links'),), 'verbose_name': 'kampaň', 'verbose_name_plural': 'kampaně'},
        ),
        migrations.AddField(
            model_name='campaign',
            name='show_application_links',
            field=models.BooleanField(default=False, verbose_name='Ukázat odkazy na aplikace'),
        ),
    ]