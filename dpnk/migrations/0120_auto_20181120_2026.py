# Generated by Django 2.0.6 on 2018-11-20 20:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dpnk', '0119_auto_20180824_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='mailing_list_enabled',
            field=models.NullBooleanField(default=None, unique=True, verbose_name='Povolit mailing list'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='nickname',
            field=models.CharField(blank=True, help_text='Nechcete soutěžit pod svým skutečným jménem? Napište nám přezdívku, podle které Vás kolegové poznají.', max_length=60, null=True, verbose_name='Přezdívka'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='sex',
            field=models.CharField(choices=[('male', 'Muž'), ('female', 'Žena')], default=None, help_text='Tato informace se nám bude hodit při rozřazování do výkonnostních kategorií', max_length=50, null=True, blank=True, verbose_name='Pohlaví'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='telephone',
            field=models.CharField(help_text='Ozveme se, až bude balíček nachystaný.', max_length=30, validators=[django.core.validators.RegexValidator('^[0-9+ ]*$', 'Telefon musí být složen s čísel, mezer a znaku plus.'), django.core.validators.MinLengthValidator(9)], verbose_name='Telefonní číslo'),
        ),
    ]