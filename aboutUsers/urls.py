from django.urls import path
from car import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from django.conf import settings
from django.conf.urls.static import static

# 创建一个 DefaultRouter 实例
router = DefaultRouter()

# 注册视图集
router.register(r'reg', UsersViewSet)



# 包含生成的 URL 到 urlpatterns
urlpatterns = [
    path('', include(router.urls)),
    path('learnAboutUser/', CurrentUserAPIView.as_view(), name='learn_about_user'),
    path('CheckCodeView_reg/', CheckCodeView_reg.as_view(),name='codeCheck'),
    path("sendCode_reg/",sendCodeView_reg.as_view(),name='sendCode_reg'),
    path('CheckCodeView_login/', CheckCodeView_login.as_view(),name='CheckCodeView_login'),
    path("sendCode_login/",sendCodeView_login.as_view(),name='sendCode_login'),
]