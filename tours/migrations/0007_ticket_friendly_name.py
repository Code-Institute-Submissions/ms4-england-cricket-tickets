# Generated by Django 3.1.5 on 2021-02-06 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0006_ticket_match'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='friendly_name',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
