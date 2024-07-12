from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import Users
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import get_user_model
from django.conf import settings
import jwt
from .models import *
from .code import *

#注册这里在序列化器的is——valid删除验证码表相关数据
class sendCodeView_reg(APIView):
    def post(self, request, format=None):
        # 解析请求体中的邮箱
        email = request.data.get('email')
        # 检查邮箱是否已经注册
        if Users.objects.filter(email=email).exists():
            return Response({'error': '邮箱已注册，请登录'}, status=status.HTTP_400_BAD_REQUEST)
        # 调用 reg_email 函数发送邮件
        result = reg_email(email)
        if result==email:
            return Response({'ok': True, 'email': "不告诉你"}, status=status.HTTP_200_OK)
        else :
            return Response({'error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CheckCodeView_reg(APIView):
    def post(self, request, format=None):
        # 解析请求体中的邮箱和验证码
        email = request.data.get('email')
        code = request.data.get('code')
        # 查找对应的验证码记录
        try:
            verification = EmailVerification.objects.get(email=email)
            expire_time = verification.expire_time
        except EmailVerification.DoesNotExist:
            return Response({'error': 'Email not found'}, status=status.HTTP_404_NOT_FOUND)

        if expire_time > timezone.now():
            if verification.code == code:
                return Response({'message': 'Verification successful'}, status=status.HTTP_200_OK)
            else: return Response({'error': 'Invalid verification code'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            verification.delete()
            return Response({'error': 'Verification code expired'}, status=status.HTTP_400_BAD_REQUEST)

#登录是验证成功删除验证码表相关数据即可
class sendCodeView_login(APIView):
    def post(self, request, format=None):
        # 解析请求体中的邮箱
        email = request.data.get('email')
        #邮箱登录
        if Users.objects.filter(email=email).exists():
            result = reg_email(email)
            if result == email:
                return Response({'ok': True, 'email': result}, status=status.HTTP_200_OK)
            else:
                return Response({'error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        #用户名登录
        elif Users.objects.filter(username=email).exists():
            email=Users.objects.get(username=email).email
            result = reg_email(email)
            if result == email:
                return Response({'ok': True, 'email': "不告诉你"}, status=status.HTTP_200_OK)
            else:
                return Response({'error'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        # 检查邮箱是否已经注册
        else:
            return Response({'error': '未注册，请注册'}, status=status.HTTP_400_BAD_REQUEST)


class CheckCodeView_login(APIView):
    def post(self, request, format=None):
        # 解析请求体中的邮箱和验证码
        email = request.data.get('email')
        code = request.data.get('code')

        # 查找对应的验证码记录

        user=None
        verification = None
        # 邮箱登录
        if Users.objects.filter(email=email).exists():
            user=Users.objects.get(email=email)
            verification = EmailVerification.objects.get(email=email)
        # 用户名登录
        elif Users.objects.filter(username=email).exists():
            user=Users.objects.get(username=email)
            email=user.email
            verification = EmailVerification.objects.get(email=email)

        if not verification or not user:
            return Response({'error': 'Email or username not found'}, status=status.HTTP_404_NOT_FOUND)

        # 检查验证码是否有效（未过期）
        if verification.expire_time > timezone.now():
            print(verification.code,code)
            if verification.code == code:
                # 验证成功，签发JWT Token
                verification.delete()
                token = AccessToken.for_user(user)  # 假设有一个关联的用户对象
                return Response({'message': 'Verification successful', 'token': str(token)}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid verification code'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            verification.delete()
            return Response({'error': 'Verification code expired'}, status=status.HTTP_400_BAD_REQUEST)

class UsersViewSet(ModelViewSet):
    queryset = Users.objects.all()

    def get_serializer_class(self):
        if self.action == "create":
            return UsersRegSerializer
        elif self.action == "retrieve" or self.action == "update":
            return UsersUpdateSerializer
        return UsersUpdateSerializer

    def get_permissions(self):
        if self.action in ["retrieve", "update", "put"]:
            return [IsAuthenticated()]
        return []  # 默认情况下，不设置任何权限

    @action(detail=False, methods=['put'], url_path='update-password')
    def update_password(self, request):
        serializer = PasswordUpdateSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = request.user  # 获取当前认证的用户
            user.set_password(serializer.validated_data['new_password'])
            user.save()
            return Response({"message": "密码更新成功"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    authentication_classes = [JWTAuthentication]  # 将身份验证类作为列表


class CurrentUserAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            # 获取 Authorization 头部，从中提取出 token
            authorization_header = request.headers.get('Authorization')
            if not authorization_header or not authorization_header.startswith('JWT '):
                raise AuthenticationFailed('Invalid Authorization header format')

            # 提取 token
            token = authorization_header.split()[1]

            # 解码 token，验证签名
            decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])

            # 获取用户 ID
            user_id = decoded_token['user_id']

            # 查询用户信息
            user = Users.objects.get(id=user_id)

            # 构造响应数据，返回用户信息
            data = {
                "id":user_id,
                'username': user.username,
                'email': user.email,
                'gender': user.gender,
                'name': user.name,
                'is_superuser': user.is_superuser
                # 可以添加其他需要返回的用户信息字段
            }
            return Response(data, status=status.HTTP_200_OK)

        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Token expired. Please login again.')
        except jwt.InvalidTokenError:
            raise AuthenticationFailed('Invalid token. Please login again.')
        except Users.DoesNotExist:
            raise AuthenticationFailed('User not found.')
