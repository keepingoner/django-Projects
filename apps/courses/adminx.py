import xadmin
from .models import Course,Lesson,Video,CourseResource


class CourseAdmin(object):
    list_display = ['name','courtime','click_nums','studys' ]
    search_fields = ['name','studys']
    list_filter = ['name','studys']


class LessonAdmin(object):
    list_display = ['name', 'course', 'add_time']
    search_fields = ['name', 'course__name']
    list_filter = ['name', 'course']



class VideoAdmin(object):
    list_display = ['name', 'lesson', 'add_time']
    search_fields = ['name', 'lesson__name']
    list_filter = ['name', 'lesson']



class CourseResourceAdmin(object):
    list_display = ['name', 'course', 'add_time']
    search_fields = ['name', 'course__name']
    list_filter = ['name', 'course']


xadmin.site.register(Course,CourseAdmin)
xadmin.site.register(Lesson,LessonAdmin)
xadmin.site.register(Video,VideoAdmin)
xadmin.site.register(CourseResource,CourseResourceAdmin)