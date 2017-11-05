from datetime import datetime
from django.db import models
from users.models import UserProfile
from courses.models import Course
# Create your models here.

class UserAsk(models.Model):
    # "用户咨询(UserAsk) (姓名，手机，课程名，时间)
    name = models.CharField(max_length=30,verbose_name="姓名")
    mobile = models.CharField(max_length=11, verbose_name="手机号", null=True, blank=True)
    coursename = models.CharField(max_length=50,verbose_name="课程名字")
    add_time = models.DateTimeField(default=datetime.now,verbose_name="咨询时间")

    class Meta:
        verbose_name = "用户咨询"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class UserMessage(models.Model):
    # 用户消息(UserMessage) （接收用户，是否已读，消息，时间）
    user = models.IntegerField(default=0,verbose_name="接收用户")
    has_read = models.BooleanField(default=False,verbose_name="是否已读")
    message = models.CharField(max_length=500,verbose_name="消息详情")
    add_time = models.DateTimeField(default=datetime.now,verbose_name="接收时间")

    class Meta:
        verbose_name = "用户消息"
        verbose_name_plural = verbose_name


class CourseComments(models.Model):
    user = models.ForeignKey(UserProfile,verbose_name="评论用户")
    course = models.ForeignKey(Course,verbose_name="评论课程")
    comment = models.CharField(max_length=500,verbose_name="课程评论")
    add_time = models.DateTimeField(default=datetime.now,verbose_name="评论时间")

    class Meta:
        verbose_name = "用户评论"
        verbose_name_plural = verbose_name


class UserCourse(models.Model):
    user = models.ForeignKey(UserProfile,verbose_name="学习用户")
    course = models.ForeignKey(Course,verbose_name="学习课程")
    add_time = models.DateTimeField(default=datetime.now,verbose_name="时间")

    class Meta:
        verbose_name = "用户学习课程"
        verbose_name_plural = verbose_name


class UserFav(models.Model):
    user = models.ForeignKey(UserProfile,verbose_name="收藏用户")
    fav_id = models.IntegerField(default=0, verbose_name="数据id")
    fav_type = models.IntegerField(choices=((1, '课程'), (2, '课程机构'), (3, '讲师')), default=1, verbose_name="收藏类型")
    add_time = models.DateTimeField(default=datetime.now,verbose_name="收藏时间")

    class Meta:
        verbose_name = "用户收藏"
        verbose_name_plural = verbose_name
