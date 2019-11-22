from django.db import models


# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=32)


class Authors(models.Model):  # 比较常用的信息放到这个表里面
    name = models.CharField(max_length=32)
    age = models.IntegerField()

    au_detail = models.OneToOneField(to="AuthorDetail", to_field="id",
                                        on_delete=models.CASCADE)


class AuthorDetail(models.Model):  # 不常用的放到这个表里面

    birthday = models.DateField()
    telephone = models.CharField(max_length=16)
    addr = models.CharField(max_length=64)


class Publishs(models.Model):
    name = models.CharField(max_length=32)
    city = models.CharField(max_length=32)

class Book(models.Model):
    title = models.CharField(max_length=32)
    price = models.FloatField()
    publish_date = models.DateField()
    # publish = models.CharField(max_length=32)

    publish = models.ForeignKey(to="Publishs", to_field="id",
                                on_delete=models.CASCADE)
    author = models.ManyToManyField(to='Authors', )
    def __str__(self):
        return f"{self.id}|{self.title}|{self.price}|{self.publish_date}|{self.publish}"
