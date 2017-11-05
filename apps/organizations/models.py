from datetime import  datetime
from django.db import models

# Create your models here.


class CityDict(models.Model):
    name = models.CharField(max_length=100,verbose_name="城市")
    desc = models.CharField(default="",verbose_name="描述",max_length=200)
    add_time = models.DateTimeField(default=datetime.now,verbose_name="添加时间")

    class Meta:
        verbose_name  = "城市信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return  self.name

class CourseOrg(models.Model):
    "名字，描述，点击数，收藏数，图像，地址，外键城市，添加时间"
    name = models.CharField(max_length=80,verbose_name="机构名字")
    desc = models.CharField(max_length=80,verbose_name="机构描述")
    students = models.IntegerField(default=0,verbose_name='学习人数')
    courses = models.IntegerField(default=0, verbose_name='课程数')
    category = models.CharField(max_length=20,choices=(('pxjg','培训机构'),('gern','  个人'),('gx','高校')),default='pxjg',verbose_name='机构类别')
    click_nums = models.IntegerField(default=0, verbose_name="点击次数")
    fav_nums = models.IntegerField(default=0, verbose_name="收藏此书")
    image = models.ImageField(upload_to="courses/org/%Y/%m", verbose_name="机构图像")
    address = models.CharField(max_length=200,verbose_name="机构地址")
    city = models.ForeignKey(CityDict,verbose_name="机构城市")
    add_time = models.DateTimeField(default=datetime.now,verbose_name="添加时间")

    class Meta:
        verbose_name = "课程机构"
        verbose_name_plural = verbose_name



    def __str__(self):
        return  self.name

class Teacher(models.Model):
    "所属机构，名称，工作年限，工作公司，工作职位，教学特点，点击"
    courseorg = models.ForeignKey(CourseOrg,verbose_name="所属机构")
    name = models.CharField(max_length=30,verbose_name="讲师名字")
    age = models.IntegerField(default='18',verbose_name='年龄')
    work_year = models.IntegerField(default=0,verbose_name="工作年限")
    work_company = models.CharField(max_length=200,verbose_name="工作单位")
    work_position = models.CharField(max_length=100,verbose_name="工作职位")
    point = models.CharField(max_length=400,verbose_name="教学特点")
    image = models.ImageField(upload_to="org/teacher/%Y/%m",default='',verbose_name="教师头像")
    click_nums = models.IntegerField(default=0, verbose_name="点击次数")
    fav_nums = models.IntegerField(default=0, verbose_name="收藏此书")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "讲师详情"
        verbose_name_plural = verbose_name
    def get_course(self):
        return self.course_set.all()

    def __str__(self):
        return self.name