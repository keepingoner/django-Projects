import xadmin
from .models import CityDict,CourseOrg,Teacher

class CityDictAdmin(object):
    list_display = ['name','desc','add_time']
    search_fields = ['name','add_time']
    list_filter = ['name','add_time']


class CourseOrgAdmin(object):
    list_display = ['name', 'click_nums', 'fav_nums','address','city','add_time']
    search_fields = ['name', 'add_time','city__name']
    list_filter = ['name', 'add_time','city']


class TeacherAdmin(object):
    list_display = ['name', 'courseorg', 'work_year', 'click_nums']
    search_fields = ['name', 'courseorg__name', 'work_year']
    list_filter = ['name', 'courseorg', 'work_year']

xadmin.site.register(CityDict,CityDictAdmin)
xadmin.site.register(CourseOrg,CourseOrgAdmin)
xadmin.site.register(Teacher,TeacherAdmin)