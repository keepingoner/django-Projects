from django.shortcuts import render
from django.views.generic import View
from .models import Course
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from operations.models import UserFav
# Create your views here.


class CourseListView(View):
    def get(self,request):
        active = 'yanse'
        all_courses = Course.objects.all().order_by('-add_time')
        hot_courses = all_courses.order_by('-click_nums')[:3]
        sort = request.GET.get('sort','')
        if sort:
            if sort=='hot':
                all_courses = all_courses.order_by('-click_nums')
            if sort=='students':
                all_courses = all_courses.order_by('-studys')

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_courses,3,request=request)

        all_courses = p.page(page)

        return render(request,'course-list.html',{
            'all_courses':all_courses,
            'sort':sort,
            'hot_courses':hot_courses,
            'active':active,
        })


class CourseDetailView(View):
    def get(self,request,course_id):
        course = Course.objects.get(id=int(course_id))
        tag = course.tag
        if tag:
            tcourses = Course.objects.filter(tag=tag)[:3]
        has_course_fav = False
        has_org_fav = False
        if UserFav.objects.filter(user=request.user, fav_id=int(course_id), fav_type=1):
            has_course_fav = True
        if UserFav.objects.filter(user=request.user, fav_id=int(course.course_org.id), fav_type=2):
            has_org_fav = True
        return render(request,'course-detail.html',{
            'course':course,
            'tcourses':tcourses,
            'has_org_fav':has_org_fav,
            'has_course_fav':has_course_fav,
        })


class CourseInfoView(View):
    def get(self, request, course_id):
        course = Course.objects.get(id=int(course_id))
        return render(request, 'course-video.html', {
            'course': course,
        })


