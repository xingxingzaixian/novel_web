# encoding: utf-8
"""
@version: 1.0
@author: 
@file: urls
@time: 2019-06-24 00:06
"""

from django.urls import path
from users.views import RegisterView, UserInfosView

urlpatterns = [
    path("register", RegisterView.as_view()),
    path("userinfos", UserInfosView.as_view())
]