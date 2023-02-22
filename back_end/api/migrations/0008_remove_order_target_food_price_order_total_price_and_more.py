# Generated by Django 4.0.3 on 2022-06-02 08:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_account_charactor_alter_order_state_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='target',
        ),
        migrations.AddField(
            model_name='food',
            name='price',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='total_price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='account',
            name='charactor',
            field=models.SmallIntegerField(choices=[(1, '小吃铺'), (2, '消费者')], default='消费者', verbose_name='identity'),
        ),
        migrations.AlterField(
            model_name='food',
            name='score',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='state',
            field=models.SmallIntegerField(choices=[(1, '已下单'), (2, '摊主已接单'), (3, '订单已完成')]),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='location',
            field=models.SmallIntegerField(choices=[(1, '小区1'), (2, '小区2'), (3, '小区3')], verbose_name='location'),
        ),
        migrations.CreateModel(
            name='OrderandFood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now=True)),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.food')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.order')),
            ],
        ),
    ]