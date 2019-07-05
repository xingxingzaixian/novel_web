# encoding: utf-8
"""
@version: 1.0
@author: 
@file: urls
@time: 2019-06-27 23:43
"""
from django.urls import path, re_path
from fiction import views

urlpatterns = [
    path('novel/', views.NovelInfoView.as_view({'get': 'list', 'post': 'create'})),
    re_path('^novel/(?P<pk>\d+)/$', views.NovelInfoView.as_view({'get': 'retrieve'})),
    path('chapter/', views.NovelChapterView.as_view({'get': 'list'})),
    re_path('^chapter/(?P<pk>\d+)/$', views.NovelChapterView.as_view({'get': 'retrieve'}))
]