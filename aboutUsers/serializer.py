import re

from django.http import JsonResponse
from rest_framework import serializers
from .models import *
from django.contrib.auth import authenticate
class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model= EmailVerification
        fields = '__all__'

class UsersRegSerializer(serializers.ModelSerializer):
    username=serializers.CharField(required=True,error_messages={
        "required":"请输入用户名",
        "blank":"用户名不允许为空",
        "min_length":"用户名长度至少为6位"
    })
    email = serializers.EmailField(required=True)
    password=serializers.CharField(required=True,min_length=6)

    class Meta:
        model=Users
        fields=("username","password","email")

    def create(self, validated_data):
         user = super().create(validated_data=validated_data)
         user.set_password(validated_data["password"])
         user.save()
         return user

    def validate_username(self,username):
        #判断用户名是否注册
        if Users.objects.filter(username=username).count():
            raise serializers.ValidationError("用户名已经存在，请查询")
            #return JsonResponse({'errors': serializers.errors}, status=500)
        return username

    def validate_email(self, email):
        if Users.objects.filter(email=email).exists():
            raise serializers.ValidationError("邮箱已经存在，请更换或重新发送验证码")
        elif EmailVerification.objects.filter(email=email).count():
            EmailVerification.objects.filter(email=email).delete()
            return email
        else:raise serializers.ValidationError("邮箱未经验证，请更换或重新发送验证码")

class UsersUpdateSerializer(serializers.ModelSerializer):
    #user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    username=serializers.CharField(read_only=True,error_messages={
        "required":"请输入用户名",
        "blank":"用户名不允许为空",
        "min_length":"用户名长度至少为6位"
    })
    # email=serializers.CharField(read_only=True)
    class Meta:
        model=Users
        fields = '__all__'


class PasswordUpdateSerializer(serializers.Serializer):
    current_password = serializers.CharField(required=True, write_only=True, min_length=6)
    new_password = serializers.CharField(required=True, write_only=True, min_length=6)

    def validate(self, attrs):
        user = self.context['request'].user

        # 检查用户是否已经认证，如果没有认证则抛出错误
        if user.is_anonymous:
            raise serializers.ValidationError("用户未认证或未登录")

        # 检查当前密码是否正确
        if not user.check_password(attrs.get('current_password')):
            raise serializers.ValidationError("当前密码不正确")

        # 检查新密码与当前密码是否相同
        if attrs.get('current_password') == attrs.get('new_password'):
            raise serializers.ValidationError("新密码不能与当前密码相同")

        return attrs

    def create(self, validated_data):
        # 不需要实现 create 方法，因为我们只需要在 validate 方法中验证数据即可
        pass

    def update(self, instance, validated_data):
        # 不需要实现 update 方法，因为我们只需要在 validate 方法中验证数据即可
        pass