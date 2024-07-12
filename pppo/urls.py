"""
URL configuration for djangorf project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.documentation import include_docs_urls
import aboutUsers

'导入模块'
from rest_framework_simplejwt.views import token_obtain_pair, token_verify, token_refresh
from aboutUsers.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("rest_framework.urls")),
    path('car/', include('car.urls')),
    path('login/', token_obtain_pair),  # 登录  签发token
	path('verify/', token_verify),  # 验证token 是否有效
    path('refresh/', token_refresh),  # 刷新token
    path('aboutUsers/', include('aboutUsers.urls')),
    path('docs/', include_docs_urls(title='后端接口文档'))

]
#添加静态路由，以便在开发环境中提供 MEDIA 文件的访问
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)