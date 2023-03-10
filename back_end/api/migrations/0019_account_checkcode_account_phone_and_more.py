# Generated by Django 4.0.3 on 2022-06-27 15:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_remove_restaurant_location_alter_order_create_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='checkcode',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='account',
            name='phone',
            field=models.CharField(default=12345678901, max_length=11),
        ),
        migrations.AlterField(
            model_name='order',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 27, 15, 23, 7, 962202, tzinfo=utc)),
        ),
    ]
