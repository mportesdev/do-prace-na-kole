# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-16 12:49
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('dpnk', '0003_tshirtsize_price'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TeamInCampaign',
        ),
        migrations.AlterModelOptions(
            name='competition',
            options={'ordering': ('-campaign', 'type', 'name'), 'verbose_name': 'Soutěžní kategorie', 'verbose_name_plural': 'Soutěžní kategorie'},
        ),
        migrations.AlterModelManagers(
            name='subsidiary',
            managers=[
                ('active_objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='campaign',
            name='benefitial_admission_fee_company',
            field=models.FloatField(default=0, verbose_name='Benefiční startovné pro firmy'),
        ),
        migrations.AlterField(
            model_name='company',
            name='address_city',
            field=models.CharField(default='', help_text='Např. „Jablonec n. N.“ nebo „Praha 3, Žižkov“', max_length=50, verbose_name='Město'),
        ),
        migrations.AlterField(
            model_name='company',
            name='address_psc',
            field=models.IntegerField(default=None, help_text='Např.: „130 00“', null=True, validators=[django.core.validators.MaxValueValidator(99999), django.core.validators.MinValueValidator(10000)], verbose_name='PSČ'),
        ),
        migrations.AlterField(
            model_name='company',
            name='address_recipient',
            field=models.CharField(blank=True, default='', help_text='Např. „odštěpný závod Brno“, „oblastní pobočka Liberec“, „Přírodovědecká fakulta“ atp.', max_length=50, null=True, verbose_name='Název pobočky (celé společnosti, závodu, kanceláře, fakulty) na adrese'),
        ),
        migrations.AlterField(
            model_name='company',
            name='address_street',
            field=models.CharField(default='', help_text='Např. „Šeříková“ nebo „Nám. W. Churchilla“', max_length=50, verbose_name='Ulice'),
        ),
        migrations.AlterField(
            model_name='company',
            name='address_street_number',
            field=models.CharField(default='', help_text='Např. „2965/12“ nebo „156“', max_length=10, verbose_name='Číslo domu'),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(help_text='Např. „Výrobna, a.s.“, „Příspěvková, p.o.“, „Nevládka, z.s.“, „Univerzita Karlova“', max_length=60, unique=True, verbose_name='Název společnosti'),
        ),
        migrations.AlterField(
            model_name='subsidiary',
            name='address_city',
            field=models.CharField(default='', help_text='Např. „Jablonec n. N.“ nebo „Praha 3, Žižkov“', max_length=50, verbose_name='Město'),
        ),
        migrations.AlterField(
            model_name='subsidiary',
            name='address_psc',
            field=models.IntegerField(default=None, help_text='Např.: „130 00“', null=True, validators=[django.core.validators.MaxValueValidator(99999), django.core.validators.MinValueValidator(10000)], verbose_name='PSČ'),
        ),
        migrations.AlterField(
            model_name='subsidiary',
            name='address_recipient',
            field=models.CharField(blank=True, default='', help_text='Např. „odštěpný závod Brno“, „oblastní pobočka Liberec“, „Přírodovědecká fakulta“ atp.', max_length=50, null=True, verbose_name='Název pobočky (celé společnosti, závodu, kanceláře, fakulty) na adrese'),
        ),
        migrations.AlterField(
            model_name='subsidiary',
            name='address_street',
            field=models.CharField(default='', help_text='Např. „Šeříková“ nebo „Nám. W. Churchilla“', max_length=50, verbose_name='Ulice'),
        ),
        migrations.AlterField(
            model_name='subsidiary',
            name='address_street_number',
            field=models.CharField(default='', help_text='Např. „2965/12“ nebo „156“', max_length=10, verbose_name='Číslo domu'),
        ),
        migrations.AlterField(
            model_name='subsidiary',
            name='city',
            field=models.ForeignKey(help_text="Rozhoduje o tom, do soutěží jakého města budete zařazeni a kde budete dostávat ceny - vizte <a href='http://www.dopracenakole.cz/pravidla' target='_blank'>pravidla soutěže</a>", on_delete=django.db.models.deletion.CASCADE, to='dpnk.City', verbose_name='Spádové město'),
        ),
    ]
