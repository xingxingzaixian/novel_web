# encoding: utf-8
"""
@version: 1.0
@author: 
@file: models
@time: 2019-06-24 07:13
"""
from django.db import models
from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):
    uid = models.CharField(max_length=64, null=False, unique=True)
    mobile = models.CharField(max_length=11, null=True, blank=True, unique=True)
