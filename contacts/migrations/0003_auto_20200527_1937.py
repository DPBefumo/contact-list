# Generated by Django 3.0.5 on 2020-05-27 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_contact_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='birthday',
            field=models.DateField(blank=True, max_length=255, null=True),
        ),
    ]