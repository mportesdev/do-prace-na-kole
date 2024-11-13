# Generated by Django 2.2.28 on 2024-11-13 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dpnk', '0177_userprofile_newsletter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='newsletter',
            field=models.CharField(blank=True, choices=[('challenge', 'Výzva'), ('events', 'Události'), ('mobility', 'Mobilita'), ('challenge-events', 'Výzva a události'), ('challenge-mobility', 'Výzva a mobilita'), ('events-mobility', 'Události a mobilita'), ('challenge-events-mobility', 'Výzva, události a mobilita')], help_text='Odběr e-mailů můžete kdykoliv v průběhu soutěže zrušit.', max_length=30, null=True, verbose_name='Odběr zpráv prostřednictvím e-mailů'),
        ),
    ]
