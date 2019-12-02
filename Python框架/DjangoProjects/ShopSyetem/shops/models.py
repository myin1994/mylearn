from django.db import models
import datetime

# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=18, blank=False, unique=True)
    password = models.CharField(max_length=32, blank=False)
    role = models.IntegerField(blank=True, default=0)

class Goods(models.Model):
    gname = models.CharField(max_length=20, blank=False)
    price = models.FloatField(blank=False)

class ShopCar(models.Model):
    user = models.ForeignKey(
        to="UserInfo",
        to_field="id",
        on_delete=models.CASCADE
    )
    mygoods = models.ForeignKey(
        to="Goods",
        to_field="id",
        on_delete=models.CASCADE
    )
    gnumber = models.IntegerField(blank=False,default=1)

class Order(models.Model):
    user = models.ForeignKey(
        to="UserInfo",
        to_field="id",
        on_delete=models.CASCADE
    )
    m = models.ManyToManyField(to='Goods',through='OrderGoods', through_fields=('order1', 'goods1'))
    order_price = models.FloatField(blank=False,default=0)
    order_date = models.DateTimeField(auto_now=True)

class OrderGoods(models.Model):
    order1 = models.ForeignKey('Order')
    goods1 = models.ForeignKey('Goods')
    goods_number = models.IntegerField(blank=False,default=1)
