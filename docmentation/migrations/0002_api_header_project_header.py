# Generated by Django 4.2.1 on 2023-05-13 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docmentation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='api',
            name='header',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='project',
            name='header',
            field=models.BooleanField(default=False),
        ),
    ]
