# encoding: utf-8
"""
@version: 1.0
@author: 
@file: serializers
@time: 2019-06-28 00:14
"""
from rest_framework import serializers
from rest_framework import exceptions
from rest_framework.serializers import ModelSerializer
from django.conf import settings
from fiction.models import NovelInfo, NovelChapter, NovelAudio

class InfoSerializer(ModelSerializer):
    home = serializers.CharField()

    def validate_home(self, value):
        check_host = False
        for host in settings.BASE_URL_HOST:
            if value.startswith(host):
                check_host = True
                break
        if not check_host:
            raise exceptions.ValidationError("The host url must be start with [%s]" % (",".join(settings.BASE_URL_HOST)))
        return value

    class Meta:
        model = NovelInfo
        fields = "__all__"

class ChapterSerializer(ModelSerializer):
    novel_name = serializers.CharField(source='novel_info.name')
    class Meta:
        model = NovelChapter
        fields = ["id", "serial_id", "title", "novel_name", "flag"]

class ChapterContentSerializer(ChapterSerializer):
    class Meta:
        model = NovelChapter
        fields = ["id", "serial_id", "title", "novel_name", "content", "flag"]

class AudioSerializer(ModelSerializer):
    class Meta:
        model = NovelAudio
        fields = "__all__"