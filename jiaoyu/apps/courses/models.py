from datetime import  datetime
from django.db import models
from organizations.models import CourseOrg,Teacher
# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=50,verbose_name="课程名字")
    desc = models.CharField(max_length=200,verbose_name="课程描述")
    detail = models.TextField(verbose_name="课程详情")
    degree = models.CharField(max_length=5,choices = (('cj',"初级"),('gj',"高级"),('zj',"中级")),verbose_name="课程难度",default='cj')
    courtime = models.IntegerField(default=0,verbose_name="课程时长")
    teacher = models.ForeignKey(Teacher,verbose_name='教师',null=True,blank=True)
    click_nums = models.IntegerField(default=0,verbose_name="点击次数")
    course_org = models.ForeignKey(CourseOrg,null=True,blank=True,verbose_name="课程机构")
    fav_nums = models.IntegerField(default=0,verbose_name="收藏此书")
    category = models.CharField(max_length=20,verbose_name="课程类别",default="后台开发")
    image = models.ImageField(upload_to="courses/%Y/%m",verbose_name="课程封面")
    studys = models.IntegerField(default=0,verbose_name="学习人数")
    tag = models.CharField(max_length=40,verbose_name="课程标签",default="服务操作系统")
    add_time = models.DateTimeField(default=datetime.now,verbose_name="登记时间")
    tonggao = models.CharField(default='',max_length=100,verbose_name='课程公告')
    youneed_know = models.CharField(max_length=200,default='',verbose_name='课程须知')
    teacher_tell = models.CharField(max_length=200, default='', verbose_name='老师告诉你学到什么')
    class Meta:
        verbose_name = "课程详情"
        verbose_name_plural = verbose_name

    def get_lesson_nums(self):
        return self.lesson_set.all().count()

    def get_users(self):
        return self.usercourse_set.all()

    def get_lesson(self):
        return self.lesson_set.all()
    def get_resource(self):
        return self.courseresource_set.all()


    def __str__(self):
        return  self.name


class Lesson(models.Model):
    name = models.CharField(max_length=50,verbose_name="章节名")
    course = models.ForeignKey(Course,verbose_name="属于课程")
    add_time = models.DateTimeField(default=datetime.now,verbose_name="登记时间")

    class Meta:
        verbose_name = "章节详情"
        verbose_name_plural = verbose_name
    def get_video(self):
        return self.video_set.all()

    def __str__(self):
        return self.name


class Video(models.Model):
    name = models.CharField(max_length=50,verbose_name="视频名称")
    lesson = models.ForeignKey(Lesson,verbose_name="对应章节")
    videourl = models.CharField(default='',max_length=100,verbose_name='视频地址')
    add_time = models.DateTimeField(default=datetime.now,verbose_name="添加时间")

    class Meta:
        verbose_name = "视频信息"
        verbose_name_plural = verbose_name

    def  __str__(self):
        return  self.name


class CourseResource(models.Model):
    course = models.ForeignKey(Course,verbose_name="对应课程")
    name = models.CharField(max_length=50,verbose_name="资源名称")
    file = models.FileField(upload_to="courses/resource/%Y/%m",verbose_name="文件")
    add_time = models.DateTimeField(default=datetime.now,verbose_name="添加时间")

    class Meta:
        verbose_name = "课程资源"
        verbose_name_plural = verbose_name

    def __str__(self):
        return  self.name
