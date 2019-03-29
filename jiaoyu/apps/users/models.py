from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=20, verbose_name="昵称")
    birday = models.DateField(verbose_name="生日", null=True, blank=True)
    sex = models.CharField(choices=(("male", "男"), ("female", "女")), max_length=6, verbose_name="性别")
    mobile = models.CharField(max_length=11, verbose_name="手机号", null=True, blank=True)
    address = models.CharField(max_length=50, default="")
    image = models.ImageField(upload_to="user/%Y/%m", max_length=500)

    class Meta:
        verbose_name = "用户表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=10, verbose_name="验证码")
    email = models.EmailField(max_length=30, verbose_name="邮箱")
    send_type = models.CharField(choices=(("register", "注册"), ("forget", "找回密码")), verbose_name="验证类型", max_length=10)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="时间")

    class Meta:
        verbose_name = "邮箱验证"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code


class Banner(models.Model):
    title = models.CharField(verbose_name="标题", max_length=40)
    image = models.ImageField(upload_to="banner/%Y/%m", verbose_name="图像")
    url = models.URLField(max_length=200, verbose_name="跳转地址", default="")
    index = models.IntegerField(default=100, verbose_name="顺序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "轮播表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
