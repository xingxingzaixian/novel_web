# encoding: utf-8
"""
@version: 1.0
@author: 
@file: models
@time: 2019-06-27 23:43
"""

from django.db import models

class NovelInfo(models.Model):
    name = models.CharField(max_length=128, verbose_name="小说名")
    home = models.CharField(max_length=64, verbose_name="小说首页")

    class Meta:
        db_table = "novel_info"

class NovelChapter(models.Model):
    serial_id = models.IntegerField(verbose_name="章节序号")
    title = models.CharField(max_length=128, verbose_name="章节名称")
    novel_info = models.ForeignKey(NovelInfo, on_delete=False)
    url = models.CharField(max_length=64, verbose_name="章节地址")
    content = models.TextField(verbose_name="章节内容")
    flag = models.BooleanField(default=False, verbose_name="是否已经合成")

    class Meta:
        db_table = "novel_chapter"

class NovelAudio(models.Model):
    text = models.CharField(max_length=512, verbose_name="合成文字")
    content = models.BinaryField(verbose_name="合成语音内容")

    class Meta:
        db_table = "novel_audio"