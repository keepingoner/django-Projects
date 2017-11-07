import xadmin
from .models import UserAsk,UserMessage,CourseComments,UserCourse,UserFav


class UserAskAdmin(object):
    list_display = ['name','mobile','coursename','add_time']
    search_fields = ['name','mobile__name','coursename']
    list_filter = ['name','mobile','coursename']



class UserMessageAdmin(object):
    list_display = ['user', 'has_read',  'add_time']
    search_fields = ['user', 'has_read', 'add_time']
    list_filter = ['user', 'has_read','add_time']


class CourseCommentsAdmin(object):
    list_display = ['user', 'course', 'comment', 'add_time']
    search_fields = ['user__name', 'course__name', ]
    list_filter = ['user', 'course']


class UserCourseAdmin(object):
    list_display = ['user', 'course','add_time']
    search_fields = ['user__name', 'course__name', ]
    list_filter = ['user', 'course']



class UserFavAdmin(object):
    list_display = ['user', 'fav_type','add_time']
    search_fields = ['fav_type', 'user__name']
    list_filter = ['fav_type', 'user']


xadmin.site.register(UserAsk,UserAskAdmin)
xadmin.site.register(UserMessage,UserMessageAdmin)
xadmin.site.register(CourseComments,CourseCommentsAdmin)
xadmin.site.register(UserCourse,UserCourseAdmin)
xadmin.site.register(UserFav,UserFavAdmin)