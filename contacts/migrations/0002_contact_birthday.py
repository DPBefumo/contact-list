# Generated by Django 3.0.5 on 2020-05-27 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='birthday',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
