# Generated by Django 5.2.3 on 2025-07-02 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='description',
            field=models.TextField(help_text='Team member description', max_length=1000),
        ),
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(help_text='Team member name', max_length=100),
        ),
        migrations.AlterField(
            model_name='team',
            name='position',
            field=models.CharField(help_text='Team member position', max_length=100),
        ),
    ]
