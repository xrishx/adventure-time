# Generated by Django 5.2.3 on 2025-07-02 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_alter_team_description_alter_team_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='team',
            options={'verbose_name': 'Team Member', 'verbose_name_plural': 'Team Members'},
        ),
    ]
