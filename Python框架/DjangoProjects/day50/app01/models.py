from django.db import models

# Create your models here.


class UserInfo(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=32)
    # def __str__(self):
    #     return self.username

class Book(models.Model):
    title = models.CharField(max_length=32)
    price = models.FloatField()
    publish_date = models.DateField()
    publish = models.CharField(max_length=32)

