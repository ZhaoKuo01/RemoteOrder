# Generated by Django 4.0.3 on 2022-04-27 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='description',
            field=models.CharField(default='小可爱', max_length=35),
        ),
    ]
