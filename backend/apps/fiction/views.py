# encoding: utf-8
"""
@version: 1.0
@author: 
@file: views
@time: 2019-06-27 23:43
"""
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from fiction.models import NovelInfo, NovelChapter
from fiction.serializers import InfoSerializer, ChapterSerializer, ChapterContentSerializer
from rest_framework.pagination import PageNumberPagination

class NovelInfoView(ModelViewSet):
    queryset = NovelInfo.objects.all().order_by('id')
    serializer_class = InfoSerializer

    def retrieve(self, request, *args, **kwargs):
        path_split = request.path_info.strip("/").split("/")
        if len(path_split) > 1 and path_split[-1].isdigit():
            page = PageNumberPagination()
            instances = NovelChapter.objects.filter(novel_info_id=path_split[-1]).all().order_by('id')
            page_chapters = page.paginate_queryset(queryset=instances, request=request, view=self)
            ser = ChapterSerializer(instance=page_chapters, many=True)
            return page.get_paginated_response(ser.data)
        else:
            super().retrieve(request, *args, **kwargs)

class NovelChapterView(ModelViewSet):
    queryset = NovelChapter.objects.all()
    serializer_class = ChapterSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_content_serializer(instance)
        return Response(serializer.data)

    # 获取章节内容
    def get_content_serializer(self, *args, **kwargs):
        serializer_class = ChapterContentSerializer
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)

# class NovelAudioView(ModelViewSet):
#     queryset = NovelAudio.objects.all()
#     serializer_class = AudioSerializer