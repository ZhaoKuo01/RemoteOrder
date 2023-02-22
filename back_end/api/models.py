from django.db import models
import datetime
from pytz import timezone


# Create your models here.

# 账户
class Account(models.Model):
    username = models.CharField(max_length=20)
    nickname = models.CharField(max_length=10, default="给自己一个名称吧")
    password = models.CharField(max_length=20)
    email = models.EmailField(default="xxx@qq.com")
    charactor_choices = (
        (1, "小吃铺"),
        (2, "消费者"),
    )
    charactor = models.SmallIntegerField(verbose_name="identity", choices=charactor_choices, default="消费者")
    phone = models.CharField(max_length=11,default=12345678901)
    checkcode = models.SmallIntegerField(default=0)
    description = models.CharField(default="description test", max_length=35)

    def __str__(self):
        return self.username


# 商店信息
class Restaurant(models.Model):
    name = models.CharField(max_length=15)
    belong_to = models.ForeignKey(to="Account", to_field="id", on_delete=models.CASCADE)
    average_score = models.FloatField(default=4)

class ResandLocation(models.Model):
    res = models.ForeignKey(to="Restaurant",to_field="id",on_delete=models.CASCADE)
    location = models.CharField(max_length=20)


class Evaluation(models.Model):
    user = models.ForeignKey(to="Account", to_field="id", on_delete=models.CASCADE)
    res = models.ForeignKey(to="Restaurant", to_field="id", on_delete=models.CASCADE)
    content = models.TextField(max_length=50)
    target = models.ForeignKey(to="Food", to_field="id", on_delete=models.CASCADE)
    create_time = models.TimeField(auto_now=True)


class Food(models.Model):
    belong_to = models.ForeignKey(to="Restaurant", to_field="id", on_delete=models.CASCADE)
    name = models.CharField(max_length=15)
    description = models.CharField(max_length=30)
    score = models.FloatField(default=0)
    price = models.FloatField(default=0)
    ordernum = models.IntegerField(default=0)


class Order(models.Model):
    user = models.ForeignKey(to="Account", to_field="id", on_delete=models.CASCADE)
    res = models.ForeignKey(to="Restaurant", to_field="id", on_delete=models.CASCADE)
    username = models.CharField(max_length=20,default="zike")
    resname = models.CharField(max_length=20,default='店铺1')
    content = models.TextField(max_length=50)
    state_choices = (
        (1, "已下单"),
        (2, "摊主已接单"),
        (3, "订单已完成"),
    )
    cst_tz = timezone('Asia/Shanghai')
    t = datetime.datetime.now()
    t = cst_tz.localize(t)
    state = models.SmallIntegerField(choices=state_choices)
    create_time = models.DateTimeField(default=t)
    total_price = models.FloatField(default=0)


class OrderandFood(models.Model):
    order = models.ForeignKey(to="Order", on_delete=models.CASCADE)
    food = models.ForeignKey(to="Food", on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now=True)


class Token(models.Model):
    user = models.OneToOneField(to=Account, on_delete=models.CASCADE)
    token = models.CharField(max_length=64)
