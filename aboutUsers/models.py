from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser

from django.utils import timezone


class EmailVerification(models.Model):
    email = models.EmailField(unique=True)
    code = models.CharField(max_length=4)
    expire_time = models.DateTimeField(default=timezone.now)

    def is_valid(self):
        """检查验证码是否有效（即未过期）"""
        return self.expire_time > timezone.now()



class Users(AbstractUser):
    first_name = None
    last_name = None
    name=models.CharField(max_length=100,blank=True,null=True)
    email = models.CharField( verbose_name="邮箱", max_length=40, help_text="邮箱")
    GENDER_CHOICES = (
        (0, "未知"),
        (1, "男"),
        (2, "女"),
    )
    gender = models.IntegerField(
        choices=GENDER_CHOICES, default=0, verbose_name="性别", null=True, blank=True, help_text="性别"
    )
    class Meta:
        db_table = "system_users"
        verbose_name = "用户表"
        verbose_name_plural = verbose_name

# Create your models here.

