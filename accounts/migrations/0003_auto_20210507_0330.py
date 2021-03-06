# Generated by Django 3.2 on 2021-05-07 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_job_applied'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='fresh',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='job',
            name='interview',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='job',
            name='replied',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='job',
            name='response',
            field=models.BooleanField(default=False),
        ),
    ]
