from django.db import models

# Create your models here.

class UserType(models.Model):
    name = models.CharField(max_length=50)

class UserInfo(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()
    user_type = models.ForeignKey('UserType')

class UserGroup(models.Model):
    groupname = models.CharField(max_length=50)
    user = models.ManyToManyField('UserInfo')

class Asset(models.Model):
    hostname = models.CharField(max_length=256)
    ip = models.GenericIPAddressField()
    location = models.CharField(max_length=100)
    create_date = models.DateTimeField(auto_now_add = True)
    user_group = models.ForeignKey('UserGroup')