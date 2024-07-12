from django.core.mail import EmailMessage
from django.template import loader
from .models import *
import random
from pppo import settings
from django.core.exceptions import *
def reg_email(email):
    # 清理过期验证码
    EmailVerification.objects.filter(expire_time__lt=timezone.now()).delete()
    email_title = "验证码"

    # 这里是生成随机验证码 我是4位的，可以自定义
    code = random.randrange(1000, 9999)

    # 这个context这里定义的字段，是要给html模板中的验证码使用的，HTML中{% code %}引用即可
    context = {
        'code': str(code)
    }
    print(str(code))
    # 这里的html文件就是发送验证码部分的html模板我放在下面
    email_template_name = 'regCode.html'
    t = loader.get_template(email_template_name)

    html_content = t.render(context)

    msg = EmailMessage(email_title,  # 邮件主题
                        html_content,  # 邮件内容，使用html模板
                        settings.EMAIL_FROM,  # 用于发送邮件的用户
                        [email]  # 接收邮件的用户列表
                        )

    # 指定邮箱发送的类型
    msg.content_subtype = 'html'

    # 发送邮箱
    if EmailVerification.objects.filter(email=email).exists():
        return ValidationError('发邮箱失败,用户已存在')
    send_status = msg.send()
    if not send_status:
        return ValidationError('发邮箱失败,{}'.format(send_status['errmsg']))

    print(str(code))
    verification = EmailVerification(email=email, code=str(code),
                                     expire_time=timezone.now() + timezone.timedelta(minutes=5))
    verification.save()
    return email