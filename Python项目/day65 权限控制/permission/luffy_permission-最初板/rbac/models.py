from django.db.models import *

# Create your models here.
class UserInfo(Model):
    username = CharField(max_length=32)
    password = CharField(max_length=32)
    roles = ManyToManyField("Role")
    def __str__(self):
        return self.username

class Role(Model):
    role_name = CharField(max_length=32)
    permissions = ManyToManyField('Permission')
    def __str__(self):
        return self.role_name


class Permission(Model):
    url = CharField(max_length=2083)
    access_name = CharField(max_length=32)

    is_menu = BooleanField(default=False)
    icon = CharField(max_length=32, null=True, blank=True)
    def __str__(self):
        return self.access_name