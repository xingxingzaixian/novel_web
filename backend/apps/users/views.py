# encoding: utf-8
"""
@version: 1.0
@author: 
@file: views
@time: 2019-06-22 23:20
"""
from django.db.models import Q
from rest_framework.views import APIView
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password
from users.models import UserProfile

class RegisterView(APIView):
    # 注册视图中无需进行验证
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        username = request.data.get("username", None)
        password = request.data.get("password", None)
        confirm_password = request.data.get("confirm_password")
        email = request.data.get("email", None)
        mobile = request.data.get("mobile", None)

        result = {}
        if not any([username, email, mobile]):
            result["status_code"] = 1001
            return JsonResponse(result)
        try:
            UserProfile.objects.get(Q(username=username)|Q(email=email)|Q(mobile=mobile))
        except UserProfile.DoesNotExist:
            pass
        else:
            result["status_code"] = 1005
            return JsonResponse(result)

        if password != confirm_password:
            result["status_code"] = 1002
            return JsonResponse(result)

        user = UserProfile(username=username, password=make_password(password), email=email, mobile=mobile)
        user.save()
        result["status_code"] = 1000
        return JsonResponse(result)

class UserInfosView(APIView):
    authentication_classes = []
    permission_classes = []
    def get(self, request):
        users = UserProfile.objects.all()
        return JsonResponse(users)