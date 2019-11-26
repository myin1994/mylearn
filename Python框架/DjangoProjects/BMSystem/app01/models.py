from django.db import models


# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=10,blank=True)
    password = models.CharField(max_length=32,blank=True)


class Author(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()

class AuthorDetail(models.Model):
    birthday = models.DateField()
    telephone = models.CharField(max_length=16)
    addr = models.CharField(max_length=64)
    au = models.OneToOneField(to="Author",to_field="id",on_delete=models.CASCADE)

class Publish(models.Model):
    name = models.CharField(max_length=32)
    city = models.CharField(max_length=32)

class Book(models.Model):
    title = models.CharField(max_length=32)
    price = models.FloatField()
    publish_date = models.DateField()
    publishs = models.ForeignKey(to="Publish", to_field="id",
                                on_delete=models.CASCADE)
    authors = models.ManyToManyField(to='Author', )
    def __str__(self):
        return f"{self.id}|{self.title}|{self.price}|{self.publish_date}|{self.publishs}"
