from django.conf.urls import url,include
from django.conf.urls.static import static
from jiaoyu.settings import MEDIA_ROOT,MEDIA_URL
from .views import CourseListView,CourseDetailView,CourseInfoView


urlpatterns = [
    url(r'^course_list/$',CourseListView.as_view(),name='course_list'),
    url(r'^course_detail/(?P<course_id>.*)/$',CourseDetailView.as_view(),name='course_detail'),
    url(r'^course_info/(?P<course_id>.*)/$',CourseInfoView.as_view(),name='course_info '),

]+static(MEDIA_URL,document_root=MEDIA_ROOT)
