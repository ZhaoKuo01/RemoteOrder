# Generated by Django 4.0.3 on 2022-06-05 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='ordernum',
            field=models.IntegerField(default=0),
        ),
    ]
